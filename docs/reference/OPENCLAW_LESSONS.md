# OPENCLAW_LESSONS

## Purpose

This document records what `openclaw` can teach `refactored-system` without allowing a donor runtime to redefine the canonical architecture.

It separates:
- valuable operator-assistant patterns
- reusable local-first ideas
- packaging and runtime lessons
- non-canonical assumptions that should remain external

This is a **reference lessons** document, not architecture truth.

Canonical truth remains in:
- `docs/MASTER_AI_SYSTEM_V2.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/RISK_TAXONOMY.md`
- `docs/MEMORY_WRITE_POLICY.md`
- `docs/EXECUTION_RECEIPTS.md`

The source-system rules explicitly place this file in the reference-doc tier, below canonical architecture. fileciteturn53file8

---

## Source Basis

The project’s repo options and source plan already classify OpenClaw as a donor/reference repo, not a merge target. The current project artifacts also explicitly keep external systems and adapters outside the brain core. fileciteturn53file10 fileciteturn53file8

---

## What OpenClaw Is Most Likely Useful For

Based on the current project context, OpenClaw is useful less as architecture truth and more as a donor for:
- local-first assistant operating patterns
- continuous operator-presence ergonomics
- daemon/background-assistant packaging ideas
- developer-facing assistant workflow patterns
- real-world “assistant lives with the machine” product feel

That makes it a strong donor for **interaction model** and **runtime presence**, but not a reason to weaken the typed control-plane architecture in `refactored-system`.

---

## Lessons Worth Reusing

### 1. The assistant should feel resident, not episodic

One of the most valuable OpenClaw-style lessons is that a useful assistant often feels like an always-present operator companion instead of a stateless request/response tool.

#### What to reuse
For `refactored-system`, adopt the principle that the brain should support:
- resumable runs
- persistent working context
- durable episodic history
- recent-environment awareness
- operator continuity between sessions

#### Where it belongs
- `app/memory/working_store.py`
- `app/memory/episodic_store.py`
- `app/orchestrator/context_loader.py`
- `app/telemetry/trace_store.py`

This is fully consistent with the master architecture’s memory and observability planes. fileciteturn53file9

---

### 2. Local-first matters for trust and privacy

OpenClaw’s value to this project is strongly tied to local-first operator behavior.

#### What to reuse
Prefer designs where:
- sensitive tasks can route locally
- the system can remain coherent if cloud providers fail
- local tools are first-class citizens
- local state and artifacts stay inspectable

#### Where it belongs
- `app/providers/local_provider.py`
- `app/providers/routing_policy.py`
- `app/policy/secrets_policy.py`
- `app/tools/shell_tool.py`
- `app/tools/file_tool.py`

This also aligns with the provider-plane rule that sensitive/private work should use a local path when available. fileciteturn53file9

---

### 3. Presence should be separated from cognition

A donor system may have a good UX feeling because it appears ever-present, but that presence should not be confused with the brain itself.

#### What to reuse
Take the product lesson:
- presence is useful
- sidecar/daemon patterns are useful
- operator continuity is useful

#### But preserve this rule
In `refactored-system`, presence must remain:
- an adapter concern
- a shell/daemon/interface concern
- not the control plane itself

The master architecture already says the integration layer remains external-facing and adapters must not become the core brain. fileciteturn53file9

---

### 4. Packaging and service ergonomics matter

OpenClaw-style systems often teach that a good assistant is not only intelligent but operationally convenient.

#### What to reuse
Design for:
- easy startup
- clean restart behavior
- service/daemon compatibility
- durable logs and receipts
- safe operator control points

#### Where it belongs
- `app/core/lifecycle.py`
- `scripts/`
- service wrappers outside the core brain
- `app/telemetry/logger.py`
- `app/telemetry/run_receipts.py`

This complements the execution-receipt model and the observability plane. fileciteturn53file9

---

### 5. Assistant UX should not require architectural compromise

A donor may deliver a compelling operator experience by hiding complexity, but the lesson for `refactored-system` is not to hide control-plane logic inside convenience wrappers.

#### What to reuse
Use OpenClaw as proof that:
- convenience matters
- low-friction operation matters
- assistant continuity matters

#### What not to do
Do not let “helpful assistant feel” justify:
- skipping approvals
- skipping receipts
- skipping verifier outputs
- hiding state transitions
- burying orchestration in informal runtime behavior

That would violate the canonical architecture directly. fileciteturn53file9

---

## What Not To Reuse Directly

### 1. Any donor runtime as the control plane

OpenClaw must not become the hidden orchestrator of `refactored-system`.

#### Rule
No donor repo gets to define:
- the state machine
- the schema contracts
- the risk taxonomy
- the receipt model
- memory promotion policy

Those are already defined canonically. fileciteturn53file9

---

### 2. UX-first shortcuts that weaken auditability

Some assistant products optimize for smoothness by hiding internal transitions.

#### Rule
`refactored-system` must remain:
- replayable
- inspectable
- receipt-backed
- policy-mediated

Never sacrifice auditability for “it feels smooth.”

---

### 3. Product-specific workflow assumptions

OpenClaw may have assumptions about:
- how users initiate tasks
- where files live
- how background runtime works
- how tools are exposed
- how the assistant surfaces results

#### Rule
Keep those as optional adapter ideas only.

Do not let them become canonical repo shape or runtime law.

---

### 4. Hardwired interface coupling

A donor system may bind tightly to a specific shell, GUI, extension, or packaging model.

#### Rule
In `refactored-system`, interface/presence layers must stay replaceable.

The core brain must still make sense if the outer shell changes.

That is exactly what the integration-plane adapter rule requires. fileciteturn53file9

---

## Classification of OpenClaw Ideas

### Adopt now
- local-first preference for sensitive/private work
- assistant continuity as a system goal
- presence as a useful external layer
- service ergonomics and clean lifecycle handling

### Rewrite later
- daemon/service wrappers
- shell-side operator workflows
- background task presentation patterns
- assistant-presence interaction surfaces

### Reference only
- product-specific workflow assumptions
- branding/UX packaging ideas
- interface-specific control surfaces

### Reject
- any shortcut that bypasses approval, receipts, or verification
- any hidden orchestration that competes with the state machine
- any coupling that makes the core dependent on one interface shell

---

## Clean Extraction Targets For `refactored-system`

Mine OpenClaw only for these kinds of patterns:

1. **Presence patterns**
   - how a system can feel continuously available

2. **Local-first operating patterns**
   - how sensitive work can stay close to the machine

3. **Lifecycle/daemon patterns**
   - how a system starts, restarts, and remains manageable

4. **Operator ergonomics**
   - how to reduce friction without weakening control

---

## Mapping Into Canonical Architecture

| OpenClaw lesson | Canonical destination |
|---|---|
| Persistent assistant feel | `app/memory/working_store.py`, `app/orchestrator/context_loader.py` |
| Local-first trust path | `app/providers/local_provider.py`, `app/policy/secrets_policy.py` |
| Service ergonomics | `app/core/lifecycle.py`, `scripts/` |
| Replaceable interface layer | `app/integrations/` adapters only |
| Operator continuity | `app/memory/episodic_store.py`, `app/telemetry/trace_store.py` |

---

## Final Lesson

OpenClaw’s best value to `refactored-system` is not as a codebase to absorb.

Its best value is as a reminder that:

> a strong assistant should feel resident, local-capable, low-friction, and continuous — while still remaining policy-aware, auditable, and architecturally clean.

Use OpenClaw as a donor for operator experience and local-first runtime patterns.
Do not let it replace the typed backend brain.
