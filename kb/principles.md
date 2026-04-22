# /kb/principles

## Purpose

This page defines the operating philosophy, reasoning rules, priorities, and non-goals for the `refactored-system` project.

## Scope

This page governs:
- how work is planned
- how uncertainty is represented
- how execution is authorized
- how verification and memory are treated
- what the system is intentionally **not**

## Facts from current project doctrine

### Architecture and execution posture
- The AI Brain is the central execution and orchestration core.
- It should do six things only: understand the task, load context, build a plan, authorize the next step, execute and verify, and persist what matters.
- Everything else is attached through adapters, providers, tools, and services.
- The brain orchestrates; it does not absorb every integration into a monolith.

### Core principles
- Correctness over fluency
- Verification over assumption
- Small working build slices over broad vague autonomy
- Typed contracts over stringly-typed handoffs
- Read-only inspection before state-changing action
- Approval before risky execution
- Modular subsystems over giant prompt logic
- Adapters over hard dependencies
- Logs, receipts, and traces over invisible behavior
- Fail closed rather than improvising unsafe execution

### Source and truth hierarchy
- Canonical internal architecture docs come before runtime truth docs, build-slice docs, reference lessons docs, and external public registries.
- Architecture docs override reference notes.
- Runtime docs override assumptions.
- Raw repo dumps are not canonical truth.
- Temporary workflow transcripts must be converted into docs or archived.

### Memory posture
- Memory must be selective, typed, and promotion-driven.
- Working memory must not store unbounded conversation history.
- Semantic memory must not store raw chat transcripts.
- Procedural memory is not written on first success.

### Receipts and verification
- If an action has no receipt, it should not be treated as trustworthy.
- Every meaningful action should emit a receipt.
- Verification must distinguish syntactic, semantic, and environment checks.

## Canonical rules

### Reasoning rules
1. Prefer the smallest relevant context set over broad retrieval.
2. Prefer canonical docs over memory and memory over speculation.
3. Mark unknowns explicitly instead of inventing values.
4. Separate facts, inferences, assumptions, and open questions in substantive work.
5. If policy, schema, or runtime truth is unclear, stop at the narrowest safe claim.

### Planning rules
1. Plan before changing.
2. Build the smallest working slice that makes the architecture more real.
3. Use typed contracts and module boundaries as the primary design language.
4. Prefer explicit state machines, receipts, and verification hooks over agent folklore.

### Execution rules
1. Read before write.
2. Classify before authorize.
3. Authorize before execute.
4. Execute through wrappers, not direct ad hoc action paths.
5. Verify against reality before claiming completion.
6. Persist only what is reusable, auditable, or required for recovery.

### Non-goals
- Turning the brain into a monolith of all external capabilities
- Treating external frameworks as the core system
- Using raw transcripts or dumps as durable project truth
- Blurring planner, builder, verifier, and policy roles
- Declaring success without artifacts, receipts, or verification

## Boundaries

### This page does decide
- default decision posture
- truth hierarchy
- planning and execution philosophy
- memory and verification posture

### This page does not decide
- exact schema field definitions
- exact risk class matrix
- exact workflow steps for each change type
- exact repo file layout beyond principles-level guidance

See:
- `/kb/schemas`
- `/kb/safety`
- `/kb/workflows`
- `/kb/architecture`

## Cross-references
- `/kb/repo-rules`
- `/kb/architecture`
- `/kb/schemas`
- `/kb/validation`
- `/kb/safety`

## Assumptions
- The repo will continue using the backend-brain blueprint as the canonical architecture source.
- The project still prefers docs-first slices before large code merges.
- Runtime truth documents will be maintained once implementation proceeds.

## Open questions
- Which principles should be enforced automatically at runtime vs only documented?
- Which parts of the source hierarchy should be surfaced in tooling or CI?
- Should there be a formal “decision record required” threshold for certain work classes?
