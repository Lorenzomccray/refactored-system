# BUILD ORDER

## Purpose
Define the canonical implementation order so the system grows in controlled slices and avoids integration-first drift.

## Core rule
Do not build everything at once.

The order of construction is part of the architecture.

## Canonical build sequence

### Phase 1 — Contracts and Control
Build first:
- schemas
- state machine
- risk taxonomy
- approval policy

#### Why first
Without contracts and control, every later layer becomes ambiguous, hard to verify, and easy to contaminate.

#### Definition of done
- canonical schemas exist
- execution states are explicit
- risk classes exist
- approvals are policy decisions, not ad hoc judgments

### Phase 2 — Core Execution
Build next:
- planner / builder / verifier contract flow
- provider router
- tool registry
- receipts

#### Why second
This makes the core able to execute one bounded flow with traceable decisions.

#### Definition of done
- one bounded end-to-end run can plan, authorize, execute, receipt, and verify

### Phase 3 — Persistence
Build:
- working store
- episodic store
- memory writer
- trace store

#### Why third
Persistence should follow stable execution semantics, not precede them.

#### Definition of done
- successful and failed runs create durable episodic records and traces

### Phase 4 — Verification
Build:
- syntactic verification
- semantic verification
- environment verification
- retry manager
- fallback manager

#### Why fourth
Verification turns execution into reality-checked behavior and enables safe retries.

#### Definition of done
- no run reaches final success without verifier output

### Phase 5 — Semantic Layer
Build:
- retrieval engine
- semantic store
- vector adapter

#### Why fifth
Semantic memory should be built on top of disciplined execution and curated persistence, not raw dumps.

#### Definition of done
- retrieval works on curated, validated sources only

### Phase 6 — Integrations
Build last:
- MCP
- LlamaIndex
- Langfuse
- Ollama or vLLM
- n8n or Supabase
- other adapters and workers

#### Why last
Integrations are capabilities and services, not the brain itself.

#### Definition of done
- adapters attach cleanly without changing core ownership or contracts

## Hard sequencing rules
- No adapter-first architecture.
- No browser or channel layer before mediated execution exists.
- No semantic memory before disciplined episodic persistence.
- No prototype lessons become canonical implementation order without a decision log entry.

## First implementation milestone
The first real milestone is one verified, receipt-backed tool call proving:
- plan
- authorize
- execute
- receipt
- verify
