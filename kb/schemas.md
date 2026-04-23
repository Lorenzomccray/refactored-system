# /kb/schemas

## Purpose
Describe the project’s canonical typed contracts, validation expectations, and versioning posture.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical schema docs remain stronger for exact contract meaning, and runtime truth remains stronger for what is currently implemented.

## When to use this page
Use this page when you need to know:
- which cross-plane contracts matter most
- why typed contracts outrank opaque strings
- what versioning and validation rules apply
- what minimum contract set should be implemented first

## Content
### Core contract set
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

### Core schema rules
- contracts must be serializable
- contracts must have stable identifiers and versions
- contracts must validate before crossing plane boundaries
- invalid contracts fail closed
- semantic validation should not proceed when syntactic validation already failed
- state-changing operations should bind to receipt-bearing contracts

### Immediate implementation priority
Start with the smallest doctrine-backed set:
- Task
- Plan
- ExecutionStep
- ToolResult
- ApprovalDecision
- VerificationResult
- MemoryRecord
- RunReceipt

## Related pages
- `kb/architecture.md`
- `kb/validation.md`
- `kb/safety.md`
- `kb/adr.md`
- `docs/SCHEMA_CONTRACTS.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override:
- canonical schema docs for exact fields, versions, or migration rules
- runtime truth for what contracts are already implemented in code
