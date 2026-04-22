# V1 SOURCE GOVERNANCE BOOTSTRAP

## Goal

Make the assistant’s source system concrete, auditable, and easy to follow before deeper code changes.

## Deliverables

1. Add `/kb/*` pages to the repo.
2. Add `docs/CORE_SOURCES_INDEX.md`.
3. Add `docs/PROJECT_MEMORY_INDEX.md`.
4. Add `docs/KB_MAINTENANCE_PROTOCOL.md`.
5. Update source blueprint to recognize KB as a first-class tier.
6. Create runtime truth files if absent.
7. Register remote doc surfaces in `sources/REMOTE_DOC_SURFACES.md`.

## Acceptance criteria

- The assistant can answer “where should I look first?” without ambiguity.
- Every source question maps to a tier and file.
- Runtime-state questions are answered from `runtime/*` instead of memory.
- Safety, validation, schema, and memory questions resolve through the KB + canonical docs.
- External docs are listed with machine-friendly endpoints and usage notes.

## Non-goals

- broad runtime code changes
- donor repo merges
- replacing canonical docs with KB pages

## Execution order

1. land KB pages
2. land core indexes
3. land runtime templates
4. land remote doc surface map
5. wire cross-links
6. only then start new code slices
