# /kb/validation

## Purpose
Define the project’s verification standards, validation layers, and minimum evidence needed for success claims.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical validation and receipt docs remain stronger for exact rules, and runtime truth remains stronger for what checks are active now.

## When to use this page
Use this page when you need to know:
- what must be validated before claiming success
- how syntactic, semantic, and environment checks differ
- what minimum checks apply to risky or state-changing work
- when rollback awareness matters

## Content
### Validation layers
- Schema validation before crossing plane boundaries
- Syntactic validation for structure, required fields, and artifact existence
- Semantic validation for whether the result matches the request and plan intent
- Environment validation for whether the claimed real-world state change actually happened

### Validation rules
- validation fails closed
- invalid contracts produce failure records
- semantic validation should not proceed when syntactic validation already failed
- state-changing and high-risk actions should bind to authorization, execution, and verification receipts

### Minimum expectations
- read-only work: schema plus targeted semantic checks as needed
- local write or execution: schema, syntactic, and environment checks
- database, browser, credential, or irreversible work: stronger evidence and rollback awareness where applicable

## Related pages
- `kb/schemas.md`
- `kb/safety.md`
- `kb/checklists.md`
- `kb/workflows.md`
- `kb/precedents.md`
- `docs/EXECUTION_RECEIPTS.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override:
- canonical validation or receipt docs for exact requirements
- runtime truth about which validations, smoke checks, or rollback paths are currently available
