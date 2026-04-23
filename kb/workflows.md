# /kb/workflows

## Purpose
Describe the standard operating workflows for planning, debugging, refactoring, release, and incident response.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical docs remain stronger for exact doctrine, and runtime truth remains stronger for what is active now.

## When to use this page
Use this page when you need the default sequence for:
- planning a bounded change
- debugging a failure path
- performing a refactor
- preparing a release
- handling an incident or recovery step

## Content
### Core workflow posture
- read before write
- classify before authorize
- authorize before execute
- verify before claim
- persist selectively, not indiscriminately

### Standard workflows
#### Planning
- read the smallest relevant canonical pages
- check runtime truth when current state matters
- state assumptions, unknowns, and success criteria
- identify the smallest viable slice

#### Debugging
- reconstruct the path from receipts, logs, runtime docs, and artifacts
- classify the failure type
- verify reproducibility
- prefer minimal targeted fixes
- record reusable lessons or precedents

#### Refactoring
- confirm the target boundary
- check architecture and schemas before editing
- keep behavior, contract, and receipt impact explicit
- avoid donor-code merges without adaptation

#### Release
- confirm what changed and what did not
- verify compatibility and safety impact
- run validation and smoke checks
- ensure runtime truth is current enough to describe reality

#### Incident response
- fail closed where policy requires
- preserve evidence first
- classify the incident
- contain the blast radius
- execute the smallest verified recovery path

## Related pages
- `kb/principles.md`
- `kb/architecture.md`
- `kb/checklists.md`
- `kb/validation.md`
- `kb/safety.md`
- `kb/precedents.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override:
- canonical workflow, safety, or validation doctrine
- runtime truth about which checks, tools, or recovery paths are currently available
