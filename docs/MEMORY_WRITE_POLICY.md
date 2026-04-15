# MEMORY_WRITE_POLICY
## What Gets Stored, Where, and When

---

## 1. Purpose

This document defines what information may be written into each memory layer.

Without a write policy, memory turns into:
- noise
- contradictions
- unbounded logs disguised as memory
- low-trust retrieval
- accidental secret retention

Memory must be selective, typed, and promotion-driven.

---

## 2. Memory Layers

The system has four memory layers:

1. Working Memory
2. Episodic Memory
3. Semantic Memory
4. Procedural Memory

Each layer has a different retention model and write rule.

---

## 3. Working Memory

### Purpose
Short-lived state for the active run.

### May store
- current task
- current plan graph
- latest observations
- recent tool outputs
- current verifier outputs
- temporary scratch summaries
- transient context references

### Must not store
- secrets in plain text
- unbounded conversation history
- arbitrary raw dumps
- promoted long-term truths

### Retention
- prune aggressively
- clear at run completion unless explicitly promoted
- safe to rebuild from episodic/semantic records where needed

---

## 4. Episodic Memory

### Purpose
Durable record of completed runs, failures, approvals, and outcomes.

### Must store
- run summaries
- plan ids and run ids
- approval decisions
- failure classes
- retries and fallback events
- key operator interventions
- final artifacts or references
- verifier outcomes

### Should store
- why a run failed
- why a recovery path succeeded
- what approval constraints were added
- what changed in the environment

### Must not store
- giant raw logs without summarization
- secret values
- duplicate copies of everything already in artifact storage

### Retention
- durable
- queryable by task, run id, failure class, and date

---

## 5. Semantic Memory

### Purpose
Retrievable knowledge store for useful facts, validated docs, and reusable project knowledge.

### May store
- validated architecture decisions
- important design notes
- extracted repo truths
- indexed docs
- knowledge summaries
- stable implementation guidance
- reusable references

### Write requirements
Only write items that are:
- validated
- likely to be reused
- understandable outside the original run context

### Must not store
- raw chat transcripts
- speculative guesses
- unresolved contradictions
- giant unfiltered prompt blobs

### Retention
- durable
- indexed
- semantically retrievable

---

## 6. Procedural Memory

### Purpose
Store reusable workflows and known-good execution patterns.

### May store
- recovery runbooks
- service restart procedures
- installation sequences
- debug playbooks
- tool recipes
- policy-aware execution sequences

### Promotion rule
Procedural memory is never written on first success.

An item may be promoted only after:
- repeated successful use
- verification of outcomes
- no contradictory evidence
- policy compatibility confirmed

### Must not store
- one-off hacks
- brittle environment-specific steps unless clearly labeled
- unverified procedures
- workflows that bypass policy

---

## 7. Promotion Rules

### Working → Episodic
Promote when:
- run completes
- approval occurs
- failure occurs
- recovery occurs
- meaningful artifact is produced

### Episodic → Semantic
Promote when:
- the content is broadly reusable
- the content is validated
- the content is not tied to one fragile run only
- future retrieval value is high

### Episodic/Semantic → Procedural
Promote only when:
- the procedure succeeded multiple times
- the verifier confirmed outcomes
- no higher-priority contradiction exists
- the workflow fits policy

---

## 8. Memory Redaction Rules

Before any memory write:
- redact secrets
- redact tokens
- redact private credentials
- remove large irrelevant blobs
- avoid storing raw browser session details unless explicitly required

If redaction cannot be guaranteed, do not write the item.

---

## 9. Storage Guidance

### Recommended progression
- Working + episodic: SQLite/Postgres first
- Semantic: vector-backed retrieval layer
- Procedural: structured records with promotion metadata

### Recommended file/data areas
- `data/state/`
- `data/artifacts/`
- `data/logs/`
- `data/vectors/`

---

## 10. Write Decision Rules

Before writing a memory item, ask:

1. Is this useful beyond the current step?
2. Is it validated?
3. Is it safe to store?
4. Which memory layer is the minimal correct destination?
5. Is there already a better canonical version stored elsewhere?

If the answer is unclear, do not write it yet.

---

## 11. Immediate Build Priority

Implement first:
- `working_store.py`
- `episodic_store.py`
- `memory_writer.py`
- `memory_policy.py`

Then add:
- semantic store
- retrieval engine
- promotion rules
- procedural store

The system does not need full semantic memory on day one, but it does need disciplined memory writes on day one.
