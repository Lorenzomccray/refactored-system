# GOBII_LESSONS

## Purpose

This document captures what `gobii` teaches the `refactored-system` project without turning `gobii` into canonical architecture.

It exists to separate:
- valuable design patterns
- reusable implementation ideas
- non-portable product assumptions
- high-risk or license-sensitive behavior

This is a **reference lessons** file, not architecture truth.

Canonical architecture still lives in:
- `docs/MASTER_AI_SYSTEM_V2.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/RISK_TAXONOMY.md`
- `docs/MEMORY_WRITE_POLICY.md`
- `docs/EXECUTION_RECEIPTS.md`

---

## Source Basis

This lessons file is based on the uploaded Gobii blueprint and extracted repo observations. The inspected material shows `gobii` as a Django-based persistent agent platform with a dynamic prompt/context builder, tool modules, browser actions, billing/credit logic, model failover, and durable session state. fileciteturn53file1 fileciteturn53file0

---

## What Gobii Appears To Be Good At

Gobii’s strongest visible qualities are:

1. **Persistent agent runtime**
   - It maintains long-lived agent state, messages, steps, tool calls, and attachments. fileciteturn53file1

2. **Prompt/context assembly discipline**
   - It pulls together messages, files, tool summaries, budgets, variables, and historical context into one runtime prompt stack. fileciteturn53file1

3. **Budget and usage controls**
   - It tracks task credits, plans, and runtime limits rather than pretending all agent work is free. fileciteturn53file0

4. **Model routing and failover**
   - It uses tiering, retries, and fallback logic instead of a single brittle provider path. fileciteturn53file1

5. **History compaction**
   - It compresses/summarizes history to stay inside token budgets. fileciteturn53file1

6. **Modular tool surfaces**
   - It has tools and browser actions separated into modules rather than one giant tool blob. fileciteturn53file1

---

## Lessons Worth Reusing

### 1. Treat prompt assembly as a real subsystem

Gobii’s prompt construction is not a single static system prompt. It behaves more like a structured context loader that merges:
- recent messages
- prior steps
- file state
- tool summaries
- budget state
- variables/configuration
- historical context windows fileciteturn53file1

#### What to reuse
For `refactored-system`, this should become:
- `app/orchestrator/context_loader.py`
- `app/memory/retrieval_engine.py`
- `app/agents/researcher_agent.py`
- `app/telemetry/artifact_store.py`

#### Rule
Do not copy Gobii’s prompt stack directly. Rebuild the idea around your typed contracts and state machine. The canonical architecture already requires explicit context loading before planning/execution. fileciteturn53file9

---

### 2. Session persistence is a first-class system requirement

Gobii demonstrates that durable agent systems need more than transient chat history. It persists agent records, message history, step history, and snapshots across runs. fileciteturn53file1

#### What to reuse
Adopt the principle that:
- runs must survive restart
- steps must be replayable
- history must be queryable
- artifacts must be referenceable

#### Where it belongs in `refactored-system`
- `app/memory/working_store.py`
- `app/memory/episodic_store.py`
- `app/telemetry/trace_store.py`
- `app/telemetry/run_receipts.py`

This aligns directly with the memory plane and observability plane already defined in the master architecture. fileciteturn53file9

---

### 3. Compaction is necessary, not optional

Gobii appears to use summarization and compaction to keep long-lived runs within token budgets. fileciteturn53file1

#### What to reuse
Create explicit compaction policy for:
- message history
- tool-call history
- browser history
- step summaries
- internal notes

#### Required adaptation
In `refactored-system`, compaction must be:
- policy-aware
- receipt-linked
- separated from semantic memory promotion
- never treated as canonical truth by default

That separation is already required by the memory write policy and execution receipt model. fileciteturn53file9

---

### 4. Budget and cost control should exist early

Gobii surfaces the reality that persistent agents need cost governance, retry control, and usage enforcement. It exposes limits, retries, and plan/credit logic. fileciteturn53file0

#### What to reuse
Even if `refactored-system` starts as a no-cost local-first build, add:
- per-step cost estimates
- retry ceilings
- model routing cost hints
- task-level budget context
- provider health checks

#### Where it belongs
- `app/providers/cost_policy.py`
- `app/providers/provider_health.py`
- `app/orchestrator/retry_manager.py`
- `app/policy/model_tool_matrix.py`

---

### 5. Tool registration should be explicit

Gobii’s modular tool layout is a useful lesson: tools should be defined as separate modules and enabled through runtime logic, not improvised ad hoc. fileciteturn53file1

#### What to reuse
For `refactored-system`, every tool should be:
- declared
- typed
- risk-classified
- authorization-gated
- receipt-producing
- verifier-compatible

That is already the required rule in the tool plane. Gobii reinforces that this needs real registration and enablement logic, not just callable Python functions. fileciteturn53file9

---

### 6. Failover routing is a production necessity

Gobii’s tiered LLM configuration and failover logic reinforce an important architectural point: the planner/builder/verifier stack should not depend on a single model or provider. fileciteturn53file1

#### What to reuse
Use provider routing that supports:
- primary model selection by role
- fallback chain by failure type
- retry with narrowed context
- tier-aware token budgets
- provider health awareness

This maps directly to the provider plane and fallback chain already defined for `refactored-system`. fileciteturn53file9

---

## What Not To Reuse Directly

### 1. Product-specific billing and plan assumptions

Gobii contains community/proprietary toggles and billing/credit behavior. Those are product/business decisions, not core brain architecture. fileciteturn53file0

#### Rule
Do not let donor billing logic define the core system model.

Only reuse the abstract lesson:
- usage needs governance
- retries/costs need ceilings

---

### 2. Browser actions that cross into unsafe territory

The extracted materials show browser automation modules including CAPTCHA solving and file upload/download automation. fileciteturn53file0

#### Rule
These patterns are **high-risk** and should not be ported directly.

For `refactored-system`:
- browser actions must remain behind explicit approval
- no anti-bot circumvention logic should become a default capability
- browser actions must be isolated, auditable, and policy-classified as `BROWSER_AUTOMATION`

This matches the risk taxonomy requirement that browser automation is a high-risk surface needing policy mediation. fileciteturn53file9

---

### 3. Giant prompt-context blobs as hidden orchestration

Gobii’s runtime appears prompt-heavy. That can be effective, but it can also hide system logic inside assembly code rather than explicit contracts. fileciteturn53file1

#### Rule
Do not import a donor system’s prompt complexity as your orchestration model.

In `refactored-system`:
- planning belongs in planner outputs
- execution belongs in execution graphs
- authorization belongs in policy decisions
- verification belongs in verifier outputs

Never substitute prompt cleverness for typed control-plane logic.

---

### 4. Django-specific platform assumptions

Gobii is structured as a Django web platform. `refactored-system` is not obligated to inherit that application shape.

#### Rule
Do not import:
- Django ORM assumptions
- Django app boundaries
- web product routing patterns
- platform-specific lifecycle constraints

Only reuse architecture lessons that survive framework change.

---

## Classification of Gobii Ideas

### Adopt now
- context loading as a real subsystem
- history compaction as a first-class concern
- provider failover principles
- modular tool registration
- durable session/run persistence
- budget/cost awareness

### Rewrite later
- file/message snapshot strategies
- model tiering logic
- detailed context-window trimming
- budget manager abstractions

### Reference only
- Django app layout
- product plan enforcement
- UI/platform coupling
- proprietary/community business toggles

### Reject
- anti-bot circumvention as a default system capability
- browser automation without strict policy gating
- hidden orchestration logic buried inside prompt assembly

---

## Clean Extraction Targets For `refactored-system`

If you mine Gobii carefully, extract only these kinds of patterns:

1. **Context builder patterns**
   - how to gather runtime state before planning

2. **Compaction triggers**
   - when to summarize older history

3. **Tier/fallback routing ideas**
   - how to switch providers when a path fails

4. **Session/state durability ideas**
   - how to persist steps, results, and resumable runs

5. **Tool catalog structure**
   - how to keep tool definitions modular

---

## Mapping Into Canonical Architecture

### Gobii lesson → `refactored-system` target

| Gobii lesson | Canonical destination |
|---|---|
| Dynamic prompt/context assembly | `app/orchestrator/context_loader.py` |
| Long-lived agent persistence | `app/memory/working_store.py`, `app/memory/episodic_store.py` |
| History compaction | `app/memory/summarizer.py`, `app/memory/promotion_rules.py` |
| Tiered model failover | `app/providers/routing_policy.py`, `app/providers/fallback_policy.py` |
| Tool modularization | `app/tools/tool_registry.py`, `app/tools/tool_contract.py` |
| Usage controls | `app/providers/cost_policy.py`, `app/policy/model_tool_matrix.py` |

---

## Final Lesson

Gobii’s strongest contribution is not a single file or framework choice.

Its strongest contribution is this:

> persistent agents need disciplined context assembly, durability, compaction, modular tooling, and provider failover.

Those ideas are worth keeping.

What should **not** be copied is the product-specific, Django-specific, or high-risk browser behavior as-is.

Use Gobii as a donor of patterns.
Do not let it become hidden architecture.
