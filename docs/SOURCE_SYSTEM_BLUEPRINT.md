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
