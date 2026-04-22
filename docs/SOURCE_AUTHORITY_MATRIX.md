# SOURCE AUTHORITY MATRIX

## Purpose

This file defines which source tier wins for each category of question.
Consult this before retrieving or writing any canonical content.

## Status date
2026-04-22

## Authority tiers (highest to lowest)

| Tier | Location | Wins when |
|------|----------|-----------|
| 1 | `runtime/*` | Question is about current state, live capabilities, or active blockers |
| 2 | `docs/*` | Question is about policy, schema, contracts, or architecture decisions |
| 3 | `kb/*` | Question is about operational guidance, principles, or procedures |
| 4 | `build/*` | Question is about active implementation targets or execution plans |
| 5 | `docs/reference/*` | Question is about analogies, lessons, or non-canonical context |
| 6 | Working memory / chat | Transient context only — never canonical truth |

## Per-domain ownership

| Domain | Canonical file |
|--------|---------------|
| Current tools and connectors | `runtime/CURRENT_TOOLS.md` |
| Current gaps | `runtime/CURRENT_GAPS.md` |
| Current blockers | `runtime/CURRENT_BLOCKERS.md` |
| Memory state | `runtime/CURRENT_MEMORY_STATE.md` |
| Repo map | `runtime/CURRENT_REPO_MAP.md` |
| Active workflows | `runtime/CURRENT_WORKFLOWS.md` |
| Source index | `docs/CORE_SOURCES_INDEX.md` |
| Schema contracts | `docs/SCHEMA_CONTRACTS.md` |
| Risk taxonomy | `docs/RISK_TAXONOMY.md` |
| Tool contracts | `docs/TOOL_CONTRACTS.md` |
| Execution receipts | `docs/EXECUTION_RECEIPTS.md` |
| Memory write policy | `docs/MEMORY_WRITE_POLICY.md` |
| Architecture | `kb/architecture.md` |
| Principles | `kb/principles.md` |
| Safety | `kb/safety.md` |
| Validation | `kb/validation.md` |
| Schemas (KB) | `kb/schemas.md` |
| Workflows (KB) | `kb/workflows.md` |
| Repo rules | `kb/repo-rules.md` |

## Conflict rule

When two sources disagree, the higher-tier source wins.
Surface the conflict explicitly — do not silently resolve it.
See `docs/SOURCE_CONFLICT_POLICY.md` for resolution steps.
