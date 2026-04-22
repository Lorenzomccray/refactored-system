# /kb/validation

## Purpose

This page defines verification standards including tests, schema checks, smoke tests, and rollback checks for `refactored-system`.

## Scope

This page governs how the project decides whether a claim of success is justified.

## Facts from current project doctrine

### Validation policy from schemas
- Contracts must be validated before crossing plane boundaries.
- Validation must fail closed.
- Invalid contracts must produce a FailureRecord.
- The verifier must not attempt semantic validation if syntactic validation already failed.

### Verification layers from architecture
- Syntactic verification checks schema validity, parseability, required fields, and artifact existence.
- Semantic verification checks whether the result matches the requested goal and plan intent without major omissions or contradictions.
- Environment verification checks whether claimed real-world state change actually happened.

### Receipt binding
Every state-changing or high-risk action must bind to:
- an authorization receipt
- an execution receipt
- a verification receipt

## Canonical validation rules

### 1. Schema validation
Use for:
- Task
- Plan
- ExecutionGraph
- ExecutionStep
- ToolCall
- ToolResult
- ApprovalRequest
- ApprovalDecision
- VerificationResult
- MemoryRecord
- RunReceipt
- FailureRecord

Rule:
- no cross-plane boundary crossing without successful schema validation

### 2. Syntactic validation
Examples:
- payload structure is valid
- fields required by contract are present
- artifacts referenced actually exist
- output is parseable where claimed

### 3. Semantic validation
Examples:
- output matches the actual request
- result respects plan intent and constraints
- major omissions or contradictions are surfaced

### 4. Environment validation
Examples:
- file actually changed
- command actually ran
- service actually restarted
- API side effect actually occurred
- database row actually mutated

### 5. Smoke validation
Use for early slices:
- repo imports or startup
- basic orchestrator path
- contract creation path
- receipt writer path
- approval classification path

### 6. Rollback checks
Required or strongly preferred when:
- database mutation occurs
- local execution affects persistent services
- local write changes config or critical files
- irreversible risk is approached and must be blocked or specially escalated

## Minimum validation expectations by action type
- READ_ONLY: schema plus targeted semantic checks as needed
- LOCAL_WRITE: schema plus syntactic plus environment checks
- LOCAL_EXECUTION: schema plus syntactic plus environment checks, with timeout
- EXTERNAL_API_CALL: schema plus semantic and or environment checks when downstream state depends on result
- DATABASE_MUTATION: schema plus environment plus rollback awareness
- BROWSER_AUTOMATION: schema plus environment checks where possible, with strict evidence capture
- CREDENTIAL_USE: schema plus audit and redaction checks
- IRREVERSIBLE: fail closed unless elevated review and strongest practical validation are present

## Boundaries

### This page does decide
- what must be verified
- how verification is split
- minimum standards for success claims

### This page does not decide
- exact test runner or framework
- exact CI job structure
- exact artifact storage backend

## Cross-references
- `/kb/schemas`
- `/kb/safety`
- `/kb/checklists`
- `/kb/workflows`
- `/kb/precedents`

## Assumptions
- Validation will expand from doc-first rules into executable checks as the repo matures.
- Smoke checks are valuable early even before full environment automation exists.
- Verification evidence will increasingly rely on receipts and artifacts rather than narration.

## Open questions
- What is the minimum V1 smoke suite?
- Which environment checks should be mandatory before claiming local service success?
- Should rollback checks be formalized as contracts or checklist items first?
