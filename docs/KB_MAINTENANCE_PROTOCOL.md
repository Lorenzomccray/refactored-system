# KB MAINTENANCE PROTOCOL

## Purpose

Define how `/kb/*` pages stay synchronized with canonical docs, runtime truth, and external changes.

## Canonical rule

KB pages are the fast navigation and decision surface.
Canonical docs remain the detailed source of truth.

If they diverge, update the KB or downgrade the KB page immediately.

## Update triggers

Update a KB page when any of the following occur:
1. a canonical doc changes its meaning
2. a schema field or versioning rule changes
3. a risk class or approval rule changes
4. a workflow changes materially
5. a runtime doc reveals a persistent new reality worth generalizing
6. an external vendor/protocol change alters how the project should ingest docs or expose tools

## Required structure for each KB page

1. Purpose
2. Scope
3. Facts from doctrine
4. Canonical rules
5. Boundaries
6. Cross-references
7. Assumptions
8. Open questions

## Change discipline

- Do not turn KB pages into transcript dumps.
- Keep KB pages short enough to be retrieval-friendly.
- Prefer additive changes.
- If uncertainty is high, record it instead of smoothing it away.
- Link to the controlling canonical doc.

## Review cadence

### Per change
- update impacted KB page(s)
- update cross-links if topic boundaries shifted
- check whether `CORE_SOURCES_INDEX.md` changed

### Weekly or per milestone
- verify stale open questions
- verify that runtime truths do not contradict KB defaults
- verify that build docs still point to the active bounded slice

## Deprecation rule

If a KB page becomes stale or superseded:
- mark it as superseded
- point to replacement page(s)
- do not silently delete historical context without an ADR or decision log entry
