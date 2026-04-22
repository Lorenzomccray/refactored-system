# CANONICAL PRECEDENTS

## Purpose

Long-form summaries of canonical precedents that inform project decisions and operational guidance.

## Status date
2026-04-22

## What belongs here

* Precedents that are too long to summarize in `kb/precedents.md`.
* Precedents with multi-step context, rationale chains, or cross-cutting impact.
* Precedents that were elevated from transient memory to permanent record.

## Precedent entries

### P-001 — Source governance before code changes

**Decision**: Establish the source governance layer (KB, canonical docs, runtime truth files) before making substantive code changes.

**Rationale**: Without a stable source layer, agents and developers answer questions from chat memory and drift from canonical truth. Landing the KB and docs first prevents compounding source conflicts.

**Outcome**: `build/V1_SOURCE_GOVERNANCE_BOOTSTRAP.md` was created as the first build target. KB pages and canonical docs were landed before any V1 code patches.

**Status**: In progress as of 2026-04-22.

**Source**: `build/V1_SOURCE_GOVERNANCE_BOOTSTRAP.md`

---

## Promotion rule

A pattern is added here when:
1. It has succeeded in at least two separate executions.
2. It has been explicitly reviewed and accepted.
3. It is cross-referenced in `kb/precedents.md`.

## Related files

* `kb/precedents.md` — short registry of all precedents
* `docs/EXECUTION_RECEIPTS.md` — execution logs that may yield new precedents
