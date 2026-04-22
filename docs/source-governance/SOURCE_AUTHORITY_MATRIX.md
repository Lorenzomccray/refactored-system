# SOURCE AUTHORITY MATRIX

## Purpose

This page defines which source wins when multiple sources disagree.

## Matrix

| Source type | Tier | Primary role | May override |
|---|---:|---|---|
| Runtime truth | 0 | current-state truth | all other tiers for current-state questions |
| Canonical repo docs | 1 | canonical system meaning | tiers 2–6 for doctrine and architecture |
| Maintained KB | 2 | navigation and maintained operational knowledge | tiers 3, 5, and 6 when aligned to canonical docs |
| Project memory | 3 | stable prior decisions and precedents | tiers 5 and 6 only |
| Remote official docs | 4 | official external truth | tiers 5 and 6 for vendor or protocol specifics |
| Derived summaries | 5 | synthesized guidance | tier 6 only |
| Raw dumps / transcripts | 6 | evidence and archival material | none |

## Rules

### Current-state questions
- runtime truth wins
- if runtime truth is missing, say it is missing and fall back carefully

### Architecture or schema meaning
- canonical repo docs win
- KB may summarize but does not override canon

### Remote vendor or protocol behavior
- official remote docs win over internal derived summaries
- if remote docs imply a change to internal doctrine, surface the variance explicitly

### Project memory
- memory informs decisions but does not silently override runtime truth or canonical docs

### Raw evidence
- raw dumps and transcripts are evidence only until promoted or translated into stronger sources

## Practical use
1. Route with `CORE_SOURCES_INDEX.md`
2. Resolve disagreements with this matrix
3. State uncertainty if the stronger source is absent or stale
