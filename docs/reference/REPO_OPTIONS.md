# REPO_OPTIONS

## Purpose

This document classifies external and adjacent repositories used by the project so the core system stays modular, legally clean, and execution-focused.

It exists to answer four questions:

1. Which repo is the canonical product repo?
2. Which repos are donor/reference repos only?
3. Which repos are external platforms or integration dependencies?
4. Which repos are owned-adjacent and may become future adapters or subsystems?

This document should be read together with:
- `MASTER_AI_SYSTEM_V2.md`
- `SOURCE_SYSTEM_BLUEPRINT.md`
- `THIRD_PARTY_ATTRIBUTION.md`
- `INTEGRATION_POLICY.md`
- `BUILD_ORDER.md`

---

## Canonical Rule

Only one repository is the canonical product repo:

```text
refactored-system/
```

This repo contains the sovereign core:
- control plane
- cognition plane
- memory plane
- provider plane
- tool plane
- policy plane
- verification plane
- telemetry plane
- schemas
- canonical docs

No external repo should be merged wholesale into the core.

---

## Repo Topology

Use this workspace layout:

```text
workspace/
├── refactored-system/          # canonical core product repo
├── references/                # external/open-source donor repos
│   ├── gobii/
│   ├── openclaw/
│   ├── mcp-servers/
│   ├── open-swe/
│   ├── claude-code-templates/
│   └── skills/
├── owned-adjacent/            # user-owned side repos, possible future adapters
│   ├── code-companion/
│   ├── TabbyML/
│   ├── Performance-Optimization-System/
│   └── neurokernel/
└── sources/                   # registries, source packs, curated docs
```

---

## Classification Matrix

| Repo | Role | Classification | How to Use | Merge Policy |
|---|---|---|---|---|
| `refactored-system` | Core product | Canonical | Build the sovereign brain here | Direct development only |
| `gobii` | Donor/reference | Reference-only | Extract patterns for routing, tooling, persistence, browser isolation, budgeting | Do not merge wholesale |
| `openclaw` | Donor/reference | Reference-only | Extract local-first operator patterns, autonomy loop ideas, packaging/UX ideas | Do not merge wholesale |
| `supabase/supabase` | Platform | External platform | Use as hosted/local platform and docs reference | Keep external |
| `modelcontextprotocol/servers` | Standards/examples | Reference-only | Use for MCP server examples, patterns, and capability references | Keep external |
| `anaisbetts/mcp-installer` | Utility | External helper | Use as installer/reference utility if helpful | Keep external |
| `davila7/claude-code-templates` | Prompt/workflow donor | Reference-only | Mine prompt and workflow patterns | Do not merge wholesale |
| `mattpocock/skills` | Skills/module donor | Reference-only | Mine modular skill patterns and task packaging ideas | Do not merge wholesale |
| `langchain-ai/open-swe` | SWE-agent donor | Reference-only | Mine software engineering loop patterns and task flow ideas | Do not merge wholesale |
| `Lorenzomccray/code-companion` | Owned adjacent | Future adapter/subsystem | Evaluate for integration only when a clear interface exists | No blind merge |
| `Lorenzomccray/TabbyML` | Owned adjacent | Future adapter/subsystem | Evaluate for local model serving or coding support roles | No blind merge |
| `Lorenzomccray/Performance-Optimization-System-` | Owned adjacent | Future adapter/subsystem | Evaluate for profiling/optimization tooling or telemetry ideas | No blind merge |
| `Lorenzomccray/neurokernel` | Owned adjacent | Future adapter/subsystem | Evaluate for orchestration/experimental cognition features | No blind merge |

---

## Reference-Only Donor Repos

These repos are used to learn from patterns, architecture choices, implementation details, and operational tradeoffs.

### Gobii

Use Gobii for lessons in:
- provider routing and failover
- budget and compaction mechanisms
- tool registration/runtime patterns
- persistent state and history handling
- browser-action isolation

Do **not** directly import:
- giant prompt assembly monoliths
- tightly coupled runtime logic
- high-risk browser behavior into the core
- proprietary/trademarked product identity

### OpenClaw

Use OpenClaw for lessons in:
- local-first assistant/operator behavior
- autonomy-loop UX and operating model
- daemon/process packaging ideas
- developer ergonomics for continuous assistance

Do **not** directly import:
- whole runtime subsystems without contracts
- packaging assumptions that conflict with the canonical architecture
- anything that bypasses policy mediation or receipts

### MCP Servers

Use `modelcontextprotocol/servers` for:
- MCP server examples
- capability patterns
- implementation references for tools/resources/prompts
- host-client-server shape

This remains an external reference repo, not core code.

### Claude Code Templates / Skills / Open SWE

Use these for:
- prompt and task decomposition patterns
- reusable skill/module packaging
- SWE-agent sequencing ideas
- examples of how to package repeatable workflows

These are donors of patterns, not architectural truth.

---

## External Platform / Integration Repos

These should stay outside the core and be used through adapters or documented interfaces.

### Supabase

Use for:
- durable storage target
- hosted database/auth/storage capabilities
- future memory or application services

Keep Supabase external. The core brain should not become Supabase-specific.

### MCP Installer

Use for:
- convenience installation workflows
- reference on packaging/distribution ergonomics

This is a helper, not part of the core system.

---

## Owned-Adjacent Repos

These repos are user-controlled and can become future subsystems, but they still should not be blindly merged into `refactored-system`.

### `code-companion`
Potential use:
- editor companion adapter
- coding-sidecar integration
- operator-assistance bridge

### `TabbyML`
Potential use:
- local model serving path
- code intelligence adapter
- private inference fallback

### `Performance-Optimization-System-`
Potential use:
- profiling and optimization flows
- telemetry or performance policy experiments

### `neurokernel`
Potential use:
- experimental cognition/orchestration ideas
- future control-plane or reasoning-plane research

### Rule

Owned-adjacent repos may become adapters or subsystems only when:
- a clear interface exists
- the integration policy is defined
- the contract boundary is written down
- the build order says it is in scope

---

## Merge Policy

### Allowed
- pattern extraction
- selective code reuse with attribution and license preservation
- adapter wrapping
- interface-level reuse
- tests/examples used as reference

### Not allowed
- whole-repo dumping into `refactored-system`
- merging multiple donor runtimes into one monolith
- copying code without preserving license obligations
- letting external repos define the canonical architecture
- bypassing the state machine, policy layer, or schema contracts

---

## Extraction Workflow

When mining a reference repo, follow this exact sequence:

1. Inspect repo purpose and strongest reusable patterns
2. Extract lessons into a reference doc
3. Classify candidate code or patterns as:
   - adopt now
   - rewrite later
   - reference only
   - reject
4. Add any actual copied code under clear attribution
5. Wrap adopted code behind your own contracts/adapters
6. Keep the canonical design in `refactored-system`

---

## Suggested Reference Docs

Maintain these files under `docs/reference/`:

```text
GOBII_LESSONS.md
OPENCLAW_LESSONS.md
MCP_PATTERNS.md
THIRD_PARTY_ATTRIBUTION.md
```

Use these docs to record:
- what to borrow
- what to reject
- what was actually reused
- what licensing/attribution requirements apply

---

## Decision Rules

Use these rules when deciding whether a repo should influence the core:

1. Does it strengthen the control plane without turning it into a monolith?
2. Does it fit the state machine and contract model?
3. Can it be isolated behind an adapter or subsystem boundary?
4. Does it preserve approval, receipts, and verification?
5. Can it be adopted without dragging in unrelated architecture?

If the answer is no, keep it reference-only.

---

## Immediate Repo Plan

### Canonical core
- `refactored-system`

### First donor/reference repos to read closely
- `gobii`
- `openclaw`
- `modelcontextprotocol/servers`
- `langchain-ai/open-swe`

### External platform docs to rely on
- Supabase docs/platform
- MCP official docs
- OpenAI official docs
- FastMCP docs
- Langfuse docs
- LlamaIndex docs

### Owned-adjacent repos to evaluate later
- `code-companion`
- `TabbyML`
- `Performance-Optimization-System-`
- `neurokernel`

---

## Final Rule

The question is not:

> "Can this repo be merged into my system?"

The real question is:

> "What exact value does this repo provide, and what is the cleanest contract boundary for using it without contaminating the core?"

That rule keeps the system sovereign.
