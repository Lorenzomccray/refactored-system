# PHASE_1_STEP_1_EXECUTION_CHECKLIST

**Status:** Active Build Checklist  
**Tier:** Build Docs (Tier 3)  
**Purpose:** Provide the smallest safe execution sequence and demonstration payloads for Phase 1 Step 1.

---

## Scope

This checklist applies only to:
- `Issue #4: Implement Phase 1 Step 1: typed schemas and source router skeleton`

It exists to keep Step 1 implementation bounded.

---

## Read first

- `docs/MASTER_AI_SYSTEM_V2.md`
- `docs/SOURCE_SYSTEM_BLUEPRINT.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/build/PHASE_1_SOVEREIGN_RUNTIME_SPINE.md`
- `docs/build/PHASE_1_ACCEPTANCE_CRITERIA.md`
- `docs/build/PHASE_1_IMPLEMENTATION_PROMPT.md`

---

## Implement in this order only

1. `app/schemas/task.py`
2. `app/schemas/source_resolution.py`
3. `app/orchestrator/task_classifier.py`
4. `app/orchestrator/source_router.py`
5. `app/orchestrator/context_loader.py`
6. minimal tests or test scaffolds for classification and routing

---

## Step 1 completion checklist

- [ ] `Task` schema exists and normalizes task input
- [ ] `SourceResolution` schema exists and can represent selected tier, consulted tiers, conflicts, escalation, confidence, and rationale
- [ ] task classifier can classify at minimum:
  - [ ] architecture
  - [ ] runtime
  - [ ] build
  - [ ] reference
  - [ ] external
- [ ] source router maps task class to preferred source tier
- [ ] source router can represent unresolved high-impact conflict without flattening it
- [ ] context loader remains minimal and does not introduce broad retrieval or donor merge logic
- [ ] no approvals logic added here
- [ ] no receipts implementation added here
- [ ] no memory promotion logic added here
- [ ] no browser/runtime integration breadth added here

---

## Required demonstration payloads

Before marking Step 1 complete, show at least:

1. one architecture query classification result
2. one runtime diagnostic classification result
3. one build/config classification result
4. one donor-pattern routing result showing canonical + reference treatment
5. one unresolved conflict object showing fail-closed or escalation state

---

## Explicit guardrail

Do not implement any of the following in this checklist scope:
- approvals execution
- tool execution wrappers
- receipts pipeline
- memory promotion or semantic/procedural writes
- browser automation breadth
- wider MCP integration
- donor runtime imports

This is the contract-and-routing slice only.

---

## Exit condition

Step 1 is complete only when a developer can:
- instantiate a task
- classify it
- route it to a preferred source tier
- represent conflict or escalation explicitly
- hand the structured result to later authorization / receipt / verification phases

If routing still lives only in prompt logic or untyped dictionaries, Step 1 is not complete.
