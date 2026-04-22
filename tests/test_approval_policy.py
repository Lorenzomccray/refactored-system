"""Unit tests for app.policy.approval_policy."""
import logging
from typing import Optional

import pytest

from app.policy.approval_policy import ApprovalPolicy, PolicyConfig
from app.schemas.approval_decision import ApprovalDecision
from app.schemas.approval_request import ApprovalRequest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_request(
    risk_class: str,
    path: Optional[str] = None,
    request_id: str = "req-1",
    task_id: str = "task-1",
    step_id: str = "step-1",
    requested_by: str = "system",
) -> ApprovalRequest:
    metadata = {"path": path} if path is not None else None
    return ApprovalRequest(
        request_id=request_id,
        task_id=task_id,
        step_id=step_id,
        risk_class=risk_class,
        reason="test",
        requested_by=requested_by,
        metadata=metadata,
    )


# ---------------------------------------------------------------------------
# 1. READ_ONLY auto-approval
# ---------------------------------------------------------------------------

class TestReadOnlyAutoApproval:
    def test_read_only_is_approved(self):
        policy = ApprovalPolicy()
        decision = policy.evaluate(make_request("READ_ONLY"))
        assert decision.approved is True
        assert decision.policy_rule == "allow-read-only"
        assert decision.requires_human is False
        assert decision.escalation_target is None

    def test_read_only_does_not_enter_human_review_queue(self):
        policy = ApprovalPolicy()
        policy.evaluate(make_request("READ_ONLY"))
        assert policy.pending_human_reviews == []


# ---------------------------------------------------------------------------
# 2. Unknown risk class fails closed
# ---------------------------------------------------------------------------

class TestUnknownRiskClassFailsClosed:
    def test_unknown_risk_class_is_denied(self):
        policy = ApprovalPolicy()
        decision = policy.evaluate(make_request("TOTALLY_MADE_UP"))
        assert decision.approved is False
        assert decision.policy_rule == "unknown-risk-class"
        assert decision.requires_human is True
        assert decision.escalation_target == "operator"

    def test_unknown_risk_class_is_queued_for_human_review(self):
        policy = ApprovalPolicy()
        policy.evaluate(make_request("TOTALLY_MADE_UP", request_id="req-unk"))
        assert len(policy.pending_human_reviews) == 1
        assert policy.pending_human_reviews[0]["request_id"] == "req-unk"


# ---------------------------------------------------------------------------
# 3. LOCAL_WRITE allowlist (safe classes only when explicitly configured)
# ---------------------------------------------------------------------------

class TestLocalWriteAllowlist:
    def test_local_write_denied_without_config(self):
        """No config → fail closed even if a path is provided."""
        policy = ApprovalPolicy()
        decision = policy.evaluate(make_request("LOCAL_WRITE", path="/tmp/output.txt"))
        assert decision.approved is False
        assert decision.policy_rule == "local-write-no-allowlist"
        assert decision.requires_human is True

    def test_local_write_approved_within_allowed_path(self):
        config = PolicyConfig(allowed_local_write_paths={"/tmp/workspace"})
        policy = ApprovalPolicy(config=config)
        decision = policy.evaluate(make_request("LOCAL_WRITE", path="/tmp/workspace/output.txt"))
        assert decision.approved is True
        assert decision.policy_rule == "allow-local-write"

    def test_local_write_approved_at_exact_allowed_path(self):
        config = PolicyConfig(allowed_local_write_paths={"/tmp/workspace/output.txt"})
        policy = ApprovalPolicy(config=config)
        decision = policy.evaluate(make_request("LOCAL_WRITE", path="/tmp/workspace/output.txt"))
        assert decision.approved is True

    def test_local_write_denied_outside_allowed_path(self):
        config = PolicyConfig(allowed_local_write_paths={"/tmp/workspace"})
        policy = ApprovalPolicy(config=config)
        decision = policy.evaluate(make_request("LOCAL_WRITE", path="/etc/passwd"))
        assert decision.approved is False
        assert decision.policy_rule == "local-write-path-not-allowed"
        assert decision.requires_human is True

    def test_local_write_denied_without_path_in_metadata(self):
        config = PolicyConfig(allowed_local_write_paths={"/tmp/workspace"})
        policy = ApprovalPolicy(config=config)
        decision = policy.evaluate(make_request("LOCAL_WRITE", path=None))
        assert decision.approved is False
        assert decision.policy_rule == "local-write-missing-path"
        assert decision.requires_human is True

    def test_path_traversal_blocked(self):
        """/../ sequences that escape the allowed prefix must be denied."""
        config = PolicyConfig(allowed_local_write_paths={"/tmp/workspace"})
        policy = ApprovalPolicy(config=config)
        decision = policy.evaluate(
            make_request("LOCAL_WRITE", path="/tmp/workspace/../../../etc/passwd")
        )
        assert decision.approved is False

    def test_prefix_collision_blocked(self):
        """'/tmp/workspace2' must not match the '/tmp/workspace' prefix."""
        config = PolicyConfig(allowed_local_write_paths={"/tmp/workspace"})
        policy = ApprovalPolicy(config=config)
        decision = policy.evaluate(make_request("LOCAL_WRITE", path="/tmp/workspace2/evil.txt"))
        assert decision.approved is False

    def test_other_risk_classes_not_auto_approved_by_allowlist(self):
        """A LOCAL_WRITE allowlist must not affect other risk classes.

        All RiskClass members except READ_ONLY and LOCAL_WRITE must remain
        fail-closed, requiring human review.  This list is built dynamically
        from the enum so that newly added risk classes are automatically
        covered.
        """
        from app.policy.risk_engine import RiskClass as RC

        exempt = {RC.READ_ONLY, RC.LOCAL_WRITE}
        config = PolicyConfig(allowed_local_write_paths={"/tmp/workspace"})
        policy = ApprovalPolicy(config=config)
        for risk in RC:
            if risk in exempt:
                continue
            decision = policy.evaluate(make_request(risk.value))
            assert decision.approved is False, f"{risk.value} should not be auto-approved"
            assert decision.requires_human is True


# ---------------------------------------------------------------------------
# 4. Human-review escalation path
# ---------------------------------------------------------------------------

class TestHumanReviewEscalation:
    def test_hook_called_when_decision_requires_human(self):
        calls = []

        def hook(decision: ApprovalDecision, request: ApprovalRequest):
            calls.append((decision, request))

        policy = ApprovalPolicy(human_review_hook=hook)
        policy.evaluate(make_request("LOCAL_EXECUTION"))
        assert len(calls) == 1
        decision, request = calls[0]
        assert decision.requires_human is True

    def test_hook_not_called_for_auto_approved(self):
        calls = []

        def hook(decision, request):
            calls.append((decision, request))

        policy = ApprovalPolicy(human_review_hook=hook)
        policy.evaluate(make_request("READ_ONLY"))
        assert calls == []

    def test_hook_receives_correct_request(self):
        received = []

        def hook(decision, request):
            received.append(request)

        policy = ApprovalPolicy(human_review_hook=hook)
        policy.evaluate(make_request("CREDENTIAL_USE", request_id="req-cred"))
        assert received[0].request_id == "req-cred"

    def test_human_review_queue_populated_on_escalation(self):
        policy = ApprovalPolicy()
        policy.evaluate(make_request("LOCAL_EXECUTION", request_id="req-exec"))
        assert len(policy.pending_human_reviews) == 1
        entry = policy.pending_human_reviews[0]
        assert entry["request_id"] == "req-exec"
        assert entry["risk_class"] == "LOCAL_EXECUTION"
        assert entry["escalation_target"] == "operator"

    def test_multiple_escalations_accumulate_in_queue(self):
        policy = ApprovalPolicy()
        policy.evaluate(make_request("LOCAL_EXECUTION", request_id="req-1"))
        policy.evaluate(make_request("CREDENTIAL_USE", request_id="req-2"))
        assert len(policy.pending_human_reviews) == 2

    def test_no_hook_no_error_on_escalation(self):
        """If no hook is registered, escalation should not raise."""
        policy = ApprovalPolicy()
        decision = policy.evaluate(make_request("IRREVERSIBLE"))
        assert decision.requires_human is True


# ---------------------------------------------------------------------------
# 5. Structured audit logging
# ---------------------------------------------------------------------------

class TestAuditLogging:
    _logger_name = "app.policy.approval_policy"

    def test_audit_log_emitted_for_approved(self, caplog):
        policy = ApprovalPolicy()
        with caplog.at_level(logging.INFO, logger=self._logger_name):
            policy.evaluate(make_request("READ_ONLY", request_id="req-ro"))
        records = [r for r in caplog.records if r.message == "approval_decision"]
        assert len(records) == 1
        assert records[0].request_id == "req-ro"
        assert records[0].approved is True
        assert records[0].policy_rule == "allow-read-only"

    def test_audit_log_emitted_for_denied(self, caplog):
        policy = ApprovalPolicy()
        with caplog.at_level(logging.INFO, logger=self._logger_name):
            policy.evaluate(make_request("CREDENTIAL_USE", request_id="req-cred"))
        records = [r for r in caplog.records if r.message == "approval_decision"]
        assert len(records) == 1
        assert records[0].approved is False
        assert records[0].requires_human is True

    def test_audit_log_contains_structured_fields(self, caplog):
        policy = ApprovalPolicy()
        with caplog.at_level(logging.INFO, logger=self._logger_name):
            policy.evaluate(
                make_request("READ_ONLY", request_id="req-fields", task_id="t1", step_id="s1")
            )
        record = next(r for r in caplog.records if r.message == "approval_decision")
        assert record.request_id == "req-fields"
        assert record.task_id == "t1"
        assert record.step_id == "s1"
        assert record.risk_class == "READ_ONLY"

    def test_audit_log_emitted_for_unknown_risk_class(self, caplog):
        policy = ApprovalPolicy()
        with caplog.at_level(logging.INFO, logger=self._logger_name):
            policy.evaluate(make_request("BOGUS_CLASS"))
        records = [r for r in caplog.records if r.message == "approval_decision"]
        assert len(records) == 1
        assert records[0].approved is False
        assert records[0].policy_rule == "unknown-risk-class"

    def test_audit_log_emitted_once_per_evaluate_call(self, caplog):
        policy = ApprovalPolicy()
        with caplog.at_level(logging.INFO, logger=self._logger_name):
            policy.evaluate(make_request("READ_ONLY"))
            policy.evaluate(make_request("LOCAL_EXECUTION"))
        records = [r for r in caplog.records if r.message == "approval_decision"]
        assert len(records) == 2
