# SOURCE SYSTEM BLUEPRINT

## Purpose

This document defines the source-governance operating system for `refactored-system`.

It exists to answer, in a consistent order:
- what source tiers exist
- what should be consulted first
- what is canonical
- what is current
- what is derived
- what is stale
- what is allowed to override what
- what must be verified before a source is trusted for action

## Design goals

The source system should be:
- discoverable
- authoritative
- maintainable
- machine-usable
- safe against drift
- easy to extend across projects

## Core distinction

Routing order and authority order are not the same thing.

A source can be easy to find without being authoritative, and authoritative without being current.

## Source tiers

| Tier | Source type | Role | Typical examples |
|---|---|---|---|
| 0 | Runtime truth | Current-state truth | `runtime/truth/*` |
| 1 | Canonical repo docs | Canonical system truth | architecture, schema, risk, memory, receipt docs |
| 2 | Maintained KB | Navigation and operational guidance | `kb/*` |
| 3 | Project memory index | Stable prior decisions and precedents | `memory/*`, memory indexes |
| 4 | Remote official docs | Vendor and protocol truth | official docs, llms.txt, docs MCP servers |
| 5 | Derived summaries | Synthesized guidance | analysis docs, generated summaries |
| 6 | Raw dumps and transcripts | Lowest-trust evidence stores | logs, pasted exports, raw dumps |

## Authority rules

If two sources conflict:
- tier 0 wins over all others for current-state questions
- tier 1 wins over tiers 2–6 for canonical system meaning
- tier 2 wins over tiers 3, 5, and 6 when it reflects maintained internal guidance
- tier 4 can outrank tiers 5 and 6 when it is official and current
- tier 6 never becomes canonical truth by itself

## Retrieval rules

1. Classify the task.
2. Use the core source index or KB index to route.
3. Retrieve the smallest relevant source set.
4. Check authority and freshness.
5. Resolve conflicts using the authority matrix.
6. State uncertainty when evidence is insufficient.
7. Produce a durable artifact where appropriate.
8. Emit or reference a receipt when action or meaningful synthesis occurred.

## Source classes

### Runtime truth
Use for:
- what is true now
- what tools are callable now
- what constraints or blockers are active now

### Canonical repo docs
Use for:
- architecture meaning
- schema contracts
- risk classes
- memory policy
- execution receipt model

### Maintained KB
Use for:
- fast navigation
- operational summaries
- checklists
- recurring questions
- source routing

### Project memory
Use for:
- recurring constraints
- enduring decisions
- stable tradeoffs
- precedent links

### Remote official docs
Use for:
- vendor and protocol specifics
- current API or protocol behavior
- official integration rules

### Derived summaries
Use for:
- scoped synthesis
- temporary analysis
- human-friendly summaries

### Raw dumps and transcripts
Use for:
- evidence inspection only
- archival or recovery context

## Governance rules

- One topic, one canonical file.
- KB pages are navigation and governance, not competing canon.
- Runtime truth overrides assumptions.
- Derived summaries must link back to stronger sources.
- Raw dumps must not be treated as authoritative without promotion.
- Freshness and owner fields should be present on governance-critical pages.

## Integration points

This blueprint is implemented through:
- `docs/source-governance/CORE_SOURCES_INDEX.md`
- `docs/source-governance/PROJECT_MEMORY_INDEX.md`
- `docs/source-governance/SOURCE_AUTHORITY_MATRIX.md`
- `docs/source-governance/SOURCE_CONFLICT_POLICY.md`
- `docs/source-governance/SOURCE_FRESHNESS_LEDGER.md`
- `docs/source-governance/TRUTH_FILE_STANDARDS.md`
- `docs/source-governance/REMOTE_DOC_SURFACES.md`
- `docs/source-governance/KB_MAINTENANCE_PROTOCOL.md`

## Non-goals

- turning the KB into a raw content bucket
- treating memory as stronger than docs
- treating logs or transcripts as canonical truth
- hiding freshness or conflict resolution inside agent intuition
