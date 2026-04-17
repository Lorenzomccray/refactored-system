# PHASE_1_SOVEREIGN_RUNTIME_SPINE

**Status:** Active Build Target  
**Tier:** Build Docs (Tier 3)  
**Purpose:** Define the smallest high-value runtime slice that turns the sovereign plan into an enforceable execution spine without merging donor runtime code.

---

## 1. Phase Goal

Build the minimum runtime spine that makes the system:
- authority-aware
- policy-mediated
- receipt-emitting
- memory-disciplined
- adapter-ready

This phase does **not** attempt to ship the full Manus-class execution layer or full Tasklet-class automation layer.

It builds the governor that those layers must pass through.

---

## 2. Non-Negotiable Constraint

This phase is subordinate to existing canonical docs.

It must preserve:
- the backend-brain plane model
- typed contracts
- approval before risky execution
- receipts and verification over invisible behavior
- source-tier routing before reasoning or execution

This phase is **not** a rewrite.
It is the first runtime realization of the original plan.

---

## 3. In-Scope Runtime Components

### 3.1 Source Router / Authority Resolver

**Purpose:** Resolve which tier must be consulted first for a given task.

**Required behaviors:**
- classify task into architecture / runtime / build / reference / external lookup
- load preferred tier first
- escalate on conflict
- emit source attribution block inputs
- fail closed on unresolved source conflict for high-impact tasks

**Target files:**
- `app/orchestrator/task_classifier.py`
- `app/orchestrator/context_loader.py`
- `app/orchestrator/source_router.py` *(new if needed)*
- `app/schemas/task.py`
- `app/schemas/source_resolution.py` *(new if needed)*

### 3.2 Governor State Machine

**Purpose:** Make execution phases explicit and replayable.

**Required behaviors:**
- intake
- context load
- plan
- authorize
- execute
- observe
- verify
- retry / replan
- persist
- respond
- fail closed

**Target files:**
- `app/orchestrator/state_machine.py`
- `app/orchestrator/loop_manager.py`
- `app/orchestrator/execution_planner.py`
- `app/schemas/execution_graph.py`

### 3.3 Approval and Policy Service

**Purpose:** Convert operator control into enforceable policy decisions.

**Required behaviors:**
- classify every planned step into risk taxonomy
- map risk class to approval requirement
- separate `READ_ONLY`, `LOCAL_WRITE`, `LOCAL_EXECUTION`, `EXTERNAL_API_CALL`, `DATABASE_MUTATION`, `BROWSER_AUTOMATION`, `CREDENTIAL_USE`, and `IRREVERSIBLE`
- prevent builder/tool bypass of policy

**Target files:**
- `app/policy/risk_engine.py`
- `app/policy/approval_policy.py`
- `app/policy/action_constraints.py`
- `app/orchestrator/approvals.py`
- `app/schemas/approval_request.py`
- `app/schemas/approval_decision.py`

### 3.4 Receipt and Provenance Pipeline

**Purpose:** Turn actions into auditable execution evidence.

**Required behaviors:**
- emit run id, task id, plan id, step id
- store tool result, verifier result, approval event, and source attribution
- support replay and human inspection
- distinguish observations from claims

**Target files:**
- `app/tools/tool_receipts.py`
- `app/telemetry/run_receipts.py`
- `app/telemetry/trace_store.py`
- `app/verification/receipt_checker.py`
- `app/schemas/run_receipt.py`
- `app/schemas/tool_result.py`
- `app/schemas/verification_result.py`

### 3.5 Memory Write Gate

**Purpose:** Prevent uncontrolled long-term memory and donor pollution.

**Required behaviors:**
- classify candidate writes by working / episodic / semantic / procedural
- allow semantic/procedural writes only through explicit policy
- reject raw transcript dumping
- require validation before promotion

**Target files:**
- `app/memory/memory_policy.py`
- `app/memory/memory_writer.py`
- `app/memory/promotion_rules.py`
- `app/schemas/memory_record.py`

### 3.6 Adapter Contract Layer

**Purpose:** Ensure external capability remains replaceable and subordinate.

**Required behaviors:**
- declare tool capability, schema, risk class, approval level, timeout, retry, verification method
- prevent direct donor runtime dependence from entering the core
- allow future Manus / Tasklet / MCP integration behind explicit contracts

**Target files:**
- `app/tools/tool_contract.py`
- `app/tools/tool_registry.py`
- `app/tools/tool_authz.py`
- `app/integrations/mcp/` *(contract-first, implementation later)*
- `app/schemas/tool_call.py`

---

## 4. Explicit Out of Scope

The following are intentionally excluded from Phase 1:

- full browser/computer-use autonomy
- recurring workflow scheduler / durable automation engine
- external SaaS fan-out integrations
- generalized RAG stack
- full multi-provider optimization
- UI, dashboard, or operator console
- donor runtime code imports from Gobii, OpenClaw, or sovereignty-MCP
- external workflow state as canonical truth

These can only be layered in after the runtime spine is proven.

---

## 5. Build Sequence Inside Phase 1

### Step 1 — Typed contracts and state machine skeleton
Create the minimal schemas and explicit state transitions first.

### Step 2 — Source router and context loader
Make source-tier routing real before expanding execution power.

### Step 3 — Risk engine and approval policy
Ensure no tool path can outrun governance.

### Step 4 — Tool contract and receipt wrapper
Every future action must go through declared contracts.

### Step 5 — Receipt checker and verifier handshake
Make receipts structurally useful, not just logs.

### Step 6 — Memory write gate
Prevent memory pollution before external execution breadth grows.

---

## 6. Donor-Derived Patterns Allowed in This Phase

These pattern classes may inform implementation, but only behind new repo-native code:

- Manus-class: delegated producer pattern, planner/executor/verifier role split
- Tasklet-class: durable workflow boundaries and recurring-task concepts
- sovereignty-MCP: preflight, dedup, decision/lesson journaling concepts
- MCP official docs: adapter and protocol boundaries

No donor runtime file may be copied into the core unchanged.

---

## 7. Deliverables

By the end of Phase 1, the repo should have:

- a source-aware task classification path
- an explicit runtime state machine
- a functioning risk-to-approval decision path
- contract-first tool invocation wrappers
- receipts for meaningful actions
- memory write policy enforcement hooks
- a clean boundary where Manus-class execution and Tasklet-class automation can later plug in safely

---

## 8. Exit Condition

Phase 1 is complete only when the system can do the following:

1. accept a task
2. resolve the correct source tier
3. create a bounded execution graph
4. classify step risk
5. refuse or request approval for unsafe work
6. execute through a wrapper that emits receipts
7. verify what happened
8. write only permitted memory artifacts
9. stop safely when evidence is insufficient

If any one of those is missing, the sovereign runtime spine is not yet real.

---

## 9. Phase 1 Output to Phase 2

Only after this phase is accepted should the project begin:
- delegated producer runtime for Manus-class execution
- recurring workflow engine for Tasklet-class automation
- broader MCP integration breadth
- browser/computer-use execution expansion
- semantic retrieval expansion

Phase 1 exists to ensure those later capabilities increase power **without decreasing control**.
