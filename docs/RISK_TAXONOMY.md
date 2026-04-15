# RISK_TAXONOMY
## Runtime Action Classification and Approval Rules

---

## 1. Purpose

This document defines the canonical risk classes for all planned and executable actions.

The purpose is to ensure:
- approval is policy-driven
- risky actions are classified consistently
- tool and model choices can be constrained by class
- logging and verification requirements are explicit
- sandboxing is not optional where required

Approval is not a feeling.
Approval is a policy decision against a classified action.

---

## 2. Core Rule

Every execution step must be assigned exactly one primary risk class before authorization.

If a step cannot be classified, it must not execute.

---

## 3. Canonical Risk Classes

### 3.1 READ_ONLY

Represents:
- reading files
- listing directories
- retrieving docs
- querying memory
- inspecting configuration
- non-mutating analysis

#### Default policy
- allowed by default
- no human approval required
- sandbox preferred but not always required
- receipt required
- verifier required only when the read informs a critical decision

---

### 3.2 LOCAL_WRITE

Represents:
- creating files
- editing files
- applying patches
- writing configs
- generating docs into the repo
- mutating local state without external side effects

#### Default policy
- human approval required
- sandbox strongly preferred
- receipt required
- syntactic verification required
- environment verification required if write success is claimed

---

### 3.3 LOCAL_EXECUTION

Represents:
- running shell commands
- invoking local binaries
- running tests
- building packages
- restarting local services
- executing scripts

#### Default policy
- human approval required
- sandbox required unless explicitly exempted
- receipt required
- syntactic + environment verification required
- timeout mandatory

---

### 3.4 EXTERNAL_API_CALL

Represents:
- HTTP requests to third-party APIs
- provider calls other than the core model path
- webhook invocation
- external service mutation or retrieval

#### Default policy
- approval required unless explicitly allowlisted and read-only
- credential use policy applies
- receipt required
- verifier required when response affects downstream execution
- audit log mandatory

---

### 3.5 DATABASE_MUTATION

Represents:
- inserts
- updates
- deletes
- schema changes
- queue/job mutations
- persistent state changes in DB-backed systems

#### Default policy
- approval required
- sandbox or staging target preferred
- receipt required
- environment verification required
- rollback plan preferred

---

### 3.6 BROWSER_AUTOMATION

Represents:
- browser navigation with intent to act
- clicking, submitting, uploading, downloading
- authenticated browser tasks
- CAPTCHA-adjacent flows
- web app automation

#### Default policy
- approval required
- sandbox or isolated browser worker required
- strict domain policy required
- receipt required
- environment verification required where possible

#### Note
This is a high-risk surface and should never bypass policy mediation.

---

### 3.7 CREDENTIAL_USE

Represents:
- reading secrets
- injecting tokens
- signing requests
- authenticating to protected services
- using SSH/API keys

#### Default policy
- approval required unless already explicitly authorized by policy for that exact capability
- receipt required
- secret access logging required
- output redaction required
- least-privilege tool path required

---

### 3.8 IRREVERSIBLE

Represents:
- destructive deletes
- production-impacting changes without rollback
- data-destroying operations
- external actions with durable consequences
- anything with no reliable reversal path

#### Default policy
- blocked by default
- explicit elevated approval required
- stronger verifier and policy review required
- detailed receipt and justification required
- fail closed on ambiguity

---

## 4. Classification Matrix

| Risk Class         | Default | Approval | Sandbox | Receipt | Verifier | Notes |
|--------------------|---------|----------|---------|---------|----------|-------|
| READ_ONLY          | Allow   | No       | Prefer  | Yes     | Optional | Safe inspection only |
| LOCAL_WRITE        | Review  | Yes      | Prefer  | Yes     | Yes      | File/config mutation |
| LOCAL_EXECUTION    | Review  | Yes      | Yes     | Yes     | Yes      | Commands/tests/builds |
| EXTERNAL_API_CALL  | Review  | Usually  | N/A     | Yes     | Often    | Credential and audit rules apply |
| DATABASE_MUTATION  | Review  | Yes      | Prefer  | Yes     | Yes      | Persistent state change |
| BROWSER_AUTOMATION | Review  | Yes      | Yes     | Yes     | Yes      | High-risk external interaction |
| CREDENTIAL_USE     | Review  | Yes      | N/A     | Yes     | Context  | Secret access must be logged |
| IRREVERSIBLE       | Block   | Elevated | Case-by-case | Yes | Yes   | Default deny |

---

## 5. Derived Policy Flags

For every classified action, derive:

```yaml
allowed_by_default: boolean
approval_required: boolean
sandbox_required: boolean
receipt_required: boolean
verification_required: boolean
escalation_required: boolean
```

These are computed from the class, not improvised by the agent.

---

## 6. Escalation Rules

Escalation is required when any of the following are true:

- risk class is `IRREVERSIBLE`
- multiple high-risk classes are combined in one step
- credential use plus external action is involved
- environment target is production
- verifier confidence is low
- rollback is unclear
- the step affects billing, auth, secrets, or persistent customer data

---

## 7. Tool Policy Binding

Every tool must declare:
- the highest risk class it can perform
- whether it supports sandbox mode
- what verification hooks it emits
- whether it can run without human review under any conditions

If a tool does not declare this, it cannot be registered.

---

## 8. Provider Policy Binding

Provider routing may be constrained by risk class.

Examples:
- `READ_ONLY` can use cheaper summarization/research models where allowed
- `LOCAL_WRITE` and `LOCAL_EXECUTION` should use stronger structured-output paths
- `CREDENTIAL_USE` should avoid providers or contexts that violate privacy policy
- `IRREVERSIBLE` must not proceed without elevated authorization regardless of model

---

## 9. Combination Rules

If a step contains more than one action class, choose the highest-risk class.

Priority order:

```text
IRREVERSIBLE
CREDENTIAL_USE
BROWSER_AUTOMATION
DATABASE_MUTATION
LOCAL_EXECUTION
EXTERNAL_API_CALL
LOCAL_WRITE
READ_ONLY
```

---

## 10. Immediate Build Priority

Implement first:
- classifier function
- risk-class enum
- policy matrix
- derived flags
- audit logging for classification

This turns approval from a prompt habit into a real runtime law system.
