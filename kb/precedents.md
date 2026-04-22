# /kb/precedents

## Purpose

This page records prior refactors, implementation lessons, and governance lessons that should inform future work.

## Scope

This page stores reusable lessons, not exhaustive transcripts.

## Current precedent set

### Precedent 1 — Current implementation lags canonical architecture
The repo contains an orchestrator-agent-tool skeleton, but the canonical docs describe a much richer plane-based architecture with contracts, policy, receipts, and verification boundaries.

Lesson:
Treat the repo as an early implementation seed, not proof that the full architecture already exists.

### Precedent 2 — Structured planner output is already the right direction
The project has already moved toward planner output with structured fields rather than plain freeform strings.

Lesson:
Continue toward explicit schemas rather than regressing to opaque text.

### Precedent 3 — Explicit staged orchestration is better than vague loops
The project has already leaned toward planner, builder, and verifier staging.

Lesson:
Continue that evolution toward a real state machine and execution graph.

### Precedent 4 — Browser capability is not the same as production-grade browser doctrine
Basic browser capability can exist before policy mediation, risk classification, receipt capture, and verification are complete.

Lesson:
Treat browser automation as a capability until it is governed by runtime law.

### Precedent 5 — Provider improvements belong in the provider plane
Provider integrations can improve incrementally, but provider routing should not leak into orchestration logic.

Lesson:
Keep provider selection and fallback policy inside the provider plane.

### Precedent 6 — Runtime truth must distinguish real callable surfaces from desired ones
Earlier validated setup notes showed Airtable operational while other connectors were not confirmed callable in that pass.

Lesson:
Do not plan as if desired connectors already exist. Revalidate and update runtime truth.

### Precedent 7 — Chats are useful context but weak canonical memory
The memory spine guidance explicitly says chat is working context, docs are truth, runtime docs are current truth, and receipts are evidence.

Lesson:
Do not let chat convenience replace durable project memory.

### Precedent 8 — Bounded runtime slices are the safer near-term path
Earlier project notes favored state machine, approval, and receipts before broadening the surface.

Lesson:
Focus on core runtime law and replayability before widening capability scope.

## Handling rules
1. Record the lesson, not the whole transcript.
2. Tie each precedent to a future decision, workflow, or checklist when possible.
3. If a precedent conflicts with newer accepted doctrine, mark it stale or superseded.
4. Precedents inform action; they do not override canonical architecture docs.

## Cross-references
- `/kb/adr`
- `/kb/workflows`
- `/kb/checklists`
- `/kb/validation`
- `/kb/safety`
