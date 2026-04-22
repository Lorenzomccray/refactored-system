# /kb/schemas

## Purpose

This page defines the canonical typed contracts, versioning rules, validation rules, and deprecation notes for `refactored-system`.

## Scope

This page governs cross-plane data contracts. If a typed contract exists, freeform opaque handoffs should not replace it.

## Facts from current project doctrine

### Design rules
- Every contract must be serializable.
- Every contract must have a stable identifier.
- Every contract must support validation before use.
- Every contract must be versionable.
- Every state-changing operation must emit a receipt-bearing contract.
- Planner, builder, verifier, policy, memory, and telemetry communicate through contracts, not ad hoc strings.
- When a field is unknown, mark it explicitly rather than inventing a value.
- Contracts should be minimal but sufficient for orchestration, verification, and replay.

### Required contract inventory
- Task
- Plan
- ExecutionGraph
- ExecutionStep
- ToolCall
- ToolResult
- ApprovalRequest
- ApprovalDecision
- VerificationResult
- MemoryRecord
- RunReceipt
- FailureRecord

## Canonical schema summary

### Task
Normalized incoming request:
- source
- goal
- constraints
- context refs
- priority
- requested capabilities
- optional risk hint

### Plan
Planner decomposition:
- assumptions
- unknowns
- success criteria
- risk summary
- human review flag
- proposed step references

### ExecutionGraph
Executable graph:
- nodes
- edges
- approval checkpoints
- required tools/providers
- global success criteria

### ExecutionStep
One executable or evaluable step:
- kind
- description
- risk class
- optional tool or provider role
- inputs ref
- expected outputs
- success criteria
- approval or sandbox flags
- timeout
- retry policy ref
- verification modes

### ToolCall
Normalized intent to invoke a tool:
- tool name
- capability
- risk class
- schema version
- payload
- agent
- authorization state

### ToolResult
Actual tool outcome:
- status
- output payload
- artifacts
- stdout or stderr summary
- verification hints
- receipt id

### ApprovalRequest / ApprovalDecision
Review gate:
- request reason and action summary
- decision outcome
- constraints added
- justification

### VerificationResult
Verifier judgment:
- syntactic status
- semantic status
- environment status
- failures
- evidence refs
- recommended next action

### MemoryRecord
Memory write unit:
- memory layer
- source run or step
- title
- summary
- content ref
- tags
- promotion state
- retention policy

### RunReceipt
Replayable audit record:
- actor
- operation
- status
- refs to inputs, outputs, artifacts, approval, verification, and failure

### FailureRecord
Failure classification:
- failure class
- summary
- recoverable flag
- suggested recovery

## Versioning rules
1. Every contract includes a version.
2. Breaking schema changes require a version increment.
3. Parsers reject incompatible versions by default.
4. Prefer additive change where possible.
5. Tool and provider adapters must declare supported versions.

## Validation rules
1. Contracts must be validated before crossing plane boundaries.
2. Validation fails closed.
3. Invalid contracts produce a FailureRecord.
4. Semantic validation should not proceed when syntactic validation already failed.

## Deprecation notes

### Current doctrine-backed deprecations
The following are considered architecturally deprecated even if present in current code:
- opaque string handoffs where a contract exists
- unverifiable tool outputs without receipt linkage
- implicit execution loops that do not materialize an execution graph
- success flags that collapse syntactic, semantic, and environment verification into one value

### Deprecation policy
A schema field or contract pattern should be considered deprecated when:
1. a canonical replacement exists
2. an ADR or schema revision names the replacement
3. adapters can reject or translate the old form safely

## Immediate implementation priority
Smallest doctrine-backed first set:
- Task
- Plan
- ExecutionStep
- ToolResult
- ApprovalDecision
- VerificationResult
- MemoryRecord
- RunReceipt

## Boundaries

### This page does decide
- canonical contract set
- schema design rules
- versioning and validation expectations

### This page does not decide
- exact Python class library
- exact serialization format beyond serializable structured contracts
- exact migration process for each implementation artifact

## Cross-references
- `/kb/architecture`
- `/kb/validation`
- `/kb/safety`
- `/kb/adr`

## Assumptions
- These contracts will eventually be implemented as code-level schemas rather than remain doc-only.
- The repo will use validation as a real gate, not just documentation.
- Version negotiation for adapters will matter once integrations expand.

## Open questions
- Which schema library should be canonical in implementation?
- Which contract versions should be stabilized first for V1?
- Should receipt references and artifact references be strongly typed URIs or project-local IDs?
