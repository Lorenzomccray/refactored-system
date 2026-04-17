# PHASE_1_ACCEPTANCE_CRITERIA

**Status:** Active Build Gate  
**Tier:** Build Docs (Tier 3)  
**Purpose:** Define the minimum evidence required to accept Phase 1 of the sovereign runtime spine.

---

## 1. Acceptance Philosophy

Phase 1 is accepted only by evidence.

Not by:
- plausible architecture talk
- passing demos without contracts
- agent narration about what “should” be true
- donor feature parity claims

Accepted means:
- the runtime spine exists
- its controls are enforceable
- its artifacts are replayable
- its outputs are auditable
- later execution/automation layers can be attached without weakening governance

---

## 2. Mandatory Acceptance Gates

## Gate A — Source Routing Is Real

### Requirement
The system must classify a task and resolve the correct source tier before planning or execution.

### Must demonstrate
- architecture questions route to canonical docs first
- runtime diagnosis routes to runtime truth first
- build/config questions route to build docs first
- donor pattern questions consult canonical + reference correctly
- unresolved conflicts escalate instead of being silently flattened

### Failure conditions
- uses reference docs as doctrine
- skips source resolution for high-impact tasks
- invents authority when no source is found
- cannot emit source attribution inputs

---

## Gate B — State Machine Is Explicit

### Requirement
The runtime lifecycle must be visible and typed.

### Must demonstrate
- transitions through intake → context load → plan → authorize → execute → observe → verify → persist → respond
- fail-closed path exists and is callable
- retries / replan are explicit states or transitions, not hidden recursion
- run state is inspectable after failure

### Failure conditions
- execution path is a hidden prompt blob
- no explicit fail-closed state
- retries occur without classification or trace

---

## Gate C — Approval Policy Cannot Be Bypassed

### Requirement
Every state-changing step must pass through risk classification and approval policy.

### Must demonstrate
- risk class is assigned per step
- at least the following classes are enforced: `READ_ONLY`, `LOCAL_WRITE`, `LOCAL_EXECUTION`, `EXTERNAL_API_CALL`, `DATABASE_MUTATION`, `BROWSER_AUTOMATION`, `CREDENTIAL_USE`, `IRREVERSIBLE`
- builder cannot self-authorize risky work
- tools cannot run outside the policy wrapper

### Failure conditions
- direct tool invocation by agents
- risk class inferred only informally
- approval logic exists only in documentation, not runtime path

---

## Gate D — Receipts Are Structured and Replayable

### Requirement
Meaningful actions must emit receipts with enough information to audit the run.

### Minimum receipt fields
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

### Must demonstrate
- receipts are emitted for at least one read-only path and one state-changing path
- receipts can be inspected after the run
- receipts distinguish observations from claims

### Failure conditions
- logs without structured receipts
- receipts missing approval or verification fields
- receipts cannot be tied back to source routing and plan ids

---

## Gate E — Verification Is Load-Bearing

### Requirement
No successful completion claim may bypass verification.

### Must demonstrate
- syntactic verification for schemas/artifacts
- semantic verification for plan/result alignment
- environment verification when state changes occur
- verifier output drives retry or fail-closed decision

### Failure conditions
- success set before verification
- verification reduced to one generic boolean
- environment-changing actions lack environment checks

---

## Gate F — Memory Write Policy Is Enforced

### Requirement
The system must not promote arbitrary content into durable memory.

### Must demonstrate
- working memory accepts temporary state
- episodic memory stores run outcomes and approvals
- semantic memory accepts only curated / validated artifacts
- procedural memory requires repeated success or explicit promotion logic
- raw transcripts and donor dumps are blocked from direct promotion

### Failure conditions
- semantic or procedural writes occur without policy checks
- transcripts are stored as canonical truth
- donor/reference material is promoted without validation

---

## Gate G — Adapter Boundary Is Clean

### Requirement
External capability must be attachable without becoming the brain.

### Must demonstrate
- tool contracts declare schema, risk, approval level, timeout, retry, verification method
- external integrations are represented as adapters or bridges
- the core can run without Manus, Tasklet, MCP breadth, or browser automation attached

### Failure conditions
- core depends on a single external framework to function
- donor runtime is copied into the core path
- adapter contract is absent or informal

---

## 3. Test Scenarios Required Before Acceptance

### Scenario 1 — Canonical architecture query
Input asks what the intended architecture is.
Expected outcome:
- canonical docs selected first
- no runtime execution attempted
- source attribution emitted

### Scenario 2 — Runtime diagnostic request
Input asks why a run failed.
Expected outcome:
- runtime truth selected first
- source conflict escalates if runtime and canonical differ
- receipts/logs used as evidence

### Scenario 3 — Low-risk read-only task
Input requests safe inspection.
Expected outcome:
- no approval gate triggered
- receipt still emitted
- verifier confirms success path

### Scenario 4 — Local write task
Input requests a state-changing local action.
Expected outcome:
- risk classified as `LOCAL_WRITE`
- approval path invoked or blocked per policy
- no direct execution without wrapper

### Scenario 5 — Memory promotion attempt
Input or system attempts to store a transcript or donor note as durable memory.
Expected outcome:
- blocked or downgraded by memory policy
- policy rationale recorded

### Scenario 6 — External adapter absent
A delegated producer or automation adapter is unavailable.
Expected outcome:
- core remains coherent
- task either narrows scope or fails closed
- no collapse of state machine or receipts

---

## 4. Risk Register for Phase 1

| Risk | Why It Matters | Control |
| :--- | :--- | :--- |
| Source drift | Wrong tier chosen means wrong answer | Enforce source router before planning |
| Approval theater | User thinks control exists when it does not | Make approval decisions runtime-bound and receipt-visible |
| Receipt theater | Logs mistaken for proofs | Define receipt schema and replay requirements |
| Memory pollution | Early bad memory poisons later reasoning | Enforce write gate before durable memory growth |
| Donor contamination | External systems begin defining the architecture | Keep donor material reference-only unless rewritten behind contracts |
| Hidden framework dependency | Core becomes replaceable only by one vendor or framework | Internal state machine and contracts remain canonical |
| Verification collapse | System claims success without reality checks | Make verifier output load-bearing |

---

## 5. Acceptance Evidence Package

Phase 1 should not be marked accepted until the following exist:

- code paths or stubs for each in-scope runtime component
- contract definitions for task, plan, approval, receipt, and memory record
- at least one demonstrable end-to-end governed run
- sample receipts from read-only and state-changing cases
- memory-policy decision examples
- documented failure example showing fail-closed behavior

---

## 6. Reject Conditions

Phase 1 must be rejected if any of the following is true:

- source routing exists only as prose
- state machine is not explicit
- approval policy can be bypassed
- tools run without declared contracts
- receipts are not structured
- verification is optional for successful completion
- semantic/procedural memory accepts unvalidated content
- donor runtime code is merged to “speed up” the build

---

## 7. Definition of Done

Phase 1 is done only when the sovereign governor is stronger than the capabilities beneath it.

That means the system can safely host future:
- Manus-class delegated execution
- Tasklet-class recurring automation
- broader MCP integrations
- browser/computer-use expansion

without losing:
- source-of-truth discipline
- operator control
- receipt-driven auditability
- memory hygiene
- modular architecture boundaries

If power increases but control weakens, Phase 1 is not complete.
