# SOURCE SYSTEM BLUEPRINT V2

## Purpose

Extend the source system so the KB layer becomes a first-class operational surface for the assistant.

## Updated source tiers

1. KB control surface
2. Canonical internal architecture docs
3. Runtime truth docs
4. Build-slice docs
5. Reference lessons docs
6. External public registries and remote doc surfaces

## KB control surface

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

## New rules

- KB pages are the assistant’s first navigation surface.
- Canonical docs remain the detailed truth layer behind the KB.
- Runtime docs override canonical docs only for current-state questions.
- External docs do not override internal doctrine without explicit variance handling.
- One topic, one controlling canonical file, with one or more KB entry points if needed.

## Retrieval protocol

### For planning
1. `kb/principles`
2. `kb/repo-rules`
3. `kb/workflows`
4. `build/*`

### For code/interface changes
1. `kb/architecture`
2. `kb/schemas`
3. `kb/validation`
4. runtime truth docs

### For risk-sensitive work
1. `kb/safety`
2. `kb/validation`
3. `RISK_TAXONOMY.md`
4. `EXECUTION_RECEIPTS.md`

### For source confusion
1. `CORE_SOURCES_INDEX.md`
2. `PROJECT_MEMORY_INDEX.md`
3. `runtime/CURRENT_GAPS.md`

## External doc surface rule

Remote docs should be mounted wherever possible through machine-friendly endpoints:
- `llms-full.txt`
- `llms.txt`
- MCP docs servers
- structured markdown or JSON APIs

## Maintenance

Update KB pages when canonical meaning changes.
Update runtime docs when actual system state changes.
Update build docs when the active target changes.
Update remote doc surfaces when official endpoints or MCP surfaces change.
