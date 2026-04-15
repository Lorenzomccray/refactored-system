# BUILD_ORDER
## Canonical Implementation Sequence

---

## 1. Purpose

This document defines the order in which the backend brain should be built.

The goal is to prevent:
- capability sprawl before control exists
- premature integration work
- unverifiable tool execution
- memory pollution before contracts exist
- building a UI around a weak brain

---

## 2. Build Philosophy

Build the control plane before the capability plane.

Build contracts before automation.

Build verification before claims of success.

Build persistence before ambition.

Build integrations last.

---

## 3. Phase 1 — Contracts and Control

### Objective
Create the core language and control skeleton of the system.

### Build
- `app/schemas/`
- `app/orchestrator/state_machine.py`
- `app/policy/risk_engine.py`
- `app/policy/approval_policy.py`

### Deliverables
- typed contracts
- runtime state machine
- risk taxonomy
- approval rules

### Exit criteria
- execution states are explicit
- steps can be classified
- risky actions cannot bypass policy
- contracts validate

---

## 4. Phase 2 — Core Execution

### Objective
Make planner, builder, verifier, provider routing, and tool registry real.

### Build
- planner/builder/verifier contract flow
- `provider_router.py`
- `tool_contract.py`
- `tool_registry.py`
- `tool_authz.py`
- `tool_receipts.py`

### Deliverables
- plan to execution graph flow
- provider selection path
- tool registration and invocation wrapper
- receipt emission

### Exit criteria
- tools cannot run without declared contracts
- provider routing is policy-aware
- receipts are generated for execution

---

## 5. Phase 3 — Persistence

### Objective
Store working truth and durable run history.

### Build
- `working_store.py`
- `episodic_store.py`
- `memory_writer.py`
- `trace_store.py`
- `approval_log.py`
- `failure_log.py`

### Deliverables
- working state persistence
- episodic run history
- approval history
- failure history
- trace records

### Exit criteria
- runs can be replayed by id
- approvals/denials are durable
- failures are queryable
- memory writes follow policy

---

## 6. Phase 4 — Verification

### Objective
Make success claims trustworthy.

### Build
- `verifier_engine.py`
- `output_checker.py`
- `artifact_validator.py`
- `environment_validator.py`
- `receipt_checker.py`

### Deliverables
- syntactic verification
- semantic verification
- environment verification
- verifier-linked receipts

### Exit criteria
- no state-changing action can be called successful without verification
- verifier outputs drive retry/replan decisions

---

## 7. Phase 5 — Semantic Layer

### Objective
Add useful retrieval without turning the core into a RAG monolith.

### Build
- `semantic_store.py`
- `retrieval_engine.py`
- vector adapter
- semantic memory write filtering

### Deliverables
- semantic retrieval
- curated semantic memory
- memory-plane separation preserved

### Exit criteria
- retrievable docs and architecture notes are available
- semantic memory is curated, not a dump

---

## 8. Phase 6 — Integrations

### Objective
Connect external capability without contaminating the core.

### Build
- MCP adapter
- LlamaIndex adapter
- Langfuse adapter
- Ollama/vLLM adapter
- n8n/Supabase adapters as needed

### Deliverables
- external capability bridges
- adapter isolation
- optional no-cost upgrades

### Exit criteria
- core brain remains coherent if any adapter is removed
- integrations are replaceable

---

## 9. Recommended First Concrete Files

Create first:

```text
app/schemas/
app/orchestrator/state_machine.py
app/policy/risk_engine.py
app/policy/approval_policy.py
app/providers/provider_router.py
app/tools/tool_contract.py
```

Create these docs in parallel:

```text
docs/MASTER_AI_SYSTEM_V2.md
docs/SCHEMA_CONTRACTS.md
docs/RISK_TAXONOMY.md
docs/MEMORY_WRITE_POLICY.md
docs/EXECUTION_RECEIPTS.md
```

---

## 10. Anti-Pattern Warnings

Do not:
- build the UI first
- wire browser automation before policy mediation
- add semantic memory before memory write rules exist
- let tool wrappers bypass authorization
- let provider routing become hardcoded into agents
- put giant prompt assembly blobs at the center of the system
- confuse logs with receipts
- confuse chat history with memory

---

## 11. Success Definition

The build order is correct if each phase:
- reduces ambiguity
- increases control
- increases replayability
- increases verification
- keeps the system modular
- does not depend on fragile hidden prompt behavior

This sequence is meant to produce a real backend brain, not a theatrical demo.
