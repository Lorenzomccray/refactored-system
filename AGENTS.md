# AGENTS.md

## Purpose
This file defines retrieval and execution behavior for development agents working in this repository.

## Route first, then resolve authority
Routing order and authority order are not the same thing.

Use `docs/source-governance/CORE_SOURCES_INDEX.md` and `kb/index.md` to route.
Use `docs/source-governance/SOURCE_AUTHORITY_MATRIX.md` and `docs/source-governance/SOURCE_CONFLICT_POLICY.md` to resolve conflicts.

## Routing order
1. `docs/source-governance/CORE_SOURCES_INDEX.md`
2. `kb/index.md`
3. relevant canonical docs in `docs/`
4. runtime truth in `runtime/truth/`
5. active build docs in `build/`
6. external source registries in `sources/`
7. memory only when the above do not answer the question

## Authority order
1. runtime truth
2. canonical repo docs
3. maintained KB
4. project memory
5. remote official docs
6. derived summaries
7. raw dumps and transcripts

## Hard rules
- Treat chats as working memory, not canonical truth.
- Prefer runtime truth docs for current-state questions.
- Consult safety, validation, risk taxonomy, and receipt rules before state-changing recommendations.
- Surface conflicts explicitly when stronger and weaker sources disagree.
- Keep architecture boundaries intact; do not merge external systems into the brain without an adapter boundary.

## OpenAI docs MCP usage rule
Always use the OpenAI developer documentation MCP server when work touches the OpenAI API, Apps SDK, Codex, MCP integrations, tools, rules, or agent runtime behavior.
