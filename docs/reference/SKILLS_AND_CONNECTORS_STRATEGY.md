# SKILLS_AND_CONNECTORS_STRATEGY

**Status:** Accepted Reference  
**Tier:** Reference Lessons (Tier 4)  
**Purpose:** Define which external skill sources and app connectors most improve the assistant's ability to develop `refactored-system` without weakening the repo-centered source-of-truth model.

---

## 1. Why this document exists

The project already has a strong doctrinal architecture:
- source-tiered truth
- doc-first governance
- typed contracts
- approval and verification requirements
- adapters instead of monoliths

But the current runtime is still materially simpler than the target sovereign brain.

That means the best external additions are not random "AI agent" sources.
They are the sources and connectors that improve:
1. contracts
2. routing
3. policy
4. receipts and observability
5. memory discipline
6. bounded integrations

---

## 2. Current gap summary

### What the project already has
- repo-centered architecture doctrine
- phased build order
- donor adoption controls
- Phase 1 runtime-spine planning artifacts
- issue chain for bounded runtime implementation

### What the project still lacks at runtime
- typed schema layer enforcement
- source router implementation
- explicit state machine runtime
- enforceable approval path
- structured receipt pipeline
- memory write gate implementation
- clean adapter boundaries in code

### Consequence
Sources and connectors should be selected primarily for helping implement those missing runtime layers.

---

## 3. Skill families to prioritize

## 3.1 Contract and schema discipline

### Why
The architecture depends on typed contracts between every plane.

### Best source categories
- Pydantic / Python validation docs
- JSON Schema / OpenAPI references
- contract-first API design references

### Use in this project
- `Task`
- `SourceResolution`
- `Plan`
- `ExecutionGraph`
- `ApprovalDecision`
- `RunReceipt`
- `MemoryRecord`

### Recommendation
This is the highest-value skill family and should be treated as mandatory.

---

## 3.2 State-machine and orchestration discipline

### Why
The target architecture requires explicit execution states and fail-closed transitions.

### Best source categories
- state machine design references
- graph orchestration references
- retry / fallback / resumability patterns

### Use in this project
- `state_machine.py`
- `loop_manager.py`
- execution lifecycle
- retry / re-plan discipline

### Recommendation
Use external graph/orchestration frameworks as pattern references or adapters, never as hidden core truth.

---

## 3.3 Policy, approval, and bounded autonomy

### Why
The project's advantage over generic agents is controlled autonomy.

### Best source categories
- policy-as-code references
- risk engine patterns
- approval-gate patterns
- action classification and fail-closed design

### Use in this project
- `risk_engine.py`
- `approval_policy.py`
- `action_constraints.py`
- tool authorization wrappers

### Recommendation
This is a core differentiator and must outrank broader execution power.

---

## 3.4 Receipts, observability, and evaluation

### Why
The system doctrine requires traces, receipts, and replayable evidence.

### Best source categories
- tracing systems
- evaluation frameworks
- logging and telemetry references
- run comparison / failure analysis tools

### Use in this project
- `run_receipts.py`
- `trace_store.py`
- `receipt_checker.py`
- failure and approval logs

### Recommendation
Prioritize observability sources that support structured runs, not only prompt analytics.

---

## 3.5 Memory discipline and retrieval

### Why
The target architecture requires four memory layers and explicit promotion rules.

### Best source categories
- curated semantic retrieval systems
- vector store docs
- memory write-policy patterns
- retrieval adapters

### Use in this project
- working / episodic / semantic / procedural memory split
- retrieval engine
- promotion rules
- memory write gate

### Recommendation
Do not add sources that encourage raw dump ingestion or unconstrained memory.

---

## 3.6 MCP and adapter boundaries

### Why
The project wants broad capability without turning protocol layers into the brain.

### Best source categories
- MCP protocol docs
- FastMCP patterns
- tool/resource separation docs
- server/client boundary docs

### Use in this project
- `mcp_tool.py`
- `app/integrations/mcp/`
- future external tool exposure

### Recommendation
Treat MCP as a transport and integration boundary, not the source of system doctrine.

---

## 3.7 Browser and computer-use references

### Why
Useful later for execution breadth, but risky if brought in too early.

### Best source categories
- Playwright docs
- browser automation patterns
- browser policy and sandboxing references

### Use in this project
- browser tool plane
- environment verification
- later delegated producer behavior

### Recommendation
Important, but only after policy, receipts, and routing exist.

---

## 3.8 Workflow automation and durable tasking

### Why
Tasklet-class capability depends on recurring workflows and durable task continuity.

### Best source categories
- workflow engines
- automation platforms
- durable execution patterns
- scheduling and retry systems

### Use in this project
- automation adapter
- recurring task engine
- later external-controlled execution layer

### Recommendation
Connect only after the sovereign runtime spine is real.

---

## 4. Highest-value external skill sources to add

These are the best source categories for the project.

## Tier A — Add immediately

1. **Pydantic docs**
   - contracts, validation, typed schemas
2. **Model Context Protocol official docs / servers**
   - protocol boundaries, tool/resource patterns
3. **LlamaIndex docs**
   - retrieval adapter patterns, not core-brain replacement
4. **Langfuse docs**
   - traces, evals, run comparison, observability
5. **Playwright Python docs**
   - browser execution and verification patterns
6. **Supabase docs**
   - durable storage / auth / data modeling references
7. **n8n docs**
   - external automation adapter patterns

## Tier B — Add after Phase 1 runtime spine starts landing

8. **Ollama docs**
   - local provider path
9. **vLLM docs**
   - higher-throughput local model serving
10. **Qdrant docs**
   - vector-memory adapter layer
11. **Weaviate docs**
   - alternative vector-memory adapter layer
12. **Temporal docs**
   - durable workflow and retry patterns
13. **OpenTelemetry / structured tracing docs**
   - portable telemetry and receipts alignment

## Tier C — Keep as reference only unless explicitly needed

14. broad general agent-framework blogs
15. donor-runtime repositories with weak boundaries
16. product-marketing pages without implementation detail

---

## 5. Connector and app priority

## 5.1 Primary execution connector

### GitHub

#### Why
GitHub is the canonical execution surface for this project.

#### Use for
- repo docs
- issues
- PRs
- code review
- CI checks
- source of truth for accepted implementation

#### Priority
**Mandatory**

---

## 5.2 High-value project-memory connectors

### Google Drive / Google Docs / Google Sheets

#### Why
Useful for research artifacts, source packs, planning sheets, and structured working docs.

#### Best use
- ingest design notes
- read planning docs
- compare work products
- avoid re-upload friction

### Notion

#### Why
Useful for design memory, long-form narrative notes, and organized project knowledge.

#### Best use
- design narratives
- structured knowledge maps
- planning summaries that link back to canonical GitHub docs

### Slack

#### Why
Useful only if the project actually uses Slack for decisions or execution coordination.

#### Best use
- triage summaries
- thread retrieval
- connector-aware task context

#### Warning
Slack should not become the source of truth for decisions.

---

## 5.3 Operational connectors

### Gmail

#### Why
Useful for project coordination, external communications, signup flows, verification emails, and draft/send support.

### Google Calendar

#### Why
Useful for milestone planning, meetings, and later approval/review loops.

### Google Contacts

#### Why
Useful when project execution involves outreach, collaborators, or calendar/email routing.

---

## 5.4 Delegated production connector

### Manus

#### Why
Best used as delegated research / deliverable generation / prototype production.

#### Best role
- wide research
- polished docs/slides/site drafts
- comparative analysis

#### Hard rule
Manus outputs are never canonical by default.
They must be reviewed and distilled into repo-native artifacts.

---

## 5.5 Internal automation connector

### Scheduled tasks / automations

#### Why
Useful later for recurring checks:
- repo health
- CI reminders
- issue follow-ups
- external monitoring tasks

#### Priority
Medium now, high later.

---

## 6. Connector usage by system plane

| Plane | Best connectors / apps | Why |
| :--- | :--- | :--- |
| Control plane | GitHub | issues, PRs, canonical execution artifacts |
| Cognition plane | GitHub + reference sources | grounded reasoning against repo doctrine |
| Memory plane | Drive, Notion, GitHub, Supabase docs | curated retrieval and durable reference |
| Tool plane | MCP sources, Playwright docs, GitHub | tool contracts and implementation references |
| Provider plane | Ollama, vLLM, provider docs | local and multi-provider routing references |
| Policy plane | GitHub docs, governance sources | runtime law and approval constraints |
| Verification plane | Langfuse, OpenTelemetry, Playwright | traces, receipts, checks |
| Integration plane | MCP, n8n, Supabase, Drive, Notion, Gmail, Calendar | bounded adapters |

---

## 7. Best order to connect apps

1. **GitHub**
2. **Google Drive / Docs / Sheets**
3. **Notion**
4. **Gmail**
5. **Google Calendar**
6. **Google Contacts**
7. **Slack** (only if truly used for project work)
8. **Manus** as delegated producer, not authority

---

## 8. What not to optimize too early

Do not spend early effort on:
- broad browser autonomy
- generalized workflow automation
- high-volume integrations
- vector stacks before memory policy
- donor runtime imports
- product polish before runtime law

These are secondary to Phase 1 runtime-spine implementation.

---

## 9. Final recommendation

If the goal is to maximize the assistant's ability to fully develop this project, the best stack is:

### Core execution
- GitHub

### Best source additions
- Pydantic
- MCP official docs / servers
- LlamaIndex
- Langfuse
- Playwright
- Supabase
- n8n

### Next-wave sources
- Ollama
- vLLM
- Qdrant or Weaviate
- Temporal
- OpenTelemetry

### Rule
Every source or connector must strengthen one of the missing runtime layers.
If it does not help contracts, routing, policy, receipts, memory, or adapter boundaries, it is not a priority.
