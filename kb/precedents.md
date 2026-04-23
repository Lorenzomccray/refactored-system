# /kb/precedents

## Purpose
Record reusable implementation and governance lessons that should inform future work.

## Authority
Maintained KB.

This page is a governed operational summary. Canonical docs and runtime truth remain stronger than precedents.

## When to use this page
Use this page when a task touches an area the repo has already learned something important about and you want to avoid relearning it from chat.

## Content
### Current precedent set
- the current implementation is still behind the canonical architecture
- structured planner output is the right direction
- explicit staged orchestration is better than vague looping
- browser capability should not be treated as governed browser doctrine until policy and verification are in place
- provider logic belongs in the provider plane
- runtime truth must distinguish callable surfaces from desired ones
- chats are useful working context but weak canonical memory
- bounded runtime slices are safer than broad uncontrolled expansion

### Handling rules
- record the lesson, not the whole transcript
- tie precedents to future decisions, workflows, or checklists when possible
- mark stale precedents when stronger doctrine supersedes them
- use precedents to inform work, not to override canonical docs

## Related pages
- `kb/adr.md`
- `kb/workflows.md`
- `kb/checklists.md`
- `kb/validation.md`
- `kb/safety.md`
- `memory/canonical-precedents.md`

## Freshness
- Last updated: 2026-04-22
- Owner: repo-maintainer
- Review interval: 30 days

## Conflict notes
This page does not override canonical architecture, policy, or runtime truth docs.
