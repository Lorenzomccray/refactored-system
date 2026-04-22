# CURRENT_REPO_MAP
## Runtime truth for the current repository layout

## Status date
2026-04-22

## Top-level directories

| Directory | Purpose | Status |
|-----------|---------|--------|
| `/app` | Application code — agents, orchestrator, tools, providers | Active |
| `/build` | Implementation targets and bounded build docs | Active |
| `/docs` | Canonical documentation | Active |
| `/docs/reference` | Non-canonical lessons and analogies | Active |
| `/kb` | Maintained knowledge base | Active |
| `/memory` | Project memory and precedent summaries | Active |
| `/runtime` | Current state truth files | Active |
| `/sources` | External doc registries and remote surfaces | Active |
| `/tests` | Automated verification | Active |
| `/tools` | Developer utilities and local scripts | Stub — no content yet |

## Key top-level files

| File | Purpose |
|------|---------|
| `REPO_MANIFEST.md` | Navigation map for humans and AI agents |
| `AGENTS.md` | Retrieval and execution behavior for development agents |
| `README.md` | Project overview and setup instructions |
| `main.py` | Application entry point |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment variable template |
| `install.sh` | Installation helper script |

## Application structure (`/app`)

See `kb/architecture.md` for component details.

## Known layout gaps

* `/tools` directory exists but contains no scripts yet.
* `docs/SOURCE_AUTHORITY_MATRIX.md` and `docs/SOURCE_CONFLICT_POLICY.md` are newly created stubs.
* `build/` contains only `V1_SOURCE_GOVERNANCE_BOOTSTRAP.md`; V1 planner/patch/execution docs are stubs.

## Update rule

Update this file whenever the top-level layout changes or a directory's status changes.
