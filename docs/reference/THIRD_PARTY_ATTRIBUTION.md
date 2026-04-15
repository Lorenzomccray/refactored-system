# THIRD_PARTY_ATTRIBUTION

## Purpose

This document records third-party and donor sources that influence `refactored-system`, and defines how attribution, license hygiene, and reuse boundaries are handled.

It exists to prevent:
- undocumented code borrowing
- accidental license violations
- architecture drift caused by hidden donor dependencies
- confusion between canonical code and reference material

This file is a **reference and compliance aid**.

It is not a substitute for legal review where required.

---

## Canonical Rule

Only `refactored-system` is the canonical product repository.

Other repositories, docs, registries, and tutorials may influence the project as:
- references
- donors of patterns
- external platforms
- adapter targets

But they do not become canonical architecture by default. The project’s repo/source planning already establishes this separation. fileciteturn53file8 fileciteturn53file10

---

## Attribution Principles

### 1. Pattern learning is not the same as code copying

There are three levels of reuse:

#### A. Pattern learning
- Learn the idea
- Rebuild it independently
- No direct code carry-over

#### B. Selective adaptation
- Reuse a small portion of logic or structure
- Rewrite into local contracts and style
- Record the source and reason

#### C. Direct incorporation
- Copy or lightly modify actual third-party code
- Preserve license obligations
- Record exact source path, commit/tag if possible, and local destination

---

### 2. Donor repos do not define runtime law

Even when a donor repo is useful, it must not define:
- state machine semantics
- approval policy
- verification policy
- memory promotion rules
- canonical repository structure

Those belong to the project’s canonical docs. fileciteturn53file9

---

### 3. Prefer adapter boundaries over wholesale merges

The project’s current repo-options plan already makes this explicit: donor repos should be mined for patterns or wrapped through adapters rather than merged wholesale. fileciteturn53file10

#### Rule
If third-party value can be obtained through:
- an adapter
- a protocol boundary
- a narrow wrapper
- a rebuilt implementation

that is preferred over direct code import.

---

## Current Third-Party / Donor Inventory

The current project materials identify these external and adjacent repos as relevant sources. fileciteturn53file7

### Reference / donor repos
- `Lorenzomccray/gobii`
- `openclaw/openclaw`
- `modelcontextprotocol/servers`
- `langchain-ai/open-swe`
- `davila7/claude-code-templates`
- `mattpocock/skills`

### External platform / ecosystem repos
- `supabase/supabase`
- `anaisbetts/mcp-installer`

### Owned-adjacent repos
- `Lorenzomccray/code-companion`
- `Lorenzomccray/TabbyML`
- `Lorenzomccray/Performance-Optimization-System-`
- `Lorenzomccray/neurokernel`

These categories align with the project’s existing repo-options classification. fileciteturn53file10

---

## Source Categories And Attribution Rules

### 1. Official documentation sources

Examples from the current source registries include:
- OpenAI docs
- MCP official docs
- FastMCP docs
- LlamaIndex docs
- Langfuse docs
- Qdrant docs
- Weaviate docs fileciteturn53file2 fileciteturn53file3 fileciteturn53file6

#### Attribution rule
When these docs influence design:
- cite them in design notes or doc comments where helpful
- do not imply affiliation
- do not quote large protected passages unnecessarily
- prefer paraphrase and implementation against public interfaces/specs

---

### 2. Donor code repositories

Examples:
- Gobii
- OpenClaw
- MCP Servers
- Open SWE
- Claude code templates
- Skills repo fileciteturn53file7

#### Attribution rule
If code or near-code ideas are adopted:
- record the source repo
- record the feature/idea borrowed
- record whether it was pattern-only, rewritten, or directly adapted
- preserve upstream license requirements where applicable

#### Preferred path
Prefer:
- pattern extraction
- clean-room rewrite into local contracts
- narrow adaptation behind adapters

Avoid:
- whole-file dumps
- silent copy/paste into core modules
- mixed-origin files with no attribution notes

---

### 3. Community tutorials and articles

The source registries include community-tier MCP/tutorial sources as lower-trust references. fileciteturn53file3 fileciteturn53file6

#### Attribution rule
Use tutorials for:
- mental models
- onboarding ideas
- examples

Do not treat them as canonical authority over:
- specs
- runtime law
- compatibility guarantees

If a tutorial-inspired pattern is used, document it as “inspired by” rather than implying formal standard status.

---

### 4. Owned-adjacent repos

Owned-adjacent repos are still not automatically canonical. The repo-options plan already treats them as future adapters or subsystems, not blind merge targets. fileciteturn53file10

#### Attribution rule
When borrowing from owned-adjacent repos:
- still document origin
- still document whether code was copied, adapted, or only referenced
- still preserve boundaries between core and subsystem/adapters

Ownership does not remove the need for architectural discipline.

---

## Reuse Record Format

Whenever a third-party idea or code segment materially affects the project, add a note using this format:

```text
Source:
Type: pattern | adapted code | direct incorporation
Upstream repo/doc:
Upstream path/page:
Local destination:
Why reused:
What was changed:
License/notice action required:
Status: active | replaced | removed
```

---

## Minimal Attribution Ledger

Use this section as the living ledger.

### Gobii
- **Role**: donor/reference repo
- **Current usage status**: pattern learning and architecture lessons only
- **Likely reusable areas**: prompt/context assembly discipline, persistence ideas, compaction, model failover, modular tooling
- **Direct code merged?**: no, not by default
- **Relevant docs**: `GOBII_LESSONS.md`

### OpenClaw
- **Role**: donor/reference repo
- **Current usage status**: product/runtime pattern reference only
- **Likely reusable areas**: local-first behavior, persistent assistant feel, service ergonomics, operator continuity
- **Direct code merged?**: no, not by default
- **Relevant docs**: `OPENCLAW_LESSONS.md`

### MCP official ecosystem / servers
- **Role**: standard + reference implementation ecosystem
- **Current usage status**: protocol and adapter guidance
- **Likely reusable areas**: host/client/server boundaries, narrow server packaging, tool/resource metadata, interoperability
- **Direct code merged?**: no by default
- **Relevant docs**: `MCP_PATTERNS.md`

### Supabase
- **Role**: external platform
- **Current usage status**: platform/integration reference
- **Likely reusable areas**: storage platform integration, external service boundary
- **Direct code merged?**: should remain external unless a specific OSS component is intentionally vendored

### Open SWE / Skills / Claude templates
- **Role**: workflow and pattern donors
- **Current usage status**: reference only
- **Likely reusable areas**: decomposition patterns, module/skill packaging, workflow ergonomics
- **Direct code merged?**: no by default

### Owned-adjacent repos
- **Role**: future subsystem or adapter candidates
- **Current usage status**: evaluate later
- **Direct code merged?**: no blind merges

---

## License Hygiene Rules

### 1. Preserve upstream notices when directly incorporating code

If actual third-party code is incorporated:
- keep required copyright/license notices
- keep license text where required
- note modifications where appropriate

### 2. Do not assume public GitHub means unrestricted reuse

Public visibility does not erase license obligations.

### 3. Prefer minimal incorporation

If you can implement the same idea cleanly without copying code, prefer that.

### 4. Avoid unclear provenance
n
If you cannot identify where a block came from, do not merge it into canonical core files until provenance is restored.

---

## Architectural Boundary Rules

When third-party influence enters the project, preserve these boundaries:

1. **Canonical docs override donor assumptions**
2. **Adapters override hard dependencies**
3. **Typed contracts override donor object models**
4. **Policy mediation overrides donor execution shortcuts**
5. **Receipts and verification override donor success claims**

These rules are already required by the master architecture and source-system blueprint. fileciteturn53file9 fileciteturn53file8

---

## What Should Be Documented Immediately When Reuse Happens

Document reuse when any of the following occur:
- a third-party function is copied or translated
- an external schema materially influences local schemas
- a donor repo changes the shape of a subsystem
- a third-party prompt template becomes operationally important
- a protocol or server implementation is wrapped directly
- vendored code enters the repo

---

## What Does Not Need Formal Attribution Notes Every Time

These usually do **not** need per-line ledger entries:
- broad architectural inspiration
- standard protocol usage from public specs
- ordinary use of public APIs/doc references
- general design ideas that were rebuilt independently

Still, when in doubt, record the source once in this file or the relevant reference doc.

---

## Practical Workflow For Safe Reuse

1. Inspect donor source
2. Decide whether value is:
   - pattern only
   - rewrite candidate
   - adapter target
   - direct incorporation candidate
3. Record it in the relevant reference doc
4. If direct incorporation occurs, update this attribution ledger
5. Keep the local implementation aligned to canonical docs, not donor structure

---

## Final Rule

The project should be able to answer this question at any time:

> “Which parts of this system are truly ours, which are inspired by others, and which directly depend on external sources?”

If that answer is unclear, attribution discipline is not strong enough yet.
