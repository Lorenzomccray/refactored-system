# SCHEMA_CONTRACTS
## Canonical Cross-Plane Contracts
### For `refactored-system`

---

## 1. Purpose

This document defines the canonical typed contracts used between the major planes of the system.

These contracts exist to prevent:
- stringly-typed handoffs
- hidden coupling
- planner/builder/verifier drift
- tool-result ambiguity
- unverifiable execution
- memory pollution
- replay/debug chaos

If a typed contract exists, no plane should pass opaque freeform strings instead.

---

## 2. Design Rules

1. Every contract must be serializable.
2. Every contract must have a stable identifier.
3. Every contract must support validation before use.
4. Every contract must be versionable.
5. Every state-changing operation must emit a receipt-bearing contract.
6. Planner, builder, verifier, policy, memory, and telemetry must communicate through contracts, not ad hoc strings.
7. When a field is unknown, mark it explicitly rather than inventing a value.
8. Contracts should be minimal but sufficient for orchestration, verification, and replay.

---

## 3. Contract Inventory

### Required contracts

```text
Task
Plan
ExecutionGraph
ExecutionStep
ToolCall
ToolResult
ApprovalRequest
ApprovalDecision
VerificationResult
MemoryRecord
RunReceipt
FailureRecord
```

---

## 4. Task Contract

Represents a normalized incoming operator or system request.

### Required fields

```yaml
id: string
version: string
created_at: datetime
source: enum[user, system, schedule, recovery]
goal: string
constraints: list[string]
context_refs: list[string]
priority: enum[low, normal, high, critical]
requested_capabilities: list[string]
risk_hint: optional[string]
```

### Notes
- `goal` is the user/system objective in normalized form.
- `context_refs` are references to docs, artifacts, or memory items, not raw blobs.
- `risk_hint` is advisory only; the policy plane classifies the actual risk.

---

## 5. Plan Contract

Represents the planner's proposed decomposition of a task.

### Required fields

```yaml
id: string
version: string
task_id: string
created_at: datetime
planner_model: string
objective: string
assumptions: list[string]
unknowns: list[string]
success_criteria: list[string]
risk_summary: list[string]
requires_human_review_now: boolean
proposed_steps: list[ExecutionStepRef]
```

### Notes
- `requires_human_review_now` is about the current workflow branch, not future execution generally.
- `proposed_steps` references execution steps by ID or embedded lightweight descriptors.

---

## 6. ExecutionGraph Contract

Represents the executable step graph derived from the plan.

### Required fields

```yaml
id: string
version: string
plan_id: string
created_at: datetime
nodes: list[ExecutionStep]
edges: list[ExecutionEdge]
approval_checkpoints: list[string]
required_tools: list[string]
required_providers: list[string]
global_success_criteria: list[string]
```

### ExecutionEdge

```yaml
from_step_id: string
to_step_id: string
condition: optional[string]
```

### Notes
- The execution graph is a first-class artifact, not an implicit loop.
- `approval_checkpoints` identifies steps that must be authorized before proceeding.

---

## 7. ExecutionStep Contract

Represents one executable or evaluable step.

### Required fields

```yaml
id: string
version: string
graph_id: string
kind: enum[read, write, execute, verify, retrieve, summarize, classify, approve]
description: string
risk_class: enum[
  READ_ONLY,
  LOCAL_WRITE,
  LOCAL_EXECUTION,
  EXTERNAL_API_CALL,
  DATABASE_MUTATION,
  BROWSER_AUTOMATION,
  CREDENTIAL_USE,
  IRREVERSIBLE
]
tool_name: optional[string]
provider_role: optional[enum[planner, builder, verifier, researcher, memory, recovery]]
inputs_ref: optional[string]
expected_outputs: list[string]
success_criteria: list[string]
requires_approval: boolean
sandbox_required: boolean
timeout_seconds: integer
retry_policy_ref: optional[string]
verification_mode: list[enum[syntactic, semantic, environment]]
```

### Notes
- Every step must be independently classifiable and verifiable.
- `requires_approval` is policy-bound, not agent-decided in isolation.

---

## 8. ToolCall Contract

Represents a normalized request to invoke a tool.

### Required fields

```yaml
id: string
version: string
step_id: string
tool_name: string
capability: string
risk_class: string
input_schema_version: string
input_payload: object
requested_by_agent: string
authorized: boolean
authorization_ref: optional[string]
created_at: datetime
```

### Notes
- A ToolCall is intent to execute, not evidence that execution occurred.

---

## 9. ToolResult Contract

Represents the actual output of a tool execution.

### Required fields

```yaml
id: string
version: string
tool_call_id: string
tool_name: string
status: enum[success, failure, timeout, blocked]
started_at: datetime
finished_at: datetime
output_payload: object
artifacts: list[string]
stdout_summary: optional[string]
stderr_summary: optional[string]
verification_hints: list[string]
receipt_id: string
```

### Notes
- `output_payload` must conform to the tool's declared output schema.
- `receipt_id` links to the canonical execution receipt.

---

## 10. ApprovalRequest Contract

Represents a request for human or policy-mediated review.

### Required fields

```yaml
id: string
version: string
step_id: string
reason: string
risk_class: string
requested_action_summary: string
artifacts_for_review: list[string]
requested_at: datetime
requested_by: string
```

---

## 11. ApprovalDecision Contract

Represents the outcome of the approval gate.

### Required fields

```yaml
id: string
version: string
approval_request_id: string
decision: enum[approved, denied, deferred]
decided_at: datetime
decided_by: string
justification: optional[string]
constraints_added: list[string]
```

### Notes
- Approval decisions may modify downstream constraints.
- Denial is a first-class result, not an exception.

---

## 12. VerificationResult Contract

Represents the verifier's judgment.

### Required fields

```yaml
id: string
version: string
step_id: string
verified_at: datetime
syntactic_status: enum[pass, fail, not_run]
semantic_status: enum[pass, fail, uncertain, not_run]
environment_status: enum[pass, fail, unknown, not_run]
summary: string
failures: list[string]
evidence_refs: list[string]
recommended_next_action: enum[continue, retry, replan, fail_closed, request_human_review]
```

### Notes
- Syntactic, semantic, and environment checks are separate dimensions.
- `uncertain` is valid and preferable to false certainty.

---

## 13. MemoryRecord Contract

Represents a unit written into memory.

### Required fields

```yaml
id: string
version: string
memory_layer: enum[working, episodic, semantic, procedural]
source_run_id: string
source_step_id: optional[string]
title: string
summary: string
content_ref: optional[string]
tags: list[string]
created_at: datetime
promotion_state: enum[direct, candidate, promoted]
retention_policy: string
```

### Notes
- Semantic and procedural memory should rarely store raw unfiltered content.
- `promotion_state` supports later promotion logic.

---

## 14. RunReceipt Contract

Represents the replayable audit record for a run or step.

### Required fields

```yaml
id: string
version: string
run_id: string
task_id: string
plan_id: optional[string]
step_id: optional[string]
actor: string
operation: string
status: enum[started, completed, failed, blocked]
timestamp: datetime
inputs_ref: optional[string]
outputs_ref: optional[string]
artifacts: list[string]
approval_ref: optional[string]
verification_ref: optional[string]
failure_ref: optional[string]
```

### Notes
- Every meaningful state transition should emit a receipt.
- Receipts are the minimum unit for replay and audit.

---

## 15. FailureRecord Contract

Represents failure classification and recovery context.

### Required fields

```yaml
id: string
version: string
run_id: string
step_id: optional[string]
failure_class: enum[
  MODEL_FAILURE,
  TOOL_FAILURE,
  POLICY_DENIAL,
  VERIFICATION_FAILURE,
  TIMEOUT,
  SCHEMA_FAILURE,
  MEMORY_FAILURE,
  UNKNOWN
]
summary: string
details_ref: optional[string]
recoverable: boolean
suggested_recovery: enum[retry, fallback, replan, human_review, fail_closed]
created_at: datetime
```

---

## 16. Contract Versioning Rules

1. Every contract includes a `version`.
2. Breaking schema changes require a version increment.
3. Parsers must reject incompatible versions by default.
4. Contracts should prefer additive changes where possible.
5. Tool and provider adapters must declare which versions they support.

---

## 17. Validation Policy

- Contracts must be validated before crossing plane boundaries.
- Validation must fail closed.
- Invalid contracts must produce a `FailureRecord`.
- The verifier must not attempt semantic validation if syntactic validation already failed.

---

## 18. Immediate Build Priority

Implement first:

```text
Task
Plan
ExecutionStep
ToolResult
ApprovalDecision
VerificationResult
MemoryRecord
RunReceipt
```

That is the smallest contract set required to make the architecture real.
