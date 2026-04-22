# AGENTS.md

## Purpose
This file defines retrieval and execution behavior for development agents working in this repository.

## Source order
1. `kb/*`
2. canonical docs in `docs/`
3. runtime truth in `runtime/`
4. active build docs in `build/`
5. external source registries in `sources/`
6. memory only when the above do not answer the question

## Hard rules
- Treat chats as working memory, not canonical truth.
- Prefer runtime docs for current-state questions.
- Consult safety, validation, risk taxonomy, and receipt rules before state-changing recommendations.
- Surface conflicts explicitly when KB, canonical docs, runtime docs, or external docs disagree.
- Keep architecture boundaries intact; do not merge external systems into the brain without an adapter boundary.

## OpenAI docs MCP usage rule
Always use the OpenAI developer documentation MCP server when work touches the OpenAI API, Apps SDK, Codex, MCP integrations, tools, rules, or agent runtime behavior.
