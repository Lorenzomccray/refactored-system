# SOURCE CONFLICT POLICY

## Purpose

Define how source conflicts are detected, stated, and resolved.

## Conflict definition

A conflict exists when two sources make incompatible claims about:
- current state
- architecture meaning
- schema definition
- workflow requirement
- safety or approval behavior
- freshness or staleness

## Resolution procedure

1. Classify the question type.
2. Identify the stronger source using `SOURCE_AUTHORITY_MATRIX.md`.
3. Prefer the stronger source.
4. State the conflict explicitly if it matters to the answer or decision.
5. If the stronger source is stale or incomplete, say so.
6. If needed, create a follow-up task to reconcile the docs.

## Standard conflict cases

### Runtime truth vs canonical docs
For current-state questions, runtime truth wins.
For architecture meaning, canonical docs still define intended system shape.

### Canonical docs vs KB
Canonical docs win.
KB should be updated.

### Official remote docs vs internal derived summaries
Official remote docs win for vendor or protocol specifics.
Derived summaries should be corrected or retired.

### Project memory vs canonical docs
Canonical docs win.
Project memory should be updated if the conflict reflects an outdated decision record.

### Raw dumps vs any maintained source
Maintained source wins unless the raw dump reveals a fresh reality that has not yet been reflected elsewhere.
In that case, the answer should say the evidence is fresh but not yet promoted.

## Required response behavior
- never hide a material conflict
- never silently pick a lower-tier source over a higher-tier source
- never treat raw dumps as canon by convenience
- prefer the smallest safe claim when evidence is mixed

## Follow-up actions when a conflict is found
- update runtime truth if the system state changed
- update KB if the summary drifted
- update canonical docs if doctrine actually changed
- update freshness ledger if a page is stale
