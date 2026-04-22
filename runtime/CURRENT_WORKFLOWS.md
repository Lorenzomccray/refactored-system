# CURRENT_WORKFLOWS
## Runtime truth for active workflows in the project

## Status date
2026-04-22

## Active workflows

### Source governance bootstrap
* **Status**: In progress
* **Goal**: Land KB + canonical docs + runtime truth files into the repo before deeper code changes
* **Build doc**: `build/V1_SOURCE_GOVERNANCE_BOOTSTRAP.md`
* **Acceptance criteria**: Assistant can answer "where should I look first?" without ambiguity

### Agent runtime (Planner → Builder → Verifier)
* **Status**: Functional baseline in `app/`
* **Goal**: Orchestrate complex tasks using chained specialized agents
* **Entry point**: `main.py`
* **See**: `kb/architecture.md`, `kb/workflows.md`

## Inactive / pending workflows

* V1 Safe Planner — stub, not yet active (`build/V1_SAFE_PLANNER.md`)
* V1 Patch Proposal — stub, not yet active (`build/V1_PATCH_PROPOSAL.md`)
* V1 Approved Execution — stub, not yet active (`build/V1_APPROVED_EXECUTION.md`)

## Workflow rule

Do not treat a workflow as active until it is listed here with an "Active" status.
Update this file when a workflow is started, paused, or completed.

## Related files

* `runtime/CURRENT_TOOLS.md` — what is actually callable in active workflows
* `runtime/CURRENT_BLOCKERS.md` — what is blocking active workflows
* `kb/workflows.md` — operational workflow guidance
