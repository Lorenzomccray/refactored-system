# SOURCE FRESHNESS LEDGER

## Purpose

Track freshness, ownership, and review cadence for key governance and truth files.

## Status legend
- fresh
- watch
- stale-risk
- stale

## Ledger

| Page | Owner | Status | Last reviewed | Review interval | Notes |
|---|---|---|---|---|---|
| `docs/source-governance/SOURCE_SYSTEM_BLUEPRINT.md` | repo-maintainer | fresh | 2026-04-22 | 30 days | core governance doc |
| `docs/source-governance/CORE_SOURCES_INDEX.md` | repo-maintainer | fresh | 2026-04-22 | 14 days | front door |
| `docs/source-governance/SOURCE_AUTHORITY_MATRIX.md` | repo-maintainer | fresh | 2026-04-22 | 30 days | conflict resolver |
| `docs/source-governance/SOURCE_CONFLICT_POLICY.md` | repo-maintainer | fresh | 2026-04-22 | 30 days | conflict workflow |
| `docs/source-governance/TRUTH_FILE_STANDARDS.md` | repo-maintainer | fresh | 2026-04-22 | 30 days | runtime truth contract |
| `docs/source-governance/REMOTE_DOC_SURFACES.md` | repo-maintainer | watch | 2026-04-22 | 14 days | external endpoints change faster |
| `runtime/truth/system-state.md` | repo-maintainer | watch | 2026-04-22 | 7 days | should track real repo state |
| `runtime/truth/tool-state.md` | repo-maintainer | watch | 2026-04-22 | 7 days | callable tool surface can drift |
| `runtime/truth/memory-state.md` | repo-maintainer | watch | 2026-04-22 | 14 days | layered memory posture |
| `runtime/truth/current-constraints.md` | repo-maintainer | watch | 2026-04-22 | 7 days | likely to change during build |
| `runtime/truth/current-open-questions.md` | repo-maintainer | watch | 2026-04-22 | 7 days | working governance queue |
| `kb/index.md` | repo-maintainer | fresh | 2026-04-22 | 14 days | kb front door |

## Update rule

Whenever a governed page changes meaning, update its freshness row in the same change if practical.
