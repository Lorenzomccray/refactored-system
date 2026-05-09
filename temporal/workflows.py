"""Temporal workflow skeletons for the Sovereign AI Work Operating System.

These workflows encode the governed execution loop and Sovereign Upgrade Plane.
They are intentionally activity-driven: tool calls, policy checks, registry
updates, receipts, and Cortex writes must be implemented behind governed
activities rather than inside workflow code.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Optional

from temporalio import workflow


class CapabilityState(str, Enum):
    DISCOVERED = "DISCOVERED"
    INSPECTING = "INSPECTING"
    CLASSIFIED = "CLASSIFIED"
    CONTRACTIFYING = "CONTRACTIFYING"
    SANDBOX_PENDING = "SANDBOX_PENDING"
    SANDBOX_TESTING = "SANDBOX_TESTING"
    SANDBOX_FAILED = "SANDBOX_FAILED"
    SANDBOX_PASSED = "SANDBOX_PASSED"
    AWAITING_APPROVAL = "AWAITING_APPROVAL"
    APPROVED_FOR_PROMOTION = "APPROVED_FOR_PROMOTION"
    REGISTERED_DISABLED = "REGISTERED_DISABLED"
    MONITOR_MODE = "MONITOR_MODE"
    ACTIVE_GOVERNED = "ACTIVE_GOVERNED"
    SUSPENDED = "SUSPENDED"
    ROLLBACK_REQUESTED = "ROLLBACK_REQUESTED"
    ROLLING_BACK = "ROLLING_BACK"
    ROLLED_BACK = "ROLLED_BACK"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    NEEDS_HUMAN_REVIEW = "NEEDS_HUMAN_REVIEW"
    REJECTED = "REJECTED"
    DEPRECATED = "DEPRECATED"


@dataclass
class HumanApprovalSignal:
    approved: bool
    approved_by: str
    justification: str


@dataclass
class PromotionApprovalSignal:
    approved: bool
    approved_by: str
    justification: str
    approved_scope: str
    approved_operations: list[str]


@dataclass
class StepApprovalSignal:
    step_id: str
    approved: bool
    approved_by: str
    justification: str


@workflow.defn
class GovernedAgentRunWorkflow:
    """Durable governed agent run.

    Core loop:
    input → deterministic plan → risk classification → approval signal if risky
    → MCP activity dispatch → verification → receipt → terminal status.
    """

    def __init__(self) -> None:
        self.approvals: dict[str, StepApprovalSignal] = {}

    @workflow.signal
    async def approve_step(self, signal: StepApprovalSignal) -> None:
        self.approvals[signal.step_id] = signal

    @workflow.query
    def approval_status(self) -> dict[str, Any]:
        return {step_id: approval.__dict__ for step_id, approval in self.approvals.items()}

    @workflow.run
    async def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        plan = await workflow.execute_activity(
            "generate_deterministic_plan",
            payload,
            start_to_close_timeout=timedelta(minutes=2),
        )

        trace: list[dict[str, Any]] = []
        outputs: list[dict[str, Any]] = []

        for step in plan["steps"]:
            risk = await workflow.execute_activity(
                "classify_risk",
                step,
                start_to_close_timeout=timedelta(minutes=1),
            )
            step["risk"] = risk
            trace.append({"event": "risk_classified", "step": step})

            if risk["risk_class"] == "IRREVERSIBLE":
                blocked_receipt = await workflow.execute_activity(
                    "generate_receipt",
                    {
                        "status": "blocked",
                        "reason": "IRREVERSIBLE action blocked by policy",
                        "payload": payload,
                        "plan": plan,
                        "trace": trace,
                    },
                    start_to_close_timeout=timedelta(minutes=2),
                )
                return {"status": "blocked", "receipt": blocked_receipt, "trace": trace}

            if risk.get("approval_required", False):
                await workflow.execute_activity(
                    "create_human_approval_request",
                    {"payload": payload, "step": step, "risk": risk},
                    start_to_close_timeout=timedelta(minutes=1),
                )
                await workflow.wait_condition(lambda step_id=step["id"]: step_id in self.approvals)
                approval = self.approvals[step["id"]]
                trace.append({"event": "approval_decision", "step_id": step["id"], "approval": approval.__dict__})
                if not approval.approved:
                    failed_receipt = await workflow.execute_activity(
                        "generate_receipt",
                        {
                            "status": "failed",
                            "reason": "Human denied approval",
                            "payload": payload,
                            "plan": plan,
                            "trace": trace,
                        },
                        start_to_close_timeout=timedelta(minutes=2),
                    )
                    return {"status": "failed", "receipt": failed_receipt, "trace": trace}

            result = await workflow.execute_activity(
                "execute_mcp_tool",
                {"payload": payload, "step": step, "risk": risk},
                start_to_close_timeout=timedelta(minutes=10),
            )
            outputs.append(result)
            trace.append({"event": "tool_result", "step_id": step["id"], "result": result})

        verification = await workflow.execute_activity(
            "verify_result",
            {"payload": payload, "plan": plan, "outputs": outputs, "trace": trace},
            start_to_close_timeout=timedelta(minutes=5),
        )
        trace.append({"event": "verification", "result": verification})

        receipt = await workflow.execute_activity(
            "generate_receipt",
            {
                "status": "succeeded" if verification.get("ok") else "failed",
                "payload": payload,
                "plan": plan,
                "outputs": outputs,
                "verification": verification,
                "trace": trace,
            },
            start_to_close_timeout=timedelta(minutes=2),
        )

        return {
            "status": "succeeded" if verification.get("ok") else "failed",
            "verification": verification,
            "receipt": receipt,
            "trace": trace,
        }


@workflow.defn
class CapabilityLifecycleWorkflow:
    def __init__(self) -> None:
        self.state: CapabilityState = CapabilityState.DISCOVERED
        self.approval: Optional[HumanApprovalSignal] = None

    @workflow.signal
    async def human_approval(self, signal: HumanApprovalSignal) -> None:
        self.approval = signal

    @workflow.query
    def current_state(self) -> str:
        return self.state.value

    @workflow.run
    async def run(self, submission: dict[str, Any]) -> dict[str, Any]:
        self.state = CapabilityState.INSPECTING
        inspection = await workflow.execute_activity(
            "inspect_capability_source",
            submission,
            start_to_close_timeout=timedelta(minutes=5),
        )
        if not inspection.get("source_reachable"):
            self.state = CapabilityState.REJECTED
            return await workflow.execute_activity(
                "generate_upgrade_rejection_receipt",
                {"submission": submission, "reason": "Source unreachable"},
                start_to_close_timeout=timedelta(minutes=2),
            )

        self.state = CapabilityState.CLASSIFIED
        classification = await workflow.execute_activity(
            "classify_capability",
            {"submission": submission, "inspection": inspection},
            start_to_close_timeout=timedelta(minutes=5),
        )

        if classification.get("requires_human_review"):
            self.state = CapabilityState.NEEDS_HUMAN_REVIEW
            await workflow.wait_condition(lambda: self.approval is not None)
            if not self.approval or not self.approval.approved:
                self.state = CapabilityState.REJECTED
                return await workflow.execute_activity(
                    "generate_upgrade_rejection_receipt",
                    {"submission": submission, "reason": "Human review denied"},
                    start_to_close_timeout=timedelta(minutes=2),
                )

        self.state = CapabilityState.CONTRACTIFYING
        adapter_contract = await workflow.execute_activity(
            "contractify_capability",
            {"submission": submission, "classification": classification},
            start_to_close_timeout=timedelta(minutes=5),
        )

        self.state = CapabilityState.SANDBOX_PENDING
        self.state = CapabilityState.SANDBOX_TESTING
        sandbox_result = await workflow.execute_child_workflow(
            SandboxedUpgradeTestingWorkflow.run,
            adapter_contract,
        )

        if not sandbox_result.get("passed"):
            self.state = CapabilityState.SANDBOX_FAILED
            return sandbox_result

        self.state = CapabilityState.SANDBOX_PASSED
        self.state = CapabilityState.AWAITING_APPROVAL
        await workflow.wait_condition(lambda: self.approval is not None)

        if not self.approval or not self.approval.approved:
            self.state = CapabilityState.REJECTED
            return await workflow.execute_activity(
                "generate_upgrade_rejection_receipt",
                {"submission": submission, "reason": "Promotion denied"},
                start_to_close_timeout=timedelta(minutes=2),
            )

        self.state = CapabilityState.APPROVED_FOR_PROMOTION
        promotion_result = await workflow.execute_child_workflow(
            GovernedPromotionWorkflow.run,
            {
                "adapter_contract": adapter_contract,
                "sandbox_result": sandbox_result,
                "approval": self.approval.__dict__,
            },
        )

        self.state = CapabilityState.ACTIVE_GOVERNED if promotion_result.get("status") == "ACTIVE_GOVERNED" else CapabilityState.REGISTERED_DISABLED
        return promotion_result


@workflow.defn
class SandboxedUpgradeTestingWorkflow:
    @workflow.run
    async def run(self, adapter_contract: dict[str, Any]) -> dict[str, Any]:
        test_trace: list[dict[str, Any]] = []

        sandbox = await workflow.execute_activity(
            "deploy_capability_to_sandbox",
            adapter_contract,
            start_to_close_timeout=timedelta(minutes=10),
        )
        test_trace.append({"step": "deploy_to_sandbox", "result": sandbox})
        if not sandbox.get("ok"):
            receipt = await workflow.execute_activity(
                "generate_upgrade_test_receipt",
                {"adapter_contract": adapter_contract, "status": "failed", "reason": "sandbox_deploy_failed", "trace": test_trace},
                start_to_close_timeout=timedelta(minutes=2),
            )
            return {"passed": False, "receipt": receipt, "trace": test_trace}

        verification = await workflow.execute_activity(
            "run_capability_verification_suite",
            {"adapter_contract": adapter_contract, "sandbox_id": sandbox["sandbox_id"]},
            start_to_close_timeout=timedelta(minutes=20),
        )
        test_trace.append({"step": "run_verification_suite", "result": verification})

        license_result = await workflow.execute_activity(
            "check_license_compliance",
            adapter_contract,
            start_to_close_timeout=timedelta(minutes=5),
        )
        test_trace.append({"step": "check_license_compliance", "result": license_result})

        risk_result = await workflow.execute_activity(
            "check_upgrade_risk_policy",
            {"adapter_contract": adapter_contract, "verification": verification, "license_result": license_result},
            start_to_close_timeout=timedelta(minutes=5),
        )
        test_trace.append({"step": "check_risk_policy", "result": risk_result})

        rollback_check = await workflow.execute_activity(
            "verify_rollback_path",
            adapter_contract,
            start_to_close_timeout=timedelta(minutes=5),
        )
        test_trace.append({"step": "verify_rollback_path", "result": rollback_check})

        sandbox_cleanup = await workflow.execute_activity(
            "destroy_upgrade_sandbox",
            {"sandbox_id": sandbox["sandbox_id"]},
            start_to_close_timeout=timedelta(minutes=5),
        )
        test_trace.append({"step": "destroy_sandbox", "result": sandbox_cleanup})

        passed = bool(
            verification.get("passed")
            and license_result.get("allowed_for_promotion")
            and risk_result.get("allowed")
            and rollback_check.get("ok")
            and sandbox_cleanup.get("ok")
        )

        receipt = await workflow.execute_activity(
            "generate_upgrade_test_receipt",
            {
                "adapter_contract": adapter_contract,
                "status": "passed" if passed else "failed",
                "trace": test_trace,
                "verification": verification,
                "license_result": license_result,
                "risk_result": risk_result,
                "rollback_check": rollback_check,
                "sandbox_cleanup": sandbox_cleanup,
            },
            start_to_close_timeout=timedelta(minutes=2),
        )
        return {"passed": passed, "receipt": receipt, "trace": test_trace}


@workflow.defn
class GovernedPromotionWorkflow:
    def __init__(self) -> None:
        self.approval: Optional[PromotionApprovalSignal] = None

    @workflow.signal
    async def promotion_approval(self, signal: PromotionApprovalSignal) -> None:
        self.approval = signal

    @workflow.query
    def approval_status(self) -> dict[str, Any]:
        return {"waiting": self.approval is None, "approved": self.approval.approved if self.approval else None}

    @workflow.run
    async def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        adapter_contract = payload["adapter_contract"]
        sandbox_result = payload["sandbox_result"]

        if not sandbox_result.get("passed"):
            return {"status": "REJECTED", "reason": "Sandbox result did not pass"}

        await workflow.execute_activity(
            "create_cockpit_promotion_request",
            {"adapter_contract": adapter_contract, "sandbox_result": sandbox_result},
            start_to_close_timeout=timedelta(minutes=2),
        )

        await workflow.wait_condition(lambda: self.approval is not None)
        if not self.approval or not self.approval.approved:
            receipt = await workflow.execute_activity(
                "generate_upgrade_promotion_receipt",
                {"status": "rejected", "adapter_contract": adapter_contract, "sandbox_result": sandbox_result, "approval": self.approval.__dict__ if self.approval else None},
                start_to_close_timeout=timedelta(minutes=2),
            )
            return {"status": "REJECTED", "receipt": receipt}

        policy_result = await workflow.execute_activity(
            "final_promotion_policy_check",
            {"adapter_contract": adapter_contract, "approval": self.approval.__dict__},
            start_to_close_timeout=timedelta(minutes=5),
        )
        if not policy_result.get("allowed"):
            receipt = await workflow.execute_activity(
                "generate_upgrade_promotion_receipt",
                {"status": "blocked", "adapter_contract": adapter_contract, "sandbox_result": sandbox_result, "approval": self.approval.__dict__, "policy_result": policy_result},
                start_to_close_timeout=timedelta(minutes=2),
            )
            return {"status": "BLOCKED_BY_POLICY", "receipt": receipt}

        previous_state = await workflow.execute_activity(
            "snapshot_capability_registry_state",
            {},
            start_to_close_timeout=timedelta(minutes=2),
        )
        registry_update = await workflow.execute_activity(
            "register_capability_disabled",
            {"adapter_contract": adapter_contract, "approval": self.approval.__dict__, "previous_state_hash": previous_state["state_hash"]},
            start_to_close_timeout=timedelta(minutes=5),
        )
        health_activation = await workflow.execute_activity(
            "activate_capability_health_check",
            {"adapter_id": registry_update["adapter_id"], "mode": "monitor"},
            start_to_close_timeout=timedelta(minutes=5),
        )
        receipt = await workflow.execute_activity(
            "generate_upgrade_promotion_receipt",
            {"status": "promoted", "adapter_contract": adapter_contract, "sandbox_result": sandbox_result, "approval": self.approval.__dict__, "policy_result": policy_result, "previous_state": previous_state, "registry_update": registry_update, "health_activation": health_activation},
            start_to_close_timeout=timedelta(minutes=2),
        )
        cortex_write = await workflow.execute_activity(
            "write_upgrade_memory_to_cortex",
            {"receipt_id": receipt["id"], "adapter_id": registry_update["adapter_id"], "capability_name": adapter_contract["name"], "status": "REGISTERED_DISABLED"},
            start_to_close_timeout=timedelta(minutes=2),
        )
        return {"status": "REGISTERED_DISABLED", "adapter_id": registry_update["adapter_id"], "receipt": receipt, "cortex_write": cortex_write}


@workflow.defn
class CapabilityRollbackWorkflow:
    @workflow.run
    async def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        adapter_id = payload["adapter_id"]
        trigger = payload["trigger"]
        requested_by = payload["requested_by"]

        current_state = await workflow.execute_activity(
            "snapshot_capability_registry_state",
            {},
            start_to_close_timeout=timedelta(minutes=2),
        )
        adapter_entry = await workflow.execute_activity(
            "get_capability_registry_entry",
            {"adapter_id": adapter_id},
            start_to_close_timeout=timedelta(minutes=2),
        )
        disable_result = await workflow.execute_activity(
            "disable_capability_adapter",
            {"adapter_id": adapter_id, "reason": trigger},
            start_to_close_timeout=timedelta(minutes=5),
        )
        restore_result = await workflow.execute_activity(
            "restore_previous_registry_state",
            {"adapter_id": adapter_id, "previous_state_hash": adapter_entry["previous_state_hash"]},
            start_to_close_timeout=timedelta(minutes=5),
        )
        health_result = await workflow.execute_activity(
            "run_post_rollback_health_check",
            {"adapter_id": adapter_id},
            start_to_close_timeout=timedelta(minutes=5),
        )

        rollback_ok = bool(disable_result.get("ok") and restore_result.get("ok") and health_result.get("ok"))
        receipt = await workflow.execute_activity(
            "generate_upgrade_rollback_receipt",
            {"adapter_id": adapter_id, "trigger": trigger, "requested_by": requested_by, "adapter_entry": adapter_entry, "current_state": current_state, "disable_result": disable_result, "restore_result": restore_result, "health_result": health_result, "rollback_ok": rollback_ok},
            start_to_close_timeout=timedelta(minutes=2),
        )
        cortex_write = await workflow.execute_activity(
            "write_rollback_memory_to_cortex",
            {"adapter_id": adapter_id, "receipt_id": receipt["id"], "status": "ROLLED_BACK" if rollback_ok else "ROLLBACK_FAILED", "trigger": trigger},
            start_to_close_timeout=timedelta(minutes=2),
        )
        if not rollback_ok:
            await workflow.execute_activity(
                "escalate_rollback_failure",
                {"adapter_id": adapter_id, "receipt_id": receipt["id"], "trigger": trigger},
                start_to_close_timeout=timedelta(minutes=2),
            )
        return {"status": "ROLLED_BACK" if rollback_ok else "ROLLBACK_FAILED", "adapter_id": adapter_id, "receipt": receipt, "cortex_write": cortex_write}
