# STATE OWNERSHIP

## Purpose
Define which layer is the authoritative owner of state and which layers may only transport, cache, enrich, or display it.

## Authoritative owner
Only the canonical core brain may own:
- task state
- approval state
- execution lifecycle state
- memory promotion state
- final run receipts
- final run disposition

## Non-authoritative layers
Adapters, workers, tools, provider gateways, queues, and surfaces may:
- transport state
- cache state
- enrich state with local metadata
- display state to operators
- propose actions
- execute bounded work

They may not:
- redefine task truth
- redefine approval truth
- redefine completion semantics
- redefine memory promotion
- become the source of truth for final receipts

## Conflict rule
If an adapter-local state view conflicts with canonical core state, the canonical core wins. The conflict must be logged and resolved explicitly.

## Required implementation rule
Every adapter must document:
- owned resources
- non-owned resources
- what state it can cache
- what state it must read from the core
