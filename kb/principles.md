# /kb/principles

## Purpose
Define the project’s operating philosophy, reasoning posture, and non-goals.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical repo docs remain stronger for system meaning, and runtime truth remains stronger for current-state questions.

## When to use this page
Use this page when you need the project’s default stance on:
- planning before implementation
- how uncertainty should be handled
- what counts as safe execution behavior
- what should not be treated as project truth

## Content
### Core principles
- Correctness over fluency
- Verification over assumption
- Small working slices over vague autonomy
- Typed contracts over opaque string handoffs
- Read-only inspection before state-changing action
- Approval before risky execution
- Adapters over hard dependencies
- Logs, receipts, and traces over invisible behavior
- Fail closed rather than improvising unsafe execution

### Working rules
- Prefer the smallest relevant context set.
- Prefer canonical docs over memory and memory over speculation.
- Mark unknowns explicitly.
- Separate facts, inferences, assumptions, and open questions in substantive work.
- Plan before changing.
- Execute through governed wrappers, not ad hoc direct action paths.
- Verify against reality before claiming completion.
- Persist only what is reusable, auditable, or required for recovery.

### Non-goals
- turning the brain into a monolith of all external capabilities
- treating external frameworks as the core system
- using raw dumps or transcripts as durable project truth
- blurring planner, builder, verifier, and policy roles
- declaring success without artifacts, receipts, or verification

## Related pages
- `kb/repo-rules.md`
- `kb/architecture.md`
- `kb/schemas.md`
- `kb/validation.md`
- `kb/safety.md`
- `docs/MASTER_AI_SYSTEM_V2.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override:
- runtime truth for current-state questions
- canonical architecture, schema, risk, memory, or receipt docs for exact system meaning
