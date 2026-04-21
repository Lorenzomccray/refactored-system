# VERIFICATION MODEL

## Purpose
Define how the system determines whether execution actually succeeded in reality rather than only appearing successful in logs or model output.

## Core rule
No execution may be called successful without verification.

Verification is not a single boolean. It has layers.

## Verification layers

### 1. Syntactic verification
Checks:
- schema validity
- parseability
- required fields present
- artifacts exist
- receipt shape valid

### 2. Semantic verification
Checks:
- result matches requested goal
- output meaning matches plan intent
- no major omissions or contradictions
- response is not merely plausible but relevant to the requested step

### 3. Environment verification
Checks:
- file actually changed
- command actually ran
- process actually restarted
- service actually responded
- state actually persisted
- browser action produced the expected page state when applicable

## Canonical verifier outputs
Every verification pass must emit:
- `verification_id`
- `run_id`
- `task_id`
- `step_id`
- verification layer
- status
- evidence summary
- artifact references
- failure reason if any

## Verification decision model
A step is only successful when:
1. syntactic verification passes
2. semantic verification passes
3. environment verification passes when the step touches reality

If one layer is not applicable, that must be recorded explicitly.

## Failure handling
If verification fails, the system may:
1. retry the same path
2. retry with narrowed scope
3. fall back to another provider or tool path
4. re-plan
5. fail closed with diagnostic artifact

## Hard rules
- Do not collapse all verification into one vague success flag.
- Do not trust planner or builder claims without receipts or artifacts.
- Do not promote memory or procedural knowledge from unverified runs.
- Do not let adapters define their own final success semantics.

## Minimal first milestone
Implement one verifier path that checks:
- schema validity
- receipt presence
- one environment effect for a mock tool

That is the minimum proof that the canonical verification plane is real.
