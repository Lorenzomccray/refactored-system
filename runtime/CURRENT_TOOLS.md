# CURRENT_TOOLS
## Concrete runtime truth for callable and trusted tool surfaces

## Status date
2026-04-22

## Purpose
This file records what is actually callable, usable, or trustworthy for project work.
It is current-state truth, not aspiration.

## Callable tool surfaces confirmed in project notes
- Airtable: operationally set up as the active structured ops surface
- Chat/project conversation: active working-memory layer
- Local artifact generation: available through file-based output bundles

## Connector surfaces not confirmed callable in the documented setup pass
- Linear: not currently callable in that pass
- Slack: not currently callable in that pass
- Notion: not currently callable in that pass

## Structured ops layer already created
- Work Queue
- Execution Receipts
- Reference Log
- Decision Log

## Source surfaces available to the assistant in project context
- Canonical docs in `docs/`
- KB pages in `kb/`
- Runtime truth docs in `runtime/`
- Build docs in `build/`
- External registries in `sources/`

## Tool-trust rule
- Prefer canonical docs first
- Prefer runtime truth docs for current-state questions
- Use chat only as working context
- Treat unsupported/unconfirmed connectors as unavailable until revalidated

## Known limitation
The last validated live setup pass had only Airtable confirmed as an operational orchestration connector.
Do not assume broader connector availability without fresh validation.
