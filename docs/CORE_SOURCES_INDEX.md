# CORE SOURCES INDEX

## Purpose

This file is the front door into the project knowledge system.

Use it before memory, before broad repo inspection, and before external browsing.

## Retrieval order

1. `/kb/*` pages for policy, architecture, workflow, schema, validation, and safety intent.
2. Canonical docs in `/docs` for full source-of-truth detail.
3. Runtime truth docs in `/runtime` for what is true now.
4. Active build docs in `/build` for the next bounded implementation target.
5. Reference docs in `/reference` for lessons and analogies.
6. External source registries in `/sources` for fresh or vendor-specific guidance.
7. Memory only when the above do not answer the question.

## Tier map

### Tier 1 — KB control surface
- `kb/principles.md`
- `kb/repo-rules.md`
- `kb/architecture.md`
- `kb/schemas.md`
- `kb/workflows.md`
- `kb/adr.md`
- `kb/checklists.md`
- `kb/precedents.md`
- `kb/validation.md`
- `kb/safety.md`
- `kb/glossary.md`
- `kb/faq.md`

### Tier 2 — Canonical docs
- `docs/MASTER_AI_SYSTEM_V2.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/RISK_TAXONOMY.md`
- `docs/MEMORY_WRITE_POLICY.md`
- `docs/EXECUTION_RECEIPTS.md`
- `docs/DECISIONS_LOG.md`
- `docs/PROJECT_MEMORY_INDEX.md`
- `docs/KB_MAINTENANCE_PROTOCOL.md`

### Tier 3 — Runtime truth
- `runtime/CURRENT_REPO_MAP.md`
- `runtime/CURRENT_WORKFLOWS.md`
- `runtime/CURRENT_PROVIDERS.md`
- `runtime/CURRENT_TOOLS.md`
- `runtime/CURRENT_MEMORY_STATE.md`
- `runtime/CURRENT_GAPS.md`
- `runtime/CURRENT_BLOCKERS.md`

### Tier 4 — Build focus
- `build/V1_SAFE_PLANNER.md`
- `build/V1_PATCH_PROPOSAL.md`
- `build/V1_APPROVED_EXECUTION.md`
- `build/V1_POLICY_ENGINE.md`
- `build/V1_MEMORY_BOOTSTRAP.md`
- `build/V1_SOURCE_GOVERNANCE_BOOTSTRAP.md`

### Tier 5 — External doc surfaces
- `sources/AI-KNOWLEDGE-SOURCES.txt`
- `sources/MCP-Knowledge.txt`
- `sources/universal_ai_source_pack.yaml`
- `sources/REMOTE_DOC_SURFACES.md`

## Resolution rules

- If KB and canonical docs conflict, canonical docs win and KB must be updated.
- If canonical docs and runtime docs conflict, runtime docs win for current-state questions.
- If build docs conflict with canonical docs, build docs must state the variance and intended migration path.
- If external docs conflict with internal doctrine, surface the conflict explicitly before acting.

## Update triggers

Update this index when:
- a new canonical doc is added
- a KB page becomes authoritative for a new topic
- a runtime truth file is added or renamed
- an external doc surface becomes operationally important
