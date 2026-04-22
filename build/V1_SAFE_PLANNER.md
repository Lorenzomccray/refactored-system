# V1 SAFE PLANNER

## Purpose

Define a safe, validated planning process for V1 changes before any execution begins.

## Status
Stub — not yet active.

## Goal

Ensure that every V1 change is planned, reviewed, and approved before any code or state modification occurs.

## Planning gates

1. Identify the change scope and affected files.
2. Check `runtime/CURRENT_BLOCKERS.md` — do not proceed if a relevant blocker is open.
3. Validate against `kb/safety.md` and `docs/RISK_TAXONOMY.md`.
4. Produce a patch proposal in `build/V1_PATCH_PROPOSAL.md`.
5. Obtain approval before executing — see `build/V1_APPROVED_EXECUTION.md`.

## Non-goals

* This file does not authorize execution.
* This file does not replace the approval step.

## Related files

* `build/V1_PATCH_PROPOSAL.md`
* `build/V1_APPROVED_EXECUTION.md`
* `docs/RISK_TAXONOMY.md`
* `kb/safety.md`
* `kb/validation.md`
