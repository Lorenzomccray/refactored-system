# EXECUTION_RECEIPTS
## Audit Records for Every Meaningful Action

---

## 1. Purpose

Execution receipts are the minimum replayable, auditable unit of system truth.

A receipt proves:
- what was attempted
- by whom or by what subsystem
- under which authorization state
- with which inputs and outputs
- what artifacts were produced
- what verification was performed
- how the action ended

If an action has no receipt, it should not be treated as trustworthy.

---

## 2. Receipt Requirements

Every meaningful step must emit a receipt.

This includes:
- plan creation
- approval requests
- approval decisions
- tool invocations
- provider calls where relevant
- verifier outcomes
- retries
- fallback transitions
- failure exits

---

## 3. Canonical Receipt Fields

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

### Field meanings

- `id`: unique receipt id
- `run_id`: top-level run correlation id
- `task_id`: originating task
- `plan_id`: optional reference to the active plan
- `step_id`: optional reference to a step in the execution graph
- `actor`: planner, builder, verifier, recovery, policy engine, tool wrapper, etc.
- `operation`: the action performed
- `status`: started/completed/failed/blocked
- `inputs_ref`: reference to stored normalized inputs
- `outputs_ref`: reference to stored outputs
- `artifacts`: produced or touched artifacts
- `approval_ref`: approval decision link if relevant
- `verification_ref`: verification result link if relevant
- `failure_ref`: failure record link if relevant

---

## 4. Receipt Classes

### 4.1 Planning Receipt
Emitted when a plan or execution graph is produced.

Should include:
- planner model/provider
- plan id
- assumptions summary
- risk summary
- approval checkpoints identified

### 4.2 Authorization Receipt
Emitted when the policy plane classifies and authorizes or blocks a step.

Should include:
- risk class
- approval required yes/no
- sandbox required yes/no
- allowed/block decision
- escalation yes/no

### 4.3 Tool Execution Receipt
Emitted when a tool is invoked.

Should include:
- tool name
- capability used
- timeout
- status
- output refs
- artifact refs
- whether sandbox was active

### 4.4 Verification Receipt
Emitted when a verifier step runs.

Should include:
- syntactic result
- semantic result
- environment result
- evidence refs
- recommended next action

### 4.5 Failure Receipt
Emitted when a step or run fails.

Should include:
- failure class
- summary
- recoverable yes/no
- suggested recovery path

---

## 5. Receipt Generation Rules

1. A receipt must be created before an action is considered complete.
2. A receipt may reference heavy payloads by pointer instead of embedding them.
3. Receipt generation must not silently fail.
4. If receipt generation fails, the enclosing step must be treated as failed or incomplete.
5. Receipts must be immutable once finalized.

---

## 6. Storage Rules

Receipts should be stored in a replayable, queryable store.

They should support lookup by:
- run id
- task id
- step id
- status
- actor
- operation
- date range

Recommended backing:
- structured DB table for index/query
- artifact store for heavy payload refs

---

## 7. Verification Binding

Every state-changing or high-risk action must bind to:
- an authorization receipt
- an execution receipt
- a verification receipt

This is especially mandatory for:
- file writes
- shell execution
- browser automation
- external API calls
- database mutation

---

## 8. Minimum Receipt Payload for V1

For early implementation, the minimum valid receipt is:

```yaml
id: string
run_id: string
actor: string
operation: string
status: string
timestamp: datetime
summary: string
```

Then progressively expand it to the full contract.

---

## 9. Immediate Build Priority

Implement first:
- receipt schema
- receipt writer
- receipt store
- receipt references from tool and verifier paths

Then:
- replay view
- failure-linked receipts
- approval-linked receipts
- artifact-linked receipts

Without receipts, observability is just storytelling.
