# MCP_PATTERNS

## Purpose

This document captures the Model Context Protocol patterns that `refactored-system` should reuse from official MCP sources and related ecosystem docs.

This file exists to answer four questions:

1. What MCP is good for in this project
2. Which MCP patterns are worth adopting now
3. Which MCP patterns should remain adapter-level only
4. How MCP fits the canonical backend-brain architecture without becoming the brain itself

This is a **reference lessons** file.

Canonical architecture remains defined in:
- `docs/MASTER_AI_SYSTEM_V2.md`
- `docs/SCHEMA_CONTRACTS.md`
- `docs/RISK_TAXONOMY.md`
- `docs/EXECUTION_RECEIPTS.md`
- `docs/SOURCE_SYSTEM_BLUEPRINT.md`

---

## Source Basis

The project’s current source registries already identify the MCP official docs, architecture overview, build-server guide, build-client guide, registry docs, FastMCP docs, and OpenAI Apps SDK MCP concepts as high-priority sources. fileciteturn53file3 fileciteturn53file6

The master architecture also already places MCP under the external integration plane and explicitly says capabilities such as MCP should remain external to the brain core. fileciteturn53file9

---

## Core MCP Lesson

The most important lesson is simple:

> MCP is a **standard adapter surface** for tools, resources, and prompts.
> It is not the control plane, not the memory policy, and not the runtime law system.

That makes MCP extremely valuable for interoperability while still remaining subordinate to the canonical brain.

---

## Patterns Worth Reusing

### 1. Host / client / server separation

Official MCP materials emphasize a host-client-server mental model and architecture. fileciteturn53file3

#### What to reuse
In `refactored-system`, keep these roles distinct:
- **Host**: the operator-facing environment or app surface
- **Client**: the bridge that talks MCP
- **Server**: the provider of tools/resources/prompts

#### Project rule
The `refactored-system` brain should usually behave as:
- an MCP **host-aware orchestrator**
- sometimes an MCP **client**
- optionally a publisher of narrow MCP **server** surfaces

But the control plane itself remains internal and canonical.

---

### 2. MCP is best used as an adapter boundary

The master architecture already requires adapters to depend on the brain, while the brain must not depend on any one adapter. MCP fits that pattern very well. fileciteturn53file9

#### What to reuse
Wrap MCP under:
- `app/integrations/mcp/`
- `app/tools/mcp_tool.py`

#### Rule
MCP should expose capabilities to the brain, not replace:
- planning
- authorization
- verification
- memory promotion
- receipts

---

### 3. External capabilities should remain discoverable and replaceable

The MCP registry model and publication flow reinforce a useful discipline: external capabilities should have metadata, discoverability, and clean packaging. fileciteturn53file3

#### What to reuse
For every MCP-backed capability, track:
- name
- provider/server identity
- capability type
- risk class
- auth needs
- input/output schema
- verification method
- receipt requirements

This complements the tool-plane requirement that tools declare capability name, schemas, risk class, approval level, timeout, retry, and verification method. fileciteturn53file9

---

### 4. FastMCP is useful for narrow server surfaces

The current source set gives FastMCP a high-priority role as a practical framework for MCP tools, resources, prompts, and clients. fileciteturn53file3 fileciteturn53file6

#### What to reuse
Use FastMCP when you want to publish:
- a thin tool surface
- a resource surface for docs/state
- a prompt surface for reusable workflows

#### Rule
Keep each published MCP surface narrow and explicit.

Examples:
- repo status server
- memory query server
- tool catalog server
- runtime telemetry resource server

Not:
- one giant “god server” with hidden orchestration logic

---

### 5. MCP resource exposure pairs well with curated source registries

The source system blueprint says public docs should be ingested in a preferred order and treated as external registries, not raw dumps. fileciteturn53file8

#### What to reuse
Expose only curated MCP resources such as:
- canonical docs
- current runtime maps
- current tool catalog
- current provider map
- current gaps/blockers

#### Rule
Do not expose:
- raw transient dumps
- unsafe secrets
- unvalidated internal scratch state

This keeps MCP resources aligned with the memory write policy and source-system blueprint.

---

### 6. MCP tools still require internal policy mediation

One common trap is to treat an MCP tool as “already safe” because it came from a standards-based server.

#### Rule
In `refactored-system`, every MCP capability must still pass through:

```text
plan → authorization → execution wrapper → receipt → verification
```

That rule already governs all tools in the canonical architecture and must apply to MCP-backed tools too. fileciteturn53file9

---

### 7. MCP can improve interoperability without contaminating the core

The strongest reason to adopt MCP is that it lets the system talk to more capabilities without hardwiring those integrations into the control plane.

#### What to reuse
Use MCP for:
- external tools
- external resources
- prompt bundles
- ecosystem interoperability
- clean capability publishing

#### What not to do
Do not let MCP determine:
- state machine design
- approval policy
- verifier semantics
- memory-layer boundaries

---

## Recommended MCP Roles In `refactored-system`

### Role A — External client to third-party servers

Use MCP to reach:
- docs servers
- tool servers
- structured external capability packs

### Role B — Narrow internal publisher

Publish selected internal capabilities as MCP servers when useful:
- current repo map
- runtime status resources
- approved tool surfaces
- memory query surface

### Role C — Adapter bridge for operator environments

Use MCP to support integration with environments that prefer standardized tool/resource access.

---

## What Not To Reuse Directly

### 1. MCP as the orchestration model

MCP is not a substitute for:
- planner outputs
- execution graphs
- approval decisions
- verifier outputs
- receipt records

#### Rule
Never mistake a protocol surface for the brain itself.

---

### 2. Blind trust in external MCP servers

An MCP server may be well-formed and still be unsafe, low-quality, stale, or too broad.

#### Rule
Before a server becomes operationally useful, classify:
- trust tier
- auth model
- risk envelope
- schema quality
- output reliability
- verification method

This is consistent with the project’s source registries already assigning trust tiers and ingestion priority. fileciteturn53file3 fileciteturn53file6

---

### 3. Giant all-in-one MCP exposure

Do not create one oversized MCP surface that publishes every internal capability.

#### Rule
Prefer small, coherent server boundaries.

Good examples:
- `repo_status_mcp`
- `memory_query_mcp`
- `docs_catalog_mcp`
- `runtime_observability_mcp`

Bad example:
- `everything_mcp` with hidden stateful power and unclear risk boundaries

---

### 4. Prompt surfaces as hidden law

MCP prompts can be useful, but they must not become the hidden place where runtime law, approval policy, or verifier semantics are actually enforced.

#### Rule
Prompts may assist execution.
They may not replace explicit policy and contract layers.

---

## Classification of MCP Ideas

### Adopt now
- MCP as adapter boundary
- host/client/server role separation
- capability metadata discipline
- narrow FastMCP-style publishing for selected surfaces
- registry/discoverability mindset

### Rewrite later
- internal MCP publishing for repo/runtime status
- resource catalog server
- curated prompt server
- MCP-backed memory query adapter

### Reference only
- community tutorials
- ecosystem packaging patterns
- registry publication flow until the internal surfaces are stable

### Reject
- treating MCP as the brain
- trusting external MCP servers without policy gating
- exposing giant uncurated internal surfaces

---

## Clean Extraction Targets For `refactored-system`

Mine MCP materials for these reusable patterns:

1. **Protocol boundary shape**
   - how tools/resources/prompts are exposed cleanly

2. **Server metadata discipline**
   - how capabilities are described and discovered

3. **Narrow server packaging**
   - how to publish one responsibility domain per surface

4. **Host/client interoperability**
   - how the brain can consume external capabilities cleanly

---

## Mapping Into Canonical Architecture

| MCP pattern | Canonical destination |
|---|---|
| Host/client/server separation | `app/integrations/mcp/` |
| MCP-backed tool wrapper | `app/tools/mcp_tool.py` |
| Capability metadata | `app/tools/tool_contract.py`, `app/tools/tool_registry.py` |
| Approval/verification wrapping | `app/tools/tool_authz.py`, `app/tools/tool_receipts.py`, `app/verification/` |
| Narrow internal MCP servers | `app/integrations/mcp/` adapters only |
| Resource publication for current docs/runtime maps | `docs/runtime/` + MCP adapter layer |

---

## Practical Initial MCP Build Order

1. Build `mcp_tool.py` as a typed wrapper
2. Add policy classification for MCP-backed tool calls
3. Add receipt generation for MCP invocations
4. Add verifier hooks for MCP results
5. Only then publish or consume higher-value MCP surfaces

This keeps MCP under control-plane law instead of beside it.

---

## Final Lesson

MCP’s best contribution to `refactored-system` is this:

> it gives the project a clean interoperability protocol for tools, resources, and prompts without forcing the core brain to become an integration monolith.

Use MCP aggressively for adapters.
Do not let it displace the canonical architecture.
