# Execution Receipt & Source Attribution Template

**Reference:** Module 15: Operational Metareasoning and Source Arbitration ([docs/reference/MODULE_15_OPERATIONAL_METAREASONING.md](../reference/MODULE_15_OPERATIONAL_METAREASONING.md))

**Instructions:** Copy and paste the block below at the end of every substantive AI assistant output. Replace the bracketed placeholders with the specific details from the task.

---

## 📋 Execution Receipt

| Field | Value |
| :--- | :--- |
| **Task ID / Context** | `[e.g., Issue #123, Slack thread link, or task description]` |
| **Action Executed** | `[Concise summary of what the assistant did or recommended]` |
| **Timestamp** | `[YYYY-MM-DD HH:MM UTC]` |

### 🔍 Source Attribution

| Field | Value |
| :--- | :--- |
| **Primary Tier** | `[CANONICAL / RUNTIME / BUILD / REFERENCE / EXTERNAL]` |
| **Primary Source(s)** | `[File path(s) or URL(s) used to ground the response]` |
| **Last Verified / Freshness** | `[Date of last known verification]` – `[Fresh / Stale (X days)]` |
| **Consulted (Secondary)** | `[List of other sources reviewed but not used as primary]` |
| **Confidence** | `[High / Medium / Low]` – `[Brief justification, e.g., "Canonical source fully addresses the query"]` |

### ⚠️ Warnings & Caveats

- `[List any staleness warnings, detected conflicts, or assumptions made]`
- `[Example: "Runtime logs conflict with Canonical ADR-004; Canonical intent preserved."]`

### 🔗 Output & Next Steps

- **Artifact(s) Generated:** `[Link to GitHub PR, Linear issue, or path to created document]`
- **Required Follow‑up:** `[Action items for the user or future assistant runs]`

---
**Verification:** This output adheres to the Source System Blueprint and Module 15 of the Living Grimoire.
