# REPO MANIFEST

## Purpose

This file is the map of the repository.

Use it to help humans and AI tools understand what exists, where to look first, and which files are canonical for each concern.

This file does not replace canonical docs, runtime truth files, or the core source index. It supports navigation.

## Repository overview

### Top-level goals
* Modular, autonomous AI system that handles complex tasks by chaining specialized agents.
* Primary product: an orchestrator-agent-tool pipeline (Planner → Builder → Verifier) backed by a governed source and knowledge layer.
* Main architectural boundaries: agent runtime (`app/`), source governance (`docs/`, `kb/`, `runtime/`), build targets (`build/`), and external source registries (`sources/`).

### Top-level layout
* `/app` — application code
* `/build` — active implementation targets and bounded build docs
* `/docs` — canonical documentation
* `/docs/reference` — non-canonical lessons and analogies
* `/kb` — maintained knowledge base
* `/memory` — project memory and precedent summaries
* `/runtime` — current state truth files
* `/sources` — external doc registries and remote surfaces
* `/tests` — automated verification
* `/tools` — developer utilities and local scripts

## Canonical entry points

### Primary docs
* `docs/CORE_SOURCES_INDEX.md`
* `docs/SOURCE_AUTHORITY_MATRIX.md`
* `docs/SOURCE_CONFLICT_POLICY.md`
* `docs/KB_MAINTENANCE_PROTOCOL.md`
* `docs/PROJECT_MEMORY_INDEX.md`

### Primary KB pages
* `kb/index.md`
* `kb/principles.md`
* `kb/repo-rules.md`
* `kb/architecture.md`
* `kb/schemas.md`
* `kb/workflows.md`
* `kb/validation.md`
* `kb/safety.md`

### Runtime truth
* `runtime/CURRENT_REPO_MAP.md`
* `runtime/CURRENT_WORKFLOWS.md`
* `runtime/CURRENT_TOOLS.md`
* `runtime/CURRENT_MEMORY_STATE.md`
* `runtime/CURRENT_GAPS.md`
* `runtime/CURRENT_BLOCKERS.md`

## File categories

### Canonical
These files are the source of truth for their domain:
* `docs/*` canonical docs
* `runtime/*` current-state files
* `kb/*` maintained operational guidance
* `tests/*` verification artifacts

### Derived
These files summarize, interpret, or support canonical content:
* `docs/reference/*`
* generated summaries
* analysis notes
* meeting notes

### Implementation
These files contain executable or build-related work:
* `app/*`
* `build/*`
* `tools/*`

## Navigation guide

### If you need policy or process
Read:
* `docs/CORE_SOURCES_INDEX.md`
* `kb/principles.md`
* `kb/repo-rules.md`
* `docs/SOURCE_AUTHORITY_MATRIX.md`

### If you need architecture or schema details
Read:
* `kb/architecture.md`
* `kb/schemas.md`
* `docs/SCHEMA_CONTRACTS.md`

### If you need current state
Read:
* `runtime/CURRENT_REPO_MAP.md`
* `runtime/CURRENT_WORKFLOWS.md`
* `runtime/CURRENT_TOOLS.md`
* `runtime/CURRENT_GAPS.md`
* `runtime/CURRENT_BLOCKERS.md`

### If you need implementation targets
Read:
* `build/V1_SAFE_PLANNER.md`
* `build/V1_PATCH_PROPOSAL.md`
* `build/V1_APPROVED_EXECUTION.md`

### If you need precedent or analogy
Read:
* `docs/reference/*`
* `kb/precedents.md`
* `memory/canonical-precedents.md`

## Update rules

Update this manifest when:
* a top-level folder is added or removed
* a canonical entry point changes
* runtime truth files are renamed
* new build targets become active
* new source registries are added

## Maintenance rules

* Keep this file short and navigable.
* Do not duplicate canonical content.
* Prefer links over summaries.
* If a file becomes canonical, move it into the canonical entry point section.
* If a file is deprecated, remove it from the manifest or mark it clearly.

## Source hierarchy reminder

1. Runtime truth files
2. Canonical docs
3. KB operational guidance
4. Build docs
5. Reference material
6. Raw or transient content

## Conflict handling

If this manifest conflicts with a canonical doc or runtime truth file, the higher-tier source wins.
