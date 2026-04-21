# OBSERVABILITY MINIMUMS

## Purpose
Define the minimum telemetry, receipt, and artifact linkage required for a run to be considered production-grade.

## Minimum answerability standard
Every production-grade run must be able to answer:
- what task was requested
- what context was loaded
- what plan was approved
- what tools and providers were used
- what artifacts were produced
- what verification was run
- what memory was written
- why the final disposition was reached

## Required identifiers
Each run must have:
- run_id
- task_id
- plan_id
- step_id[]
- tool_receipt_id[]
- artifact_id[]
- verification_id[]
- approval_id[]
- memory_write_id[]

## Hard rule
If a run cannot be traced, replayed, and audited, it is not production-grade.
