# /kb/workflows

## Purpose

This page defines the standard workflows for planning, debugging, refactoring, release, and incident response in `refactored-system`.

## Scope

This page governs operational sequences. It does not replace architecture, schema, safety, or validation pages; it applies them.

## Facts from current project doctrine

### Canonical execution lifecycle
INTAKE → CONTEXT_LOAD → PLAN → AUTHORIZE → EXECUTE → OBSERVE → VERIFY → RETRY_OR_REPLAN → PERSIST → RESPOND → FAIL_CLOSED

### Source workflow rules
- Prefer canonical docs first.
- Runtime docs override assumptions.
- Build docs define the next coding target.
- Temporary transcripts should be converted to docs or archived.

### Memory workflow rules
- Working memory is short-lived.
- Episodic memory stores outcomes and approvals.
- Semantic memory stores validated reusable knowledge.
- Procedural memory requires repeated successful reuse before promotion.

## Standard workflows

### 1. Planning workflow
1. Read the smallest relevant canonical pages.
2. Check runtime truth docs if the task concerns current state.
3. Normalize the task objective and constraints.
4. Produce assumptions, unknowns, and success criteria.
5. Classify likely risk checkpoints.
6. Identify the smallest viable slice.
7. Link the plan to the canonical docs it depends on.

### 2. Debugging workflow
1. Reconstruct the failing path from receipts, logs, runtime docs, and artifacts.
2. Distinguish:
   - schema failure
   - policy denial
   - tool failure
   - verification failure
   - timeout
   - unknown
3. Verify whether the failure is reproducible.
4. Prefer minimal, targeted fixes over broad rewrites.
5. Record the failure as a precedent or lesson if reusable.
6. Update runtime truth if the current system state changed.

### 3. Refactoring workflow
1. Confirm the target boundary and why it matters.
2. Check architecture and schemas before editing.
3. Identify the smallest safe refactor slice.
4. Keep behavior, contract, and receipt impact explicit.
5. Preserve or improve verification and replayability.
6. Avoid donor-code merges without adaptation.
7. Update docs first or in lockstep when structure changes.

### 4. Release workflow
1. Confirm what changed and what did not.
2. Verify schema or contract compatibility.
3. Verify safety and approval paths for new risky behavior.
4. Run validation and smoke checks.
5. Ensure runtime truth docs are current enough to describe reality.
6. Generate execution receipts or release notes that support replay.

### 5. Incident response workflow
1. Fail closed where policy requires.
2. Preserve evidence first.
3. Classify the incident by failure or risk type.
4. Contain the blast radius.
5. Execute the smallest verified recovery path.
6. Record the incident outcome in episodic or precedent form.
7. Promote to procedural guidance only after repeated validated success.

## Workflow invariants
- Read before write.
- Classify before authorize.
- Authorize before execute.
- Verify before claim.
- Persist selectively, not indiscriminately.

## Boundaries

### This page does decide
- standard operational sequence
- how other KB pages are applied during work

### This page does not decide
- exact CI runner steps
- exact test commands
- exact deployment tooling
- exact branch or ticket workflow

## Cross-references
- `/kb/principles`
- `/kb/architecture`
- `/kb/checklists`
- `/kb/validation`
- `/kb/safety`
- `/kb/precedents`

## Assumptions
- The project wants reusable, repeatable workflows more than one-off heroics.
- Runtime docs will be kept current enough to inform planning and debugging.
- Receipts and artifacts will become primary debugging evidence once implemented.

## Open questions
- Which workflow steps should become automated gates?
- Should incident response get its own deeper playbook once runtime surfaces are live?
- Which refactor classes require ADRs vs checklist-only treatment?
