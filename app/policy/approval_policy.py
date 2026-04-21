from app.policy.risk_engine import RiskClass
from app.schemas.approval_decision import ApprovalDecision
from app.schemas.approval_request import ApprovalRequest


class ApprovalPolicy:
    """Minimal fail-closed approval scaffold for the first code milestone."""

    def evaluate(self, request: ApprovalRequest) -> ApprovalDecision:
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

        return ApprovalDecision(
            request_id=request.request_id,
            approved=False,
            policy_rule="require-human-approval",
            reason=f"{risk.value} is not auto-approved in the minimal scaffolding path.",
            requires_human=True,
            escalation_target="operator",
        )
