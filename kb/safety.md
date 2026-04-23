# /kb/safety

## Purpose
Define the project’s guardrails, approval posture, risk classes, and fail-closed safety stance.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical risk and safety docs remain stronger for exact policy, and runtime truth remains stronger for what controls are active now.

## When to use this page
Use this page when you need to know:
- which risk classes matter
- when approval is required
- when sandboxing or escalation should be expected
- what fail-closed means in practice

## Content
### Canonical risk classes
- READ_ONLY
- LOCAL_WRITE
- LOCAL_EXECUTION
- EXTERNAL_API_CALL
- DATABASE_MUTATION
- BROWSER_AUTOMATION
- CREDENTIAL_USE
- IRREVERSIBLE

### Core safety rules
- approval is a policy decision against a classified action
- every execution step should have one primary risk class before authorization
- if a step cannot be classified, it should not execute
- ambiguity should resolve to block, defer, or fail closed

### Safety posture
- read-only work is generally lowest risk
- local writes, local execution, database mutation, browser automation, and credential use require stronger controls
- irreversible work defaults to the strongest blocking or elevated-review path
- risky actions should bind to approval, execution, and verification receipts

## Related pages
- `kb/principles.md`
- `kb/repo-rules.md`
- `kb/validation.md`
- `kb/schemas.md`
- `kb/workflows.md`
- `docs/RISK_TAXONOMY.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override:
- canonical risk and safety docs for exact policy language
- runtime truth for which controls, sandboxes, or escalation paths are currently available
