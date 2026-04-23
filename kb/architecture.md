# /kb/architecture

## Purpose
Describe the canonical system structure, boundaries, and execution shape of the backend brain.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical repo docs remain stronger for exact system meaning, and runtime truth remains stronger for what is present now.

## When to use this page
Use this page when you need to know:
- the major planes of the system
- what belongs inside or outside the brain
- the canonical execution lifecycle
- which boundaries must be preserved during design and implementation

## Content
### Core system shape
The backend brain is organized into planes:
- Control
- Cognition
- Memory
- Tool
- Provider
- Policy
- Verification
- Observability
- Integration

### Core boundary rules
- No plane should pass opaque strings when a typed contract exists.
- Planner does not execute tools directly.
- Builder does not self-authorize risky work.
- Tools are invoked through wrappers and policy.
- Provider routing belongs in the provider plane.
- Verification keeps syntactic, semantic, and environment checks distinct.
- External systems remain adapters; the brain must not depend on any single adapter.

### Canonical execution lifecycle
`INTAKE → CONTEXT_LOAD → PLAN → AUTHORIZE → EXECUTE → OBSERVE → VERIFY → RETRY_OR_REPLAN → PERSIST → RESPOND → FAIL_CLOSED`

### Architectural intent
The brain should coordinate task understanding, context loading, planning, authorization, execution, verification, and persistence without absorbing every external capability into a monolith.

## Related pages
- `kb/principles.md`
- `kb/schemas.md`
- `kb/workflows.md`
- `kb/validation.md`
- `kb/safety.md`
- `kb/adr.md`
- `docs/MASTER_AI_SYSTEM_V2.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override:
- canonical architecture docs for exact module or interface meaning
- runtime truth for what is currently implemented or missing
