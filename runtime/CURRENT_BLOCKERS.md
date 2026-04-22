# CURRENT_BLOCKERS
## Source-system blockers that can reduce assistant reliability

## Status date
2026-04-22

## Current blockers
- Repo-side landing of the KB/source pack is not yet confirmed
- Connector availability outside Airtable was not confirmed in the last validated setup pass
- Runtime truth may drift if not explicitly maintained after project changes
- Some governance pages are doctrine-derived because formal repo precedents are thin

## Blocker handling rule
If a blocker affects truth, capability, or safety:
- surface it explicitly
- do not silently assume it away
- prefer the smallest safe next step
