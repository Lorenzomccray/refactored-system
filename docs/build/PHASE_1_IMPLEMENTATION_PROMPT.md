# PHASE_1_IMPLEMENTATION_PROMPT

**Status:** Active Build Prompt  
**Tier:** Build Docs (Tier 3)  
**Purpose:** Provide the exact implementation prompt for the dev tool to execute Phase 1 of the sovereign runtime spine.

---

You are implementing Phase 1 of `Lorenzomccray/refactored-system`.

Operate as a reasoning-first, doc-first systems architect and implementation engineer.

## Mission

Implement the **sovereign runtime spine** only.

This is the smallest runtime slice that makes the system:
- authority-aware
- policy-mediated
- receipt-emitting
- memory-disciplined
- adapter-ready

This is **not** a rewrite.
This is **not** a donor-code merge.
This is **not** UI work.
This is **not** broad integration work.

You are building the governor that future Manus-class execution and Tasklet-class automation must pass through.

---

## Source-of-truth order

You must obey this source hierarchy:

1. Canonical architecture docs
2. Runtime truth
3. Build docs
4. Reference lessons
5. External registries

If sources conflict:
- canonical docs govern intended design
- runtime truth governs current observed state
- reference docs never override canonical docs

Do not use donor/runtime repos as authority.
Do not blindly merge donor code.

---

## Required repo docs to follow

Read and implement against these docs first:

- `docs/BUILD_ORDER.md`
- `docs/SOURCE_SYSTEM_BLUEPRINT.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/RISK_TAXONOMY.md`
- `docs/MEMORY_WRITE_POLICY.md`
- `docs/EXECUTION_RECEIPTS.md`
- `docs/reference/DONOR_ADOPTION_MATRIX.md`
- `docs/build/PHASE_1_SOVEREIGN_RUNTIME_SPINE.md`
- `docs/build/PHASE_1_ACCEPTANCE_CRITERIA.md`
- `docs/build/PHASE_1_IMPLEMENTATION_PROMPT.md`

Treat:
- `docs/build/PHASE_1_SOVEREIGN_RUNTIME_SPINE.md` as the build target
- `docs/build/PHASE_1_ACCEPTANCE_CRITERIA.md` as the gate
- `docs/reference/DONOR_ADOPTION_MATRIX.md` as boundary guidance, not runtime authority

---

## Build scope

Implement only these runtime components now:

### 1. Source Router / Authority Resolver
Required behaviors:
- classify tasks into architecture / runtime / build / reference / external
- resolve preferred source tier
- escalate on source conflict
- fail closed on unresolved high-impact source conflict
- produce source attribution inputs

Target files:
- `app/orchestrator/task_classifier.py`
- `app/orchestrator/context_loader.py`
- `app/orchestrator/source_router.py`
- `app/schemas/task.py`
- `app/schemas/source_resolution.py`

### 2. Governor State Machine
Required behaviors:
- explicit lifecycle:
  - intake
  - context_load
  - plan
  - authorize
  - execute
  - observe
  - verify
  - persist
  - respond
  - fail_closed
- explicit retry / replan transitions
- inspectable run state after failure

Target files:
- `app/orchestrator/state_machine.py`
- `app/orchestrator/loop_manager.py`
- `app/orchestrator/execution_planner.py`
- `app/schemas/execution_graph.py`

### 3. Risk + Approval Service
Required behaviors:
- classify every planned step by risk
- enforce at least:
  - `READ_ONLY`
  - `LOCAL_WRITE`
  - `LOCAL_EXECUTION`
  - `EXTERNAL_API_CALL`
  - `DATABASE_MUTATION`
  - `BROWSER_AUTOMATION`
  - `CREDENTIAL_USE`
  - `IRREVERSIBLE`
- no builder/tool bypass

Target files:
- `app/policy/risk_engine.py`
- `app/policy/approval_policy.py`
- `app/policy/action_constraints.py`
- `app/orchestrator/approvals.py`
- `app/schemas/approval_request.py`
- `app/schemas/approval_decision.py`

### 4. Tool Contract + Receipt Wrapper
Required behaviors:
- every action goes through declared contracts
- receipts include:
  - run id
  - task id
  - plan id
  - step id
  - source attribution
  - risk class
  - approval decision or bypass rationale
  - tool/provider used
  - result summary
  - verifier result
  - timestamp

Target files:
- `app/tools/tool_contract.py`
- `app/tools/tool_registry.py`
- `app/tools/tool_authz.py`
- `app/tools/tool_receipts.py`
- `app/telemetry/run_receipts.py`
- `app/telemetry/trace_store.py`
- `app/verification/receipt_checker.py`
- `app/schemas/tool_call.py`
- `app/schemas/tool_result.py`
- `app/schemas/run_receipt.py`
- `app/schemas/verification_result.py`

### 5. Memory Write Gate
Required behaviors:
- separate:
  - working memory
  - episodic memory
  - semantic memory
  - procedural memory
- block raw transcript dumping
- block donor/reference promotion without validation
- require explicit policy for semantic/procedural writes

Target files:
- `app/memory/memory_policy.py`
- `app/memory/memory_writer.py`
- `app/memory/promotion_rules.py`
- `app/schemas/memory_record.py`

### 6. Adapter Contract Boundary
Required behaviors:
- declare capability, schema, risk, approval level, timeout, retry, verification method
- allow future Manus / Tasklet / MCP integration only behind contracts
- core must remain coherent if adapters are removed

Target files:
- `app/integrations/mcp/` contract-first only
- no broad implementation fan-out yet

---

## Out of scope

Do not implement these in this task:
- UI/dashboard/operator console
- full browser/computer-use autonomy
- recurring workflow scheduler
- generalized RAG stack
- full external integration fan-out
- donor runtime imports from Gobii, OpenClaw, or sovereignty-MCP
- broad provider optimization
- semantic retrieval expansion
- uncontrolled agent autonomy

---

## Required implementation order

Follow this sequence exactly:

1. typed schemas
2. source router + context loader
3. governor state machine skeleton
4. risk engine + approval policy
5. tool contracts + receipt wrapper
6. verification handshake
7. memory write gate

Do not skip ahead.

---

## Acceptance targets

Your implementation is only acceptable if it can demonstrate:

### Scenario 1
A canonical architecture query:
- routes to canonical docs first
- emits source attribution
- performs no risky execution

### Scenario 2
A runtime diagnostic request:
- routes to runtime truth first
- escalates conflict with canonical if needed
- uses receipts/logs as evidence

### Scenario 3
A low-risk read-only task:
- triggers no approval
- still emits a receipt
- passes verification

### Scenario 4
A local write task:
- is classified as `LOCAL_WRITE`
- cannot execute without approval logic
- cannot bypass wrapper

### Scenario 5
A memory promotion attempt from transcript/reference content:
- is blocked or downgraded by policy
- records rationale

### Scenario 6
A missing external adapter:
- does not collapse the core
- fails closed or narrows scope safely

---

## Non-negotiable rules

- Do not claim success without verification
- Do not create theatrical placeholder architecture and call it done
- Do not merge donor code
- Do not let tools run outside policy mediation
- Do not let receipts degrade into unstructured logs
- Do not let memory writes bypass policy
- Do not let external frameworks become the hidden core
- Do not expand scope beyond Phase 1 runtime spine

---

## Engineering standards

- Use explicit typed schemas
- Keep modules small and composable
- Prefer deterministic control flow over prompt-only behavior
- Add concise comments only where needed to clarify control boundaries
- Write tests or test scaffolds for critical decision paths
- Favor fail-closed behavior
- Prefer internal contracts over framework magic

---

## Required output format

Return your work in this exact structure:

1. `REQUESTED`
   - restate the Phase 1 implementation goal

2. `SOURCES USED`
   - list the repo docs used
   - note any conflicts found

3. `PLAN`
   - smallest safe implementation sequence

4. `CHANGED FILES`
   - every created/updated file
   - one-line purpose per file

5. `IMPLEMENTATION NOTES`
   - important design decisions
   - why they align with repo doctrine

6. `TEST / VERIFICATION`
   - what scenarios were validated
   - what passed
   - what remains unverified

7. `RISKS / GAPS`
   - anything incomplete or intentionally deferred

8. `NEXT SAFE STEP`
   - the next bounded implementation slice after this one

If you cannot complete a file, say exactly why.
If repo reality differs from docs, report the mismatch explicitly.
If a decision is ambiguous, choose the smallest safe option that preserves the sovereign spine.

---

## Tracking

Primary execution issue:
- `#3 Implement Phase 1 sovereign runtime spine`

This prompt exists to keep the implementation instruction inside the repo's build layer rather than only in external chat history.
