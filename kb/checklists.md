# /kb/checklists

## Purpose

This page provides reusable checklists for refactors, reviews, releases, and verification in `refactored-system`.

## Refactor checklist
- Confirm the target boundary from `/kb/architecture`
- Confirm the smallest safe slice
- Identify affected contracts from `/kb/schemas`
- Identify affected risk classes or approval paths from `/kb/safety`
- State what changes and what does not change
- Preserve or improve receipt and verification paths
- Avoid donor-code merge behavior
- Update canonical docs if structure or doctrine changes
- Update runtime truth docs if actual current state changes
- Record reusable lessons in `/kb/precedents` if needed

## Review checklist
- Is the change grounded in canonical docs?
- Are facts separated from assumptions?
- Are plane boundaries preserved?
- Are typed contracts used where they should be?
- Are risky actions classified and gated?
- Are verification expectations explicit?
- Are receipts and observability implications explicit?
- Are open questions surfaced rather than hidden?

## Release checklist
- Confirm release scope
- Confirm schema compatibility
- Confirm validation and smoke coverage
- Confirm safety and approval impact
- Confirm runtime truth docs are current enough
- Confirm artifact and receipt trail exists
- Confirm rollback posture is understood for risky changes

## Verification checklist
- Syntactic checks identified
- Semantic checks identified
- Environment checks identified
- Success criteria stated
- Evidence refs captured
- Recommended next action clear
- Uncertainty stated when appropriate

## Safety-sensitive change checklist
- Primary risk class identified
- Highest-risk class chosen if multiple actions are combined
- Approval requirement clear
- Sandbox requirement clear
- Receipt requirement clear
- Verification requirement clear
- Escalation requirement clear
- Fail-closed path defined

## Runtime truth update checklist
- Does the change alter current repo structure?
- Does it alter current tools, providers, or workflows?
- Does it close or add a current gap or blocker?
- Should a runtime doc be updated now rather than later?
- Are assumptions being replaced by actual observed state?

## Cross-references
- `/kb/workflows`
- `/kb/validation`
- `/kb/safety`
- `/kb/repo-rules`
- `/kb/precedents`
