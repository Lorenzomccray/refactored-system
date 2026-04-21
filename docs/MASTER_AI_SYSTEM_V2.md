# MASTER AI SYSTEM v2
## Backend Brain Blueprint
### No UI layer. Core execution and orchestration only.

---

## 1. Purpose

The AI Brain is the central execution and orchestration core.

It should do only six things:

1. Understand the task
2. Load the right context
3. Build an executable plan
4. Authorize the next step
5. Execute and verify
6. Persist what matters

Everything else is a capability attached through adapters, providers, tools, and services.

The brain orchestrates.
It does not absorb every integration into a monolith.

---

## 2. Design Principles

### 2.1 Core principles

- Correctness over fluency
- Verification over assumption
- Small working build slices over broad vague autonomy
- Typed contracts over stringly-typed handoffs
- Read-only inspection before state-changing action
- Approval before risky execution
- Modular subsystems over giant prompt logic
- Adapters over hard dependencies
- Logs, receipts, and traces over invisible behavior
- Fail closed rather than improvising unsafe execution

### 2.2 Architectural posture

The system is divided into planes.

Each plane has one responsibility domain.

Each plane communicates through typed contracts.

No single plane may become a hidden control blob.

### 2.3 Ownership Law

The core brain is the only authoritative owner of:
- task state
- approval state
- execution lifecycle state
- memory promotion state
- final receipts
- final run disposition

All adapters, workers, tools, and surfaces are non-authoritative.

They may:
- transport
- cache
- enrich
- display
- propose
- execute bounded work

They may not:
- redefine truth
- redefine completion
- redefine approval
- redefine memory promotion

---

## 3. Canonical System Topology

### 3.1 Control Plane

This is the real brain.

#### Responsibilities

- task intake
- task classification
- context loading
- planning coordination
- authorization checks
- dispatch
- retry / fallback / re-plan
- completion gating
- final response assembly

#### Core modules

```text
app/orchestrator/
  router.py
  dispatcher.py
  loop_manager.py
  approvals.py
  state_manager.py
  task_classifier.py
  context_loader.py
  execution_planner.py
  retry_manager.py
  fallback_manager.py
  completion_gate.py
  state_machine.py
```

#### Rule

The control plane may coordinate every other plane, but it does not directly implement provider logic, tool logic, memory storage, or browser automation.

---

### 3.2 Cognition Plane

This is where reasoning roles live.

#### Agents

```text
app/agents/
  planner_agent.py
  builder_agent.py
  verifier_agent.py
  researcher_agent.py
  memory_agent.py
  recovery_agent.py
```

#### Role boundaries

- **Planner Agent** decomposes goals into executable steps and constraints.
- **Builder Agent** executes approved steps through tools and providers.
- **Verifier Agent** checks whether reality matches expected outcomes.
- **Researcher Agent** gathers external or documentary context when allowed.
- **Memory Agent** summarizes and promotes memory candidates.
- **Recovery Agent** handles failure-driven re-entry when execution goes off-plan.

#### Hard rules

- Planner never executes tools directly.
- Builder never self-authorizes risky work.
- Verifier never trusts planner or builder claims without artifacts or receipts.
- Recovery only activates after failure type is classified.

---

### 3.3 Memory Plane

The memory system has four layers.

#### Working Memory

Use for:
- active task context
- current substep chain
- recent observations
- temporary tool outputs
- scratch state

Characteristics:
- high churn
- low retention
- fast access
- aggressively pruned

#### Episodic Memory

Use for:
- completed runs
- failures
- retries
- approvals granted/denied
- operator interventions
- final artifacts
- recovery outcomes

Characteristics:
- durable
- historical
- replay-friendly

#### Semantic Memory

Use for:
- indexed docs
- architecture decisions
- system references
- validated notes
- retrievable artifacts
- external knowledge summaries

Characteristics:
- retrieval-oriented
- semantically searchable
- curated, not raw dump storage

#### Procedural Memory

Use for:
- known-good workflows
- install sequences
- recovery runbooks
- debugging playbooks
- tool recipes
- policy-linked execution patterns

Characteristics:
- promoted only after repeated success
- reusable
- operational

#### Memory modules

```text
app/memory/
  working_store.py
  episodic_store.py
  semantic_store.py
  procedural_store.py
  retrieval_engine.py
  memory_writer.py
  memory_policy.py
  summarizer.py
  promotion_rules.py
```

#### Memory write policy

##### Working memory

Write:
- every step output
- every recent observation
- temporary tool results
- current execution graph

##### Episodic memory

Write:
- run summaries
- approvals
- denials
- retries
- failures
- final artifacts
- important operator decisions

##### Semantic memory

Write only:
- curated docs
- validated design notes
- extracted repo truths
- reusable references
- indexed artifacts worth retrieval

##### Procedural memory

Write only after repeated successful reuse:
- runbooks
- install recipes
- restart patterns
- repair flows
- tool usage playbooks

#### Promotion rule

No item is promoted into procedural memory on first success.

---

### 3.4 Tool Plane

This is the action layer.

#### Tool categories

```text
app/tools/
  base_tool.py
  tool_contract.py
  tool_registry.py
  tool_authz.py
  tool_receipts.py
  tool_sandbox_policy.py
  shell_tool.py
  browser_tool.py
  file_tool.py
  api_tool.py
  db_tool.py
  memory_tool.py
  mcp_tool.py
  automation_tool.py
```

#### Every tool must declare

- capability name
- input schema
- output schema
- risk class
- approval level
- retry policy
- timeout
- verification method
- audit/receipt record format

#### Hard rule

No agent may call a tool directly.

Every tool invocation must flow through:

```text
plan → authorization → execution wrapper → receipt → verification
```

---

### 3.5 Provider Plane

This is the model-routing substrate.

#### Provider modules

```text
app/providers/
  base_provider.py
  provider_router.py
  openai_provider.py
  anthropic_provider.py
  deepseek_provider.py
  local_provider.py
  model_registry.py
  routing_policy.py
  fallback_policy.py
  provider_health.py
  cost_policy.py
```

#### Target routing

- **Planner** → highest reasoning model
- **Builder** → strongest code/tool execution model
- **Verifier** → strongest structured-output / consistency model
- **Research/browser summarization** → cheaper fast model
- **Sensitive/private** → local provider path when available

#### Fallback chain

1. retry same model/provider
2. retry with narrowed scope or reduced context
3. alternate provider
4. re-plan with downgraded capability or narrower scope
5. fail closed with diagnostic artifact

---

### 3.6 Policy Plane

This is runtime law.

#### Policy modules

```text
app/policy/
  risk_engine.py
  approval_policy.py
  action_constraints.py
  secrets_policy.py
  sandbox_policy.py
  model_tool_matrix.py
  escalation_policy.py
  audit_policy.py
```

#### Risk taxonomy

Every planned action must be classified as one of:

- `READ_ONLY`
- `LOCAL_WRITE`
- `LOCAL_EXECUTION`
- `EXTERNAL_API_CALL`
- `DATABASE_MUTATION`
- `BROWSER_AUTOMATION`
- `CREDENTIAL_USE`
- `IRREVERSIBLE`

#### Each class defines

- allowed by default
- approval required
- sandbox required
- blocked outright
- verifier required
- receipt required
- escalation required

#### Hard rule

Approval is not a feeling.
Approval is a policy decision against a classified action.

---

### 3.7 Verification Plane

This is what turns execution into reality-checked behavior.

#### Verification modules

```text
app/verification/
  verifier_engine.py
  assertion_runner.py
  output_checker.py
  artifact_validator.py
  environment_validator.py
  receipt_checker.py
  success_criteria.py
```

#### Verification layers

##### Syntactic verification

Checks:
- schema validity
- parseability
- required fields present
- artifacts exist

##### Semantic verification

Checks:
- result matches requested goal
- output meaning matches plan intent
- no major omissions or contradictions

##### Environment verification

Checks:
- file actually changed
- command actually ran
- process actually restarted
- service actually responded
- state actually persisted

#### Hard rule

Do not collapse all verification into one vague “success” flag.

---

### 3.8 Observability Plane

This is what makes the system inspectable.

#### Telemetry modules

```text
app/telemetry/
  logger.py
  trace_store.py
  metrics.py
  event_bus.py
  artifact_store.py
  run_receipts.py
  approval_log.py
  failure_log.py
  memory_log.py
```

#### Every run should emit

- run id
- task id
- plan id
- step ids
- tool receipts
- verifier results
- approval events
- retries
- fallback events
- persisted memory writes
- final disposition

#### Hard rule

If a run cannot be traced, replayed, and audited, it is not production-grade.

---

### 3.9 Integration Plane

This is the external-facing adapter layer.

#### Integration modules

```text
app/integrations/
  supabase/
  ollama/
  n8n/
  langgraph/
  llamaindex/
  mcp/
  browser_use/
  aider/
  openhands/
```

#### Adapter rule

Adapters may depend on the brain.
The brain must not depend on any single adapter.

#### Keep external

- LangGraph
- LlamaIndex
- Supabase
- Ollama
- n8n
- MCP
- browser-use
- aider
- OpenHands

These are capabilities or services, not the brain itself.

---

## 4. Cross-Plane Contract Layer

This is mandatory.

No plane should pass opaque strings when a typed contract exists.

### Canonical schemas

```text
app/schemas/
  task.py
  plan.py
  execution_step.py
  execution_graph.py
  tool_call.py
  tool_result.py
  verification_result.py
  approval_request.py
  approval_decision.py
  memory_record.py
  run_receipt.py
  failure_record.py
```

### Required contract rules

- Planner emits `Plan`
- Execution planner emits `ExecutionGraph`
- Tool wrapper emits `ToolResult`
- Policy engine emits `ApprovalDecision`
- Verifier emits `VerificationResult`
- Memory layer writes `MemoryRecord`
- Telemetry emits `RunReceipt`
- Failure paths emit `FailureRecord`

---

## 5. Runtime State Machine

This is the canonical execution lifecycle.

```text
INTAKE
→ CONTEXT_LOAD
→ PLAN
→ AUTHORIZE
→ EXECUTE
→ OBSERVE
→ VERIFY
→ RETRY_OR_REPLAN
→ PERSIST
→ RESPOND
→ FAIL_CLOSED
```

### State meanings

#### INTAKE

Normalize incoming task, operator context, and execution intent.

#### CONTEXT_LOAD

Load working memory, episodic history, semantic retrieval, and policy context.

#### PLAN

Produce a plan and execution graph.

#### AUTHORIZE

Classify risk and determine whether approval is required.

#### EXECUTE

Run approved steps through the tool/provider layer.

#### OBSERVE

Capture receipts, outputs, logs, and intermediate artifacts.

#### VERIFY

Run syntactic, semantic, and environment checks.

#### RETRY_OR_REPLAN

Retry same path, fallback, or re-plan with narrower scope.

#### PERSIST

Store memory-worthy outputs, artifacts, and traces.

#### RESPOND

Assemble operator-facing result.

#### FAIL_CLOSED

Stop safely with a diagnostic artifact.

---

## 6. Canonical Repository Layout

```text
refactored-system/
├── main.py
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── settings_loader.py
│   │   ├── dependency_registry.py
│   │   ├── lifecycle.py
│   │   ├── constants.py
│   │   └── feature_flags.py
│   │
│   ├── orchestrator/
│   │   ├── router.py
│   │   ├── dispatcher.py
│   │   ├── loop_manager.py
│   │   ├── approvals.py
│   │   ├── state_manager.py
│   │   ├── task_classifier.py
│   │   ├── context_loader.py
│   │   ├── execution_planner.py
│   │   ├── retry_manager.py
│   │   ├── fallback_manager.py
│   │   ├── completion_gate.py
│   │   └── state_machine.py
│   │
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── builder_agent.py
│   │   ├── verifier_agent.py
│   │   ├── researcher_agent.py
│   │   ├── memory_agent.py
│   │   └── recovery_agent.py
│   │
│   ├── memory/
│   │   ├── working_store.py
│   │   ├── episodic_store.py
│   │   ├── semantic_store.py
│   │   ├── procedural_store.py
│   │   ├── retrieval_engine.py
│   │   ├── memory_writer.py
│   │   ├── memory_policy.py
│   │   ├── summarizer.py
│   │   └── promotion_rules.py
│   │
│   ├── providers/
│   │   ├── base_provider.py
│   │   ├── provider_router.py
│   │   ├── openai_provider.py
│   │   ├── anthropic_provider.py
│   │   ├── deepseek_provider.py
│   │   ├── local_provider.py
│   │   ├── model_registry.py
│   │   ├── routing_policy.py
│   │   ├── fallback_policy.py
│   │   ├── provider_health.py
│   │   └── cost_policy.py
│   │
│   ├── tools/
│   │   ├── base_tool.py
│   │   ├── tool_contract.py
│   │   ├── tool_registry.py
│   │   ├── tool_authz.py
│   │   ├── tool_receipts.py
│   │   ├── tool_sandbox_policy.py
│   │   ├── shell_tool.py
│   │   ├── browser_tool.py
│   │   ├── file_tool.py
│   │   ├── api_tool.py
│   │   ├── db_tool.py
│   │   ├── memory_tool.py
│   │   ├── mcp_tool.py
│   │   └── automation_tool.py
│   │
│   ├── browser/
│   │   ├── playwright_controller.py
│   │   ├── browser_context_service.py
│   │   ├── extraction_profiles.py
│   │   ├── workflow_runner.py
│   │   ├── page_state_cache.py
│   │   └── browser_policy.py
│   │
│   ├── policy/
│   │   ├── risk_engine.py
│   │   ├── approval_policy.py
│   │   ├── action_constraints.py
│   │   ├── secrets_policy.py
│   │   ├── sandbox_policy.py
│   │   ├── model_tool_matrix.py
│   │   ├── escalation_policy.py
│   │   └── audit_policy.py
│   │
│   ├── verification/
│   │   ├── verifier_engine.py
│   │   ├── assertion_runner.py
│   │   ├── output_checker.py
│   │   ├── artifact_validator.py
│   │   ├── environment_validator.py
│   │   ├── receipt_checker.py
│   │   └── success_criteria.py
│   │
│   ├── integrations/
│   │   ├── supabase/
│   │   ├── ollama/
│   │   ├── n8n/
│   │   ├── langgraph/
│   │   ├── llamaindex/
│   │   ├── mcp/
│   │   ├── browser_use/
│   │   ├── aider/
│   │   └── openhands/
│   │
│   ├── telemetry/
│   │   ├── logger.py
│   │   ├── trace_store.py
│   │   ├── metrics.py
│   │   ├── event_bus.py
│   │   ├── artifact_store.py
│   │   ├── run_receipts.py
│   │   ├── approval_log.py
│   │   ├── failure_log.py
│   │   └── memory_log.py
│   │
│   └── schemas/
│       ├── task.py
│       ├── plan.py
│       ├── execution_step.py
│       ├── execution_graph.py
│       ├── tool_call.py
│       ├── tool_result.py
│       ├── verification_result.py
│       ├── approval_request.py
│       ├── approval_decision.py
│       ├── memory_record.py
│       ├── run_receipt.py
│       └── failure_record.py
│
├── data/
│   ├── state/
│   ├── artifacts/
│   ├── logs/
│   ├── cache/
│   └── vectors/
│
├── configs/
│   ├── system.yaml
│   ├── routing.yaml
│   ├── tools.yaml
│   ├── memory.yaml
│   ├── policy.yaml
│   └── observability.yaml
│
├── scripts/
├── tests/
└── docs/
```

---

## 7. Canonical Execution Flow

```text
User Task
↓
Task Classifier
↓
Context Loader
  ├─ working memory
  ├─ episodic memory
  ├─ semantic retrieval
  └─ policy context
↓
Planner Agent
↓
Execution Planner
  ├─ execution graph
  ├─ required tools
  ├─ required providers
  ├─ risk classes
  ├─ approval checkpoints
  └─ success criteria
↓
Authorization Gate
↓
Builder Agent / Tool Executor
↓
Observation Capture
↓
Verifier Agent
  ├─ syntactic checks
  ├─ semantic checks
  └─ environment checks
↓
Retry / Fallback / Re-plan
↓
Persist memory + logs + receipts + artifacts
↓
Final response
```

---

## 8. No-Cost Upgrades

These upgrades fit the architecture and do not require paid lock-in by default.

### 8.1 FastMCP

Use for:
- clean MCP server surfaces
- tools/resources/prompts exposure
- fast adapter implementation

Why:
- fastest no-cost path to an MCP bridge
- keeps MCP external to the brain core

### 8.2 Pydantic or Pydantic AI contract discipline

Use for:
- schemas
- validation
- typed outputs
- fail-closed parsing

Why:
- highest reliability improvement per effort

### 8.3 Langfuse self-hosted

Use for:
- traces
- evals
- run comparison
- failure analysis
- prompt/perf diagnostics

Why:
- observability becomes real instead of ad hoc

### 8.4 LlamaIndex adapter

Use for:
- semantic retrieval
- indexed docs
- document/query adapters

Why:
- gives a clean retrieval layer without forcing the core brain to become a RAG framework

### 8.5 Qdrant or Weaviate OSS

Use for:
- semantic memory vector layer

Why:
- keeps structured memory separate from vector search
- preserves clean memory-plane separation

### 8.6 Ollama or vLLM local path

Use for:
- private tasks
- sensitive verification
- local fallback
- offline capability later

### 8.7 MCP Registry support

Use later for:
- discoverability
- publishing clean MCP surfaces
- external tool exposure without re-architecting the brain

---

## 9. Best No-Cost Build Order

Do not build everything at once.

### Phase 1 — Contracts and Control

Build first:
- schemas
- state machine
- risk taxonomy
- approval policy

### Phase 2 — Core Execution

Build next:
- planner / builder / verifier contract flow
- provider router
- tool registry
- receipts

### Phase 3 — Persistence

Build:
- working store
- episodic store
- memory writer
- trace store

### Phase 4 — Verification

Build:
- syntactic verification
- semantic verification
- environment verification
- retry manager
- fallback manager

### Phase 5 — Semantic Layer

Build:
- retrieval engine
- semantic store
- vector adapter

### Phase 6 — Integrations

Build last:
- MCP
- LlamaIndex
- Langfuse
- Ollama / vLLM
- n8n / Supabase

---

## 10. Immediate Build Priorities

If this blueprint is adopted, the first concrete docs to create are:

```text
docs/MASTER_AI_SYSTEM_V2.md
docs/SCHEMA_CONTRACTS.md
docs/RISK_TAXONOMY.md
docs/MEMORY_WRITE_POLICY.md
docs/EXECUTION_RECEIPTS.md
```

The first code to create is:

```text
app/schemas/
app/orchestrator/state_machine.py
app/policy/risk_engine.py
app/policy/approval_policy.py
app/providers/provider_router.py
app/tools/tool_contract.py
```

---

## 11. Hard Architectural Rules

1. No plane may become a monolith.
2. No agent may self-authorize risky execution.
3. No tool may execute without a declared contract.
4. No execution may be called “successful” without verification.
5. No memory layer may become an unfiltered dump.
6. No adapter may be required for the brain to remain coherent.
7. No browser or MCP action may bypass policy mediation.
8. No provider should be hardwired into the planner/builder/verifier roles.
9. No hidden state transition should exist outside the state machine.
10. No raw string handoff should exist where a typed schema is available.
11. No adapter, worker, or surface may own authoritative task state, approval state, memory promotion state, or final run disposition.
12. No prototype or donor code may enter the canonical core without a decision log entry, schema mapping, policy review, and verification criteria.

---

## 12. Final Verdict

This architecture is intended to produce a system that is:

- modular
- auditable
- approval-aware
- memory-layered
- provider-flexible
- tool-safe
- verification-driven
- integration-ready
- no-cost extensible

It is a backend brain, not a demo shell.

It is designed to scale from:
- local-first CLI operation
- to sovereign multi-provider, multi-tool, policy-mediated execution

---
