# /kb/faq

## Purpose

This page answers recurring questions, edge cases, and common pitfalls for `refactored-system`.

## FAQ

### Is the current repo already the full architecture?
No. The current repo is an early orchestrator-agent-tool seed. The canonical architecture describes a fuller plane-based system with typed contracts, policy, receipts, validation, and clearer boundaries.

### Are chats canonical project memory?
No. Chats are active working context. Docs are truth, runtime docs are current truth, receipts are evidence, and procedural memory requires repeated success before promotion.

### Can a planner call tools directly?
No. Doctrine says no agent may call a tool directly. Tool invocation should flow through plan → authorization → execution wrapper → receipt → verification.

### Can risky work proceed if it looks fine?
No. Approval is not intuitive judgment; it is a policy decision against a classified action.

### What if a step cannot be classified?
It must not execute.

### What if syntactic validation fails?
Fail closed for that boundary crossing. Semantic validation should not proceed as if the payload were valid.

### Can external frameworks become the brain?
No. They stay as capabilities or adapters. The brain must not depend on any single adapter.

### Can semantic memory store raw chat transcripts?
No. Semantic memory stores validated, reusable, understandable knowledge, not raw transcripts or giant prompt dumps.

### When does procedural memory get updated?
Only after repeated successful reuse, verification of outcomes, and no contradictory evidence.

### What counts as trustworthy execution evidence?
Receipts, artifacts, and verification results. If an action has no receipt, it should not be treated as trustworthy.

### Which docs should be read first for a task?
Use the smallest relevant set. Prefer KB and canonical docs, then runtime truth docs if the task depends on current state, then build and checklist docs.

### Do runtime docs override architecture docs?
No. Runtime docs override assumptions about current state. They do not silently rewrite accepted architecture doctrine.

### Can raw repo dumps be treated as source of truth?
No. Raw repo dumps are explicitly not canonical truth.

### What is the safest near-term implementation priority?
The doctrine points toward bounded runtime slices: state machine, approval or risk enforcement, receipts, schemas, and validation before broadening capability surface.

## Cross-references
- `/kb/principles`
- `/kb/repo-rules`
- `/kb/architecture`
- `/kb/safety`
- `/kb/validation`
- `/kb/precedents`
