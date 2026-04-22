# /kb/architecture

## Purpose

This page describes the canonical system structure, component boundaries, interfaces, dependencies, and ownership domains for `refactored-system`.

## Scope

This page governs the architecture of the backend brain only. It does not define a UI layer.

## Facts from current project doctrine

### Purpose of the brain
The AI Brain is the central execution and orchestration core. It should do only six things:
1. Understand the task
2. Load the right context
3. Build an executable plan
4. Authorize the next step
5. Execute and verify
6. Persist what matters

### Canonical planes
The system is divided into planes:
- Control Plane
- Cognition Plane
- Memory Plane
- Tool Plane
- Provider Plane
- Policy Plane
- Verification Plane
- Observability Plane
- Integration Plane

### Cross-plane rule
No plane should pass opaque strings when a typed contract exists.

### Runtime state machine
The canonical execution lifecycle is:
INTAKE → CONTEXT_LOAD → PLAN → AUTHORIZE → EXECUTE → OBSERVE → VERIFY → RETRY_OR_REPLAN → PERSIST → RESPOND → FAIL_CLOSED

## Canonical architecture summary

### 1. Control Plane
Responsibilities:
- intake
- classification
- context loading
- planning coordination
- authorization checks
- dispatch
- retry / fallback / re-plan
- completion gating
- final response assembly

Boundary:
- coordinates other planes
- must not directly implement provider logic, tool logic, memory storage, or browser automation

### 2. Cognition Plane
Roles:
- planner
- builder
- verifier
- researcher
- memory
- recovery

Boundary:
- planner does not execute tools directly
- builder does not self-authorize risky work
- verifier does not trust planner/builder claims without artifacts or receipts
- recovery activates only after failure classification

### 3. Memory Plane
Layers:
- working
- episodic
- semantic
- procedural

Boundary:
- memory writes must respect layer-specific rules
- semantic memory is curated, not a raw dump store
- procedural memory requires repeated success before promotion

### 4. Tool Plane
Purpose:
- normalized action layer for shell, browser, file, API, DB, memory, MCP, and automation capabilities

Boundary:
- tools are invoked through wrappers and policy, not directly by agents
- every tool declares input/output schema, risk class, approval level, retry policy, timeout, verification method, and receipt format

### 5. Provider Plane
Purpose:
- route model work by role, capability, privacy, cost, and fallback policy

Boundary:
- provider routing belongs here, not in agents or control plane
- fallback must narrow scope or fail closed rather than improvise

### 6. Policy Plane
Purpose:
- classify risk
- derive approval and sandbox requirements
- constrain actions, secrets, model/tool pairings, and escalation

Boundary:
- approval is a policy decision against a classified action, not a freeform agent judgment

### 7. Verification Plane
Purpose:
- turn execution claims into reality-checked outcomes

Boundary:
- syntactic, semantic, and environment verification must remain distinct

### 8. Observability Plane
Purpose:
- make the system replayable, inspectable, and auditable

Boundary:
- if a run cannot be traced, replayed, and audited, it is not production-grade

### 9. Integration Plane
Purpose:
- external adapters for Supabase, Ollama, n8n, LangGraph, LlamaIndex, MCP, browser-use, aider, OpenHands, and similar services

Boundary:
- adapters may depend on the brain
- the brain must not depend on any single adapter

## Ownership model

This repo currently implies responsibility domains by plane rather than named teams:
- orchestration ownership for control plane
- reasoning-role ownership for cognition plane
- persistence/retrieval ownership for memory plane
- normalized capability ownership for tool plane
- model routing ownership for provider plane
- runtime law ownership for policy plane
- reality-check ownership for verification plane
- audit/trace ownership for observability plane
- adapter ownership for integrations

## Boundaries

### This page does decide
- the architectural shape of the system
- primary boundaries between planes
- the canonical execution lifecycle
- what belongs inside vs outside the brain

### This page does not decide
- exact implementation order
- exact schema field definitions
- exact workflow steps
- exact runtime configuration values

## Cross-references
- `/kb/principles`
- `/kb/schemas`
- `/kb/workflows`
- `/kb/validation`
- `/kb/safety`
- `/kb/adr`

## Assumptions
- The backend-brain blueprint remains the architecture source of truth until superseded by a later ADR-backed revision.
- The repo will continue to favor modular planes over framework-specific abstractions.
- The current implementation is not yet fully aligned to the canonical architecture.

## Open questions
- Which plane should own context-window compaction and memory-trigger heuristics?
- Which integration adapters belong in-repo vs externalized?
- Should the state machine be implemented as explicit contracts plus persistence from V1, or staged in narrower slices?
