# CORE SOURCES INDEX

## Purpose

This is the front door into the source system.

Use it to decide:
- what source tier to check first
- which pages are canonical for the task
- which pages are current-state truth
- which pages are summary-only

## Source tiers

1. Runtime truth — `runtime/truth/*`
2. Canonical repo docs — canonical architecture, schema, risk, memory, receipt docs
3. Maintained KB — `kb/*`
4. Project memory — `docs/source-governance/PROJECT_MEMORY_INDEX.md` plus `memory/*` when present
5. Remote official docs — `docs/source-governance/REMOTE_DOC_SURFACES.md`
6. Derived summaries
7. Raw dumps and transcripts

## Task-to-source routing

### General orientation
Read in order:
1. `kb/index.md`
2. `kb/principles.md`
3. `kb/repo-rules.md`

### Architecture or design work
Read in order:
1. `kb/architecture.md`
2. `docs/MASTER_AI_SYSTEM_V2.md`
3. `kb/schemas.md`
4. `docs/SCHEMA_CONTRACTS.md`

### Planning work
Read in order:
1. `kb/workflows.md`
2. `kb/checklists.md`
3. `docs/source-governance/PROJECT_MEMORY_INDEX.md`
4. active build doc in `build/`

### Risk-sensitive work
Read in order:
1. `kb/safety.md`
2. `kb/validation.md`
3. canonical risk and receipt docs
4. runtime constraints

### Current-state questions
Read in order:
1. `runtime/truth/system-state.md`
2. `runtime/truth/tool-state.md`
3. `runtime/truth/memory-state.md`
4. `runtime/truth/current-constraints.md`
5. `runtime/truth/current-open-questions.md`

### Prior decision or recurring tradeoff
Read in order:
1. `docs/source-governance/PROJECT_MEMORY_INDEX.md`
2. `memory/canonical-precedents.md`
3. `kb/precedents.md`
4. `kb/adr.md`

### Vendor or protocol questions
Read in order:
1. `docs/source-governance/REMOTE_DOC_SURFACES.md`
2. relevant official remote docs
3. only then any derived summary

## Canonical docs map

### Canonical system truth
- `docs/MASTER_AI_SYSTEM_V2.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/RISK_TAXONOMY.md`
- `docs/MEMORY_WRITE_POLICY.md`
- `docs/EXECUTION_RECEIPTS.md`

### Source governance truth
- `docs/source-governance/SOURCE_SYSTEM_BLUEPRINT.md`
- `docs/source-governance/SOURCE_AUTHORITY_MATRIX.md`
- `docs/source-governance/SOURCE_CONFLICT_POLICY.md`
- `docs/source-governance/SOURCE_FRESHNESS_LEDGER.md`
- `docs/source-governance/RUNTIME_FILE_STANDARDS.md`
- `docs/source-governance/KB_MAINTENANCE_PROTOCOL.md`

## Usage notes

- Use the smallest relevant set.
- Routing order is not authority order.
- Always check freshness when the question depends on current state.
- Never treat raw dumps as canonical truth.
