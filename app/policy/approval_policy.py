import logging
import os
from collections import deque
from dataclasses import dataclass, field
from typing import Callable, Deque, List, Optional, Set

from app.policy.risk_engine import RiskClass
from app.schemas.approval_decision import ApprovalDecision
from app.schemas.approval_request import ApprovalRequest

logger = logging.getLogger(__name__)


@dataclass
class PolicyConfig:
    """Allowlist configuration for :class:`ApprovalPolicy`.

    ``allowed_local_write_paths`` is the set of directory prefixes that
    ``LOCAL_WRITE`` actions are permitted to write into.  The policy is
    fail-closed: if the set is empty *or* the request carries no path, the
    action is denied and sent to human review.
    """

    allowed_local_write_paths: Set[str] = field(default_factory=set)


class ApprovalPolicy:
    """Fail-closed approval policy with allowlist, structured audit logging,
    and a human-review queue/hook.

    Backward-compatible with the original scaffold: callers that do not pass a
    ``PolicyConfig`` or ``human_review_hook`` get the same fail-closed
    behaviour as before, plus audit logging and queue support.
    """

    def __init__(
        self,
        config: Optional[PolicyConfig] = None,
        human_review_hook: Optional[Callable[[ApprovalDecision, ApprovalRequest], None]] = None,
    ) -> None:
        self.config = config or PolicyConfig()
        self.human_review_hook = human_review_hook
        self._human_review_queue: Deque[dict] = deque()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def evaluate(self, request: ApprovalRequest) -> ApprovalDecision:
        """Evaluate *request* and return an :class:`ApprovalDecision`.

        Every decision is:
        1. Audited via structured logging.
        2. Enqueued for human review (and the hook fired) when
           ``requires_human`` is ``True``.
        """
        decision = self._evaluate_inner(request)
        self._audit(request, decision)
        if decision.requires_human:
            self._enqueue_human_review(request, decision)
        return decision

    @property
    def pending_human_reviews(self) -> List[dict]:
        """Snapshot of queued entries that need human review."""
        return list(self._human_review_queue)

    # ------------------------------------------------------------------
    # Internal evaluation helpers
    # ------------------------------------------------------------------

    def _evaluate_inner(self, request: ApprovalRequest) -> ApprovalDecision:
        try:
            risk = RiskClass(request.risk_class)
        except ValueError:
            return ApprovalDecision(
                request_id=request.request_id,
                approved=False,
                policy_rule="unknown-risk-class",
                reason="Risk class is not recognized.",
                requires_human=True,
                escalation_target="operator",
            )

        if risk == RiskClass.READ_ONLY:
            return ApprovalDecision(
                request_id=request.request_id,
                approved=True,
                policy_rule="allow-read-only",
                reason="Read-only work is allowed in the minimal scaffolding path.",
            )

        if risk == RiskClass.LOCAL_WRITE:
            return self._evaluate_local_write(request)

        return ApprovalDecision(
            request_id=request.request_id,
            approved=False,
            policy_rule="require-human-approval",
            reason=f"{risk.value} is not auto-approved in the minimal scaffolding path.",
            requires_human=True,
            escalation_target="operator",
        )

    def _evaluate_local_write(self, request: ApprovalRequest) -> ApprovalDecision:
        """Approve LOCAL_WRITE only when a non-empty allowlist is configured
        and the requested path is within one of the approved prefixes."""
        metadata = request.metadata or {}
        path: Optional[str] = metadata.get("path")

        if not self.config.allowed_local_write_paths:
            return ApprovalDecision(
                request_id=request.request_id,
                approved=False,
                policy_rule="local-write-no-allowlist",
                reason="LOCAL_WRITE is not approved: no allowed paths are configured.",
                requires_human=True,
                escalation_target="operator",
            )

        if not path:
            return ApprovalDecision(
                request_id=request.request_id,
                approved=False,
                policy_rule="local-write-missing-path",
                reason="LOCAL_WRITE is not approved: no target path provided in request metadata.",
                requires_human=True,
                escalation_target="operator",
            )

        normalized = os.path.normpath(path)
        for allowed in self.config.allowed_local_write_paths:
            normalized_allowed = os.path.normpath(allowed)
            if normalized == normalized_allowed or normalized.startswith(
                normalized_allowed + os.sep
            ):
                return ApprovalDecision(
                    request_id=request.request_id,
                    approved=True,
                    policy_rule="allow-local-write",
                    reason=f"LOCAL_WRITE to '{path}' is within an approved path.",
                )

        return ApprovalDecision(
            request_id=request.request_id,
            approved=False,
            policy_rule="local-write-path-not-allowed",
            reason=f"LOCAL_WRITE to '{path}' is outside all approved paths.",
            requires_human=True,
            escalation_target="operator",
        )

    # ------------------------------------------------------------------
    # Audit and human-review plumbing
    # ------------------------------------------------------------------

    def _audit(self, request: ApprovalRequest, decision: ApprovalDecision) -> None:
        """Emit a structured audit log entry for every approval decision."""
        logger.info(
            "approval_decision",
            extra={
                "request_id": request.request_id,
                "task_id": request.task_id,
                "step_id": request.step_id,
                "risk_class": request.risk_class,
                "requested_by": request.requested_by,
                "approved": decision.approved,
                "policy_rule": decision.policy_rule,
                "requires_human": decision.requires_human,
                "escalation_target": decision.escalation_target,
            },
        )

    def _enqueue_human_review(
        self, request: ApprovalRequest, decision: ApprovalDecision
    ) -> None:
        """Add a human-review entry to the internal queue and fire the hook."""
        entry = {
            "request_id": request.request_id,
            "task_id": request.task_id,
            "step_id": request.step_id,
            "risk_class": request.risk_class,
            "reason": decision.reason,
            "policy_rule": decision.policy_rule,
            "escalation_target": decision.escalation_target,
        }
        self._human_review_queue.append(entry)
        if self.human_review_hook is not None:
            self.human_review_hook(decision, request)

