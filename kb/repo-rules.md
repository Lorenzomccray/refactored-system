# /kb/repo-rules

## Purpose
Define repository-specific constraints, allowed change types, and merge-readiness expectations.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical repo docs remain stronger for doctrine, and runtime truth remains stronger for current-state questions.

## When to use this page
Use this page when you need to know:
- what kinds of changes fit the repo
- what changes are out of bounds
- what a bounded, doctrine-aligned change looks like
- what minimum merge-readiness signals should be present

## Content
### Preferred change types
- canonical documentation improvements
- runtime truth updates reflecting actual state
- small implementation slices aligned to the canonical architecture
- contract-first changes
- validation, receipt, approval, and risk-classification improvements
- adapter work that preserves brain-to-adapter boundaries

### Out-of-bounds or discouraged changes
- broad donor merges without adaptation
- code that bypasses documented planes and typed contracts
- large raw prompt or transcript dumps committed as project truth
- integrations that make the core depend on one external framework or service
- behavior that cannot be replayed, audited, or verified

### Merge-readiness doctrine
A change should align with:
- relevant canonical docs
- plane boundaries
- contract updates when interfaces change
- stated validation impact
- stated receipt or audit impact for meaningful execution changes
- surfaced assumptions and open questions

## Related pages
- `kb/principles.md`
- `kb/architecture.md`
- `kb/schemas.md`
- `kb/validation.md`
- `kb/safety.md`
- `kb/checklists.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override:
- canonical architecture, schema, risk, or safety docs
- runtime truth about what is actually present in the repo now
