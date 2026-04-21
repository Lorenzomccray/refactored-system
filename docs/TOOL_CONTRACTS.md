# TOOL CONTRACTS

## Purpose
Define the canonical contract every tool must satisfy before it may be registered, planned, authorized, executed, or verified by the core brain.

## Core rule
No agent may call a tool directly.

Every tool invocation must flow through:

```text
plan → authorization → execution wrapper → receipt → verification
```

## Required tool declaration
Every tool must declare all of the following:
- capability name
- version
- owner
- input schema
- output schema
- risk class
- approval level
- timeout
- retry policy
- verification method
- receipt format
- artifact outputs
- secret requirements
- sandbox requirements

## Canonical tool contract

### Metadata
- `tool_name`
- `tool_version`
- `tool_category`
- `description`
- `owner`

### Inputs
- canonical input schema
- validation rules
- required fields
- optional fields
- normalization rules

### Outputs
- canonical output schema
- error schema
- artifact references
- receipt references

### Execution policy
- risk class
- approval requirement
- sandbox requirement
- allowed environments
- timeout
- retry behavior
- max concurrency if applicable

### Verification policy
- syntactic check
- semantic check
- environment check
- success criteria

### Audit and receipts
Each tool run must emit:
- `tool_receipt_id`
- `run_id`
- `task_id`
- `step_id`
- tool name and version
- normalized input summary
- normalized output summary
- start and end timestamps
- verifier linkage
- artifact linkage
- error state if applicable

## Tool categories
- shell tools
- browser tools
- file tools
- api tools
- db tools
- memory tools
- mcp tools
- automation tools

## Hard rules
- No undeclared tool may execute.
- No tool may mutate state without a declared risk class.
- No tool may bypass approval if approval is required by policy.
- No tool may return opaque strings where a typed output schema exists.
- No tool success may be accepted without verification.
- No tool may write secrets into receipts, artifacts, or memory.

## Registration rule
A tool is only considered active when all of the following exist:
1. contract definition
2. schema validation
3. policy mapping
4. receipt mapping
5. verification mapping
6. runtime registration entry

## Minimal implementation milestone
The first working milestone is one mock tool that proves the full flow:
- plan
- authorize
- execute
- receipt
- verify
