# DONOR_ADOPTION_MATRIX

**Status:** Accepted Reference  
**Tier:** Reference Lessons (Tier 4)  
**Purpose:** Classify external patterns and donor capabilities for adoption without allowing donor systems to override the sovereign repo-centered architecture.

---

## 1. Operating Rule

This project is a **merge + upgrade** effort, not a rewrite.

The sovereign repo-centered assistant remains the authority.
Donor systems may contribute:
- patterns
- subsystem ideas
- adapter shapes
- workflow designs
- observability and execution lessons

They may **not** become canonical truth.

In every case:
1. Canonical architecture docs define intended design.
2. Runtime truth defines current observed behavior.
3. Build docs define the next approved coding target.
4. Reference docs inform but do not authorize runtime changes.

---

## 2. Classification Model

### Core
Capabilities that must become sovereign, repo-native, and policy-governed.

### Adapter
Capabilities that should exist as replaceable integration layers or translation layers.

### External-Controlled
Capabilities that may remain outside the core so long as they are invoked through the sovereign governor, with explicit policy, receipts, and approval boundaries.

### Reject
Capabilities or practices that would weaken sovereignty, blur source-of-truth boundaries, or introduce unsafe autonomy.

---

## 3. Donor Adoption Matrix

| Donor / Capability Family | Candidate Patterns | Placement | Why | Guardrails | Next Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Manus-class autonomous execution** | planner / execution / verification split; deep research workflows; multi-step delegated task completion; polished deliverable generation | **External-Controlled** for execution and deliverables; **Adapter** for orchestration hooks | High-value delegated producer model, but should not become repo authority | Never let Manus outputs become canonical by default; all results must be reviewed, classified, and distilled into repo docs or bounded runtime changes | Build a delegated-execution adapter contract and review gate |
| **Tasklet-class workflow automation** | recurring tasks; natural-language workflow setup; tool-trigger orchestration; durable task continuity | **External-Controlled** for recurring automation; **Adapter** for workflow trigger bridge | Valuable for durable automation, but workflow state must not outrank canonical repo docs | Require operator-owned schedules, receipts, approval policy, and source routing before any workflow writes | Build automation adapter contract and recurring-task governance doc |
| **Gobii patterns** | agent continuity; budget / compaction instincts; browser-use style operation; productized dev-tool behavior | **Adapter** for durable orchestration patterns; **Reference only** for product behaviors | Useful source of design patterns, but runtime merge risk is high if copied directly | No blind runtime merges; extract only bounded contracts, state patterns, and UX/operator lessons | Write targeted extraction notes for continuity, compaction, and browser mediation |
| **OpenClaw patterns** | tool-rich local execution ideas; agent shell behaviors; computer-use ambitions | **Reference only** with selective **Adapter** extraction if proven safe | Historically high freeze/operational instability risk in your environment; useful more as cautionary donor than as direct base | Keep out of core runtime; reject unreviewed local orchestration and system-coupled behaviors | Extract only lessons on failure modes, not runtime base code |
| **sovereignty-MCP** | preflight checks; dedup checks; decision journaling; lesson tracking; worker dispatch; session persistence concepts | **Core** for preflight / receipt / decision logging concepts; **Adapter** for MCP exposure | These patterns align strongly with sovereign governance, but current implementation includes unsafe direct DB coupling and secret handling concerns | Rebuild behind typed contracts; remove hardcoded secrets; do not import donor runtime directly | Convert concepts into canonical contracts for preflight, dedup, receipt, and worker dispatch |
| **MCP official patterns** | server/client boundary; tool/resource separation; protocol-level interoperability; registry publishing; host-client mental model | **Adapter** and some **Core contract influence** | MCP is appropriate as a replaceable protocol boundary, not as the brain itself | Core must depend on internal contracts first, then expose MCP through adapter boundary | Formalize MCP adapter boundary in tool and integration contracts |
| **LangGraph / orchestration patterns** | stateful multi-step graph execution; explicit node transitions; resumability | **Adapter** with **Core influence** on state machine design | Useful for graph execution patterns, but external orchestration framework must not become hidden core | Internal state machine remains canonical; external graph frameworks are optional bridges | Keep internal state machine first; add optional graph adapter later |
| **LlamaIndex / RAG patterns** | retrieval pipelines; indexing; semantic search surfaces | **Adapter** | Useful for semantic retrieval, but the memory plane must remain curated and policy-governed | No dump-style ingestion into memory; semantic writes must follow memory policy | Add retrieval adapter after runtime spine exists |
| **Langfuse / observability patterns** | tracing, evals, cost tracking, run analytics | **Adapter** with **Core receipt alignment** | Valuable for observability and evaluation, but receipts and audit semantics must remain repo-defined | Canonical receipt model first, external observability second | Map canonical receipt fields to external traces later |
| **Browser/computer-use runtimes** | browser automation, UI interaction, fallback execution | **External-Controlled** behind strict policy | High capability, high risk | Require approval classes, sandboxing, receipts, and environment verification | Keep disabled by default until policy and receipt pipeline are real |

---

## 4. Explicit Reject List

The following are rejected regardless of donor source:

- blind donor runtime merges
- letting external tool state become canonical truth
- direct writes to canonical docs without approval and receipts
- uncontrolled long-term memory accumulation
- hidden autonomous retries that bypass policy
- hardcoded credentials or baked-in service secrets
- monolithic runtime blobs that collapse control, tools, memory, and providers into one layer
- product polish work that outruns control, contracts, and verification

---

## 5. Core Extraction Priorities

These are the highest-value donor-derived patterns to extract into the sovereign core:

1. **Preflight + dedup + warning surfaces** from sovereignty-MCP concepts
2. **Delegated producer model** from Manus-class execution
3. **Durable recurring workflow model** from Tasklet-class automation
4. **Protocol adapter discipline** from MCP official patterns
5. **State-machine explicitness** from graph-based orchestration systems

---

## 6. Adoption Decision Rule

A donor capability may move forward only if it passes all checks below:

- It strengthens the sovereign governor rather than replacing it
- It can be expressed as a contract, adapter, or bounded subsystem
- It does not outrank canonical architecture docs
- It does not require blind donor code merge
- It can emit receipts, traces, and verification artifacts
- It can be disabled or removed without collapsing the brain

If any answer is **no**, the capability remains reference-only or is rejected.

---

## 7. Output of This Matrix

This matrix should be used to drive:
- `docs/build/PHASE_1_SOVEREIGN_RUNTIME_SPINE.md`
- `docs/build/PHASE_1_ACCEPTANCE_CRITERIA.md`
- future ADRs for delegated execution, automation, memory writes, and adapter boundaries

It is a reference-classification artifact, not an authorization to merge donor runtime code.
