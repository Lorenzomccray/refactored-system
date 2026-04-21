# SOURCE SYSTEM BLUEPRINT

## Purpose
This file defines how project sources are organized, prioritized, and maintained so the system stays aligned, modular, and execution-focused.

## Source tiers
1. Canonical internal architecture docs
2. Runtime truth docs
3. Build-slice docs
4. Reference lessons docs
5. External public registries

## Canonical docs
- MASTER_AI_SYSTEM_V2.md
- SCHEMA_CONTRACTS.md
- RISK_TAXONOMY.md
- MEMORY_WRITE_POLICY.md
- EXECUTION_RECEIPTS.md
- TOOL_CONTRACTS.md
- PROVIDER_ROUTING.md
- VERIFICATION_MODEL.md
- INTEGRATION_POLICY.md
- BUILD_ORDER.md
- DECISIONS_LOG.md
- STATE_OWNERSHIP.md
- SECRETS_POLICY.md
- ADAPTER_BOUNDARIES.md
- OBSERVABILITY_MINIMUMS.md
- IDENTITY_MODEL.md
- SANDBOX_CONTAINMENT_POLICY.md

## Runtime docs
- runtime/CURRENT_REPO_MAP.md
- runtime/CURRENT_WORKFLOWS.md
- runtime/CURRENT_PROVIDERS.md
- runtime/CURRENT_TOOLS.md
- runtime/CURRENT_MEMORY_STATE.md
- runtime/CURRENT_GAPS.md
- runtime/CURRENT_BLOCKERS.md

## Build docs
- build/V1_SAFE_PLANNER.md
- build/V1_PATCH_PROPOSAL.md
- build/V1_APPROVED_EXECUTION.md
- build/V1_POLICY_ENGINE.md
- build/V1_MEMORY_BOOTSTRAP.md

## Reference docs
- reference/GOBII_LESSONS.md
- reference/OPENCLAW_LESSONS.md
- reference/MCP_PATTERNS.md
- reference/REPO_OPTIONS.md
- reference/THIRD_PARTY_ATTRIBUTION.md

## External source registries
- sources/AI-KNOWLEDGE-SOURCES.txt
- sources/MCP-Knowledge.txt
- sources/universal_ai_source_pack.yaml

## Rules
- One topic, one canonical file.
- Architecture docs override reference notes.
- Runtime docs override assumptions.
- Build docs define the next coding target.
- Raw repo dumps are not canonical truth.
- Temporary workflow transcripts must be converted into docs or archived.
- No prototype, donor, or adapter may redefine canonical architecture by momentum.
- No repo may move from REFERENCE or SANDBOX to ADAPTER or PRIMARY without a decision log entry and doctrine review.
- Any adopted pattern from a donor repo must be rewritten into a canonical internal doc before implementation.
- Runtime truth docs must be updated whenever actual running behavior changes, not only when architecture changes.
- If runtime truth conflicts with canonical docs, the conflict must be explicitly logged and resolved.
- The canonical core is the sole owner of authoritative task state, approval state, memory promotion state, and final run receipts.
- No raw adapter payload may cross into the core without canonical schema normalization.
- No secrets may be hardcoded in canonical or adapter source.
- No queue, workflow engine, or adapter scheduler may define canonical task success semantics.
- No item may enter procedural memory without repeated success, failure notes, environment assumptions, and rollback guidance.
- Public docs should be ingested in this order:
  1. llms-full.txt
  2. llms.txt
  3. markdown
  4. openapi/json/yaml/schema
  5. structured_html

## Maintenance
Update canonical docs when architecture changes.
Update runtime docs when actual system state changes.
Update build docs when the active implementation target changes.
Archive outdated transcripts and prompt experiments.
