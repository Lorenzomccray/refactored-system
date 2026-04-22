# PROJECT MEMORY INDEX

## Purpose

This file defines what the assistant should trust first and what memory layers currently exist.

## Current objective

Make the project source system concrete enough that assistant behavior is anchored in docs, runtime truth, receipts, and externally retrievable documentation surfaces.

## Canonical memory posture

- Chat = working context
- Docs = truth
- Runtime docs = current truth
- Receipts = evidence
- Procedural memory = only after repeated verified success

## Canonical docs
- `docs/MASTER_AI_SYSTEM_V2.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/RISK_TAXONOMY.md`
- `docs/MEMORY_WRITE_POLICY.md`
- `docs/EXECUTION_RECEIPTS.md`
- `docs/DECISIONS_LOG.md`
- `docs/KB_MAINTENANCE_PROTOCOL.md`
- `docs/CORE_SOURCES_INDEX.md`

## Active KB surface
- `kb/principles.md`
- `kb/repo-rules.md`
- `kb/architecture.md`
- `kb/schemas.md`
- `kb/workflows.md`
- `kb/validation.md`
- `kb/safety.md`

## Active runtime truth docs
- `runtime/CURRENT_REPO_MAP.md`
- `runtime/CURRENT_WORKFLOWS.md`
- `runtime/CURRENT_PROVIDERS.md`
- `runtime/CURRENT_TOOLS.md`
- `runtime/CURRENT_MEMORY_STATE.md`
- `runtime/CURRENT_GAPS.md`
- `runtime/CURRENT_BLOCKERS.md`

## Current build target
- `build/V1_SOURCE_GOVERNANCE_BOOTSTRAP.md`

## Promotion rules

### Working → Episodic
Promote when a run completes, fails, gets approval, or produces a meaningful artifact.

### Episodic → Semantic
Promote only validated, reusable, context-independent knowledge.

### Semantic/Episodic → Procedural
Promote only after repeated verified success and no higher-priority contradiction.

## Current gaps
- Runtime truth docs may still be incomplete.
- KB exists as files but may not yet be wired into repo navigation or tooling.
- External docs are listed but not all are yet operationally mounted as MCP surfaces.
