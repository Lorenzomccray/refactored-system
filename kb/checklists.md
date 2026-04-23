# /kb/checklists

## Purpose
Provide reusable checklists for refactors, reviews, releases, verification, and runtime-truth updates.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical workflow, safety, and validation docs remain stronger for exact requirements.

## When to use this page
Use this page when preparing or reviewing a bounded change and you need a compact execution checklist.

## Content
### Refactor checklist
- confirm the target boundary
- confirm the smallest safe slice
- identify affected contracts and safety impact
- preserve or improve receipts and verification
- update canonical docs if doctrine changed
- update runtime truth if actual state changed

### Review checklist
- grounded in canonical docs
- boundaries preserved
- typed contracts used where needed
- risky actions classified and gated
- verification expectations explicit
- open questions surfaced

### Release checklist
- scope confirmed
- compatibility confirmed
- validation and smoke coverage checked
- runtime truth current enough to describe reality
- artifact and receipt trail present

### Runtime truth update checklist
- repo structure changed?
- tools, providers, or workflows changed?
- gaps or blockers changed?
- assumptions replaced by observed state?

## Related pages
- `kb/workflows.md`
- `kb/validation.md`
- `kb/safety.md`
- `kb/repo-rules.md`
- `kb/precedents.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 14 days

## Conflict notes
This page does not override canonical workflow, safety, or validation docs.
