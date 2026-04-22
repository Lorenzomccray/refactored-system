# /kb/adr

## Purpose

This page indexes important architecture and governance decisions for `refactored-system`.

## Scope

This page is the registry and summary layer for decisions. Detailed ADR files may live elsewhere.

## Accepted decision spine

### ADR-001 — Backend brain, no UI layer in core
Status: accepted
Decision: The repo’s canonical focus is the backend execution and orchestration brain, not a UI layer.
Why it matters: Prevents product-surface drift from distorting core architecture.

### ADR-002 — Plane-based architecture
Status: accepted
Decision: The system is divided into explicit planes with one responsibility domain each.
Why it matters: Prevents hidden control blobs and encourages modular boundaries.

### ADR-003 — Typed contracts over opaque strings
Status: accepted
Decision: Cross-plane communication should use canonical typed contracts.
Why it matters: Reduces drift, ambiguity, and unverifiable execution.

### ADR-004 — Approval and risk classification as runtime law
Status: accepted
Decision: Risk is classified per step, and approval is a policy decision against a classified action.
Why it matters: Prevents ad hoc authorization behavior.

### ADR-005 — Verification is multi-dimensional
Status: accepted
Decision: Syntactic, semantic, and environment verification remain separate dimensions.
Why it matters: Avoids false positives and vague success reporting.

### ADR-006 — Receipts are minimum trust units
Status: accepted
Decision: Meaningful actions require execution receipts.
Why it matters: Supports replay, audit, and debugging.

### ADR-007 — Memory is layered and promotion-driven
Status: accepted
Decision: Working, episodic, semantic, and procedural memory have different write rules; procedural memory is never written on first success.
Why it matters: Keeps memory useful and prevents dump-store drift.

### ADR-008 — Source hierarchy and canonical truth
Status: accepted
Decision: Canonical docs precede runtime truth docs, build docs, reference notes, and external registries; raw dumps are not canonical truth.
Why it matters: Preserves trustworthy source selection.

### ADR-009 — Adapters over hard dependencies
Status: accepted
Decision: External systems remain adapters or capabilities, not the brain itself.
Why it matters: Preserves sovereignty and reduces lock-in.

## ADR usage rules
1. Use an ADR when a decision changes architecture, contracts, runtime law, or source-of-truth rules.
2. ADRs should state the decision, rationale, and consequences.
3. If a KB page and an ADR conflict, surface the conflict explicitly.
4. Runtime docs can override assumptions, but not silently rewrite accepted architecture decisions.

## Cross-references
- `/kb/principles`
- `/kb/architecture`
- `/kb/schemas`
- `/kb/safety`
- `/kb/precedents`
