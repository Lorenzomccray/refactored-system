# /kb/safety

## Purpose

This page defines guardrails, approval gates, rollback strategy, risk classification, and fail-closed rules for `refactored-system`.

## Scope

This page governs runtime safety posture for risky action.

## Facts from current project doctrine

### Core safety statements
- Approval is not a feeling; it is a policy decision against a classified action.
- Every execution step must be assigned exactly one primary risk class before authorization.
- If a step cannot be classified, it must not execute.
- Fail closed rather than improvising unsafe execution.

### Canonical risk classes
- READ_ONLY
- LOCAL_WRITE
- LOCAL_EXECUTION
- EXTERNAL_API_CALL
- DATABASE_MUTATION
- BROWSER_AUTOMATION
- CREDENTIAL_USE
- IRREVERSIBLE

### Risk-class combination rule
If a step contains more than one action class, choose the highest-risk class.

Priority order:
IRREVERSIBLE > CREDENTIAL_USE > BROWSER_AUTOMATION > DATABASE_MUTATION > LOCAL_EXECUTION > EXTERNAL_API_CALL > LOCAL_WRITE > READ_ONLY

## Canonical safety rules

### 1. Approval gates
- READ_ONLY: generally allowed by default
- LOCAL_WRITE: human approval required
- LOCAL_EXECUTION: human approval required
- EXTERNAL_API_CALL: approval required unless explicitly allowlisted and read-only
- DATABASE_MUTATION: approval required
- BROWSER_AUTOMATION: approval required
- CREDENTIAL_USE: approval required unless already explicitly authorized for that exact capability
- IRREVERSIBLE: blocked by default and requires elevated approval

### 2. Sandbox rules
- LOCAL_EXECUTION requires sandbox unless explicitly exempted
- LOCAL_WRITE strongly prefers sandbox
- BROWSER_AUTOMATION requires sandbox or isolated browser worker
- DATABASE_MUTATION prefers staging or sandboxed target when possible

### 3. Receipt and audit rules
- risky actions require receipts
- credential access requires secret-access logging and output redaction
- external and browser actions require stronger evidence capture

### 4. Verification binding
- state-changing and high-risk actions must bind to authorization, execution, and verification receipts
- ambiguity should resolve to block, defer, or fail closed, not silent continuation

### 5. Escalation rules
Escalate when:
- risk class is IRREVERSIBLE
- multiple high-risk classes are combined
- credential use is combined with external action
- target is production
- verifier confidence is low
- rollback is unclear
- billing, auth, secrets, or persistent customer data are affected

### 6. Rollback strategy
- prefer reversible paths
- prefer staging targets for database mutation and risky local execution
- if rollback is unclear and risk is high, do not proceed without escalation
- irreversible operations default to deny unless the elevated path is explicit

## Boundaries

### This page does decide
- risk-class-based safety posture
- approval, sandbox, receipt, and escalation expectations
- fail-closed default stance

### This page does not decide
- exact UI or human-review mechanism
- exact secret manager implementation
- exact staging environment implementation

## Cross-references
- `/kb/principles`
- `/kb/repo-rules`
- `/kb/validation`
- `/kb/schemas`
- `/kb/workflows`

## Assumptions
- The project wants safety rules to become runtime law, not just advisory notes.
- Elevated approval for irreversible actions will be defined more concretely later.
- Production-target detection will eventually be explicit rather than inferred.

## Open questions
- What exact conditions create an exemption for sandboxed local execution?
- How should allowlisted read-only external API calls be registered and audited?
- What is the precise elevated-approval workflow for irreversible or production-impacting actions?
