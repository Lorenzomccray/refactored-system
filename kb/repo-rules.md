# /kb/repo-rules

## Purpose

This page defines repository-specific constraints, allowed change types, forbidden patterns, and merge rules for `refactored-system`.

## Scope

This page governs:
- what kinds of changes are acceptable
- how documentation and runtime truth interact
- what should not be merged or treated as canonical
- when a change is ready to merge

## Facts from current project doctrine

### Source system rules
- One topic, one canonical file.
- Architecture docs override reference notes.
- Runtime docs override assumptions.
- Build docs define the next coding target.
- Raw repo dumps are not canonical truth.
- Temporary workflow transcripts must be converted into docs or archived.

### Architecture rules with repo impact
- The brain orchestrates and should not absorb every integration into a monolith.
- Adapters may depend on the brain; the brain must not depend on any single adapter.
- No plane should pass opaque strings when a typed contract exists.
- No agent may call a tool directly.
- Every tool invocation should flow through plan → authorization → execution wrapper → receipt → verification.

## Canonical change rules

### Allowed change types
1. Canonical documentation updates that sharpen architecture, schemas, policies, workflows, validation, or receipts.
2. Runtime truth doc updates that reflect actual current state.
3. Small implementation slices that bring the repo closer to the canonical architecture.
4. Contract-first changes that introduce or refine typed schemas before broad orchestration behavior.
5. Validation, receipt, approval, and risk-classification improvements.
6. Adapter work that preserves the brain/adapters boundary.

### Restricted change types
1. Broad merges from donor systems without adaptation.
2. Runtime code drops that bypass the documented planes and typed contracts.
3. Secret-bearing examples, credentials, or raw environment values committed as project truth.
4. Large prompt dumps, chat transcripts, or raw exported analyses committed as canonical docs.
5. Integrations that make the core depend on one external framework or service.
6. Magic behavior that cannot be replayed, audited, or verified.

### Merge rules
A change is merge-ready only when:
1. it cites or aligns with the relevant canonical docs
2. it does not violate plane boundaries
3. contracts are updated if interfaces changed
4. validation impact is stated
5. receipt or audit impact is stated for meaningful execution changes
6. assumptions and open questions are surfaced instead of hidden

## Forbidden patterns

### Architecture violations
- hidden control blobs
- direct tool calls from agents
- provider-specific logic embedded into the control plane
- browser automation embedded as core brain logic
- external framework lock-in inside the core

### Documentation violations
- multiple canonical files for the same topic
- reference notes overriding architecture docs
- runtime claims that contradict current runtime docs
- raw repo snapshots treated as final truth

### Safety and operational violations
- state-changing work without approval path
- unclassified risky execution
- unverifiable success claims
- writing secrets or sensitive credentials into memory or docs

## Boundaries

### This page does decide
- repository hygiene expectations
- acceptable and unacceptable change classes
- merge-readiness criteria at a doctrine level

### This page does not decide
- exact reviewer workflow
- exact branch naming
- exact CI commands
- exact changelog format

## Cross-references
- `/kb/principles`
- `/kb/architecture`
- `/kb/schemas`
- `/kb/validation`
- `/kb/safety`
- `/kb/checklists`

## Assumptions
- Merge rules here refer to doctrine and readiness, not to GitHub branch-protection settings.
- The project intends to remain doc-first and architecture-boundary-first.
- Runtime docs will become mandatory merge context as implementation matures.

## Open questions
- What is the exact minimum doc set required before code merges?
- Which changes require linked ADRs?
- Should the repo explicitly distinguish safe refactor, behavioral change, and runtime law change in PR labels?
