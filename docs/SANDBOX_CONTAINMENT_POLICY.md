# SANDBOX CONTAINMENT POLICY

## Purpose
Define how prototype, donor, and sandbox systems may inform the canonical core without contaminating it.

## Allowed influence paths
Sandbox and donor outputs may influence the canonical system only through:
- DECISIONS_LOG.md
- runtime truth docs
- normalized lessons docs
- explicitly approved schema changes

## Forbidden
- direct code copy from sandbox to core
- undocumented behavior promotion
- adapter-first architecture changes based on convenience
- prototype data becoming semantic memory by default
- prototype-owned receipts becoming canonical run receipts

## Review rule
No prototype or donor pattern may enter the canonical core without:
1. a decision log entry
2. schema mapping
3. policy review
4. verification criteria

## Teardown rule
Any sandbox system must be removable without damaging the coherence of the canonical core.
