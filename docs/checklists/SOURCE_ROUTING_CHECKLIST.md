# Source Routing Checklist for AI Assistant Outputs

**Purpose:** To ensure that all knowledge retrieval and reasoning tasks adhere to the project's source‑tier doctrine. Always complete this checklist *before* producing a final response or artifact.

**Reference:** Module 15: Operational Metareasoning and Source Arbitration ([docs/reference/MODULE_15_OPERATIONAL_METAREASONING.md](../reference/MODULE_15_OPERATIONAL_METAREASONING.md))

---

## Step 1: Classify the Query or Task

First, identify the primary knowledge need. Use the table below to map your task to the correct starting tier.

| If the Task is... | Preferred Source Tier (Start Here) | Rationale |
| :--- | :--- | :--- |
| **Understanding intended design, patterns, or rules** (e.g., "Should we use this pattern?", "What is our policy on...?") | **Tier 1: Canonical Architecture** | `docs/architecture/` defines the *intent*. |
| **Diagnosing a failure, verifying current state, or checking runtime behavior** (e.g., "Why did the build fail?", "Is the service running?") | **Tier 2: Runtime Truth** | Logs and tests are the source of *truth for state*. |
| **Identifying current dependencies, configurations, or build steps** (e.g., "What version of Python do we use?", "How do I run the tests?") | **Tier 3: Build Documentation** | `pyproject.toml`, `Makefile`, and build docs define the *target*. |
| **Gathering context from donor repos, past experiments, or external research** (e.g., "How did `donor-repo` solve this?", "What do the benchmarks say?") | **Tier 4: Reference Lessons** | These are *advisory*; they do not dictate design. |
| **Retrieving vendor‑specific specifications or model capabilities** (e.g., "What does the model card say?", "What is the API limit?") | **Tier 5: External Registries** | Contextual and vendor‑controlled. |

---

## Step 2: Execute the Routing Decision

Follow this decision tree for the identified starting tier:

1.  **Retrieve from the *Preferred Tier***.
    - [ ] Is a relevant source found in this tier?
        - **Yes:** Continue to Step 3.
        - **No:** Proceed to the next lower tier (e.g., Tier 1 → Tier 2). If no source is found across all relevant tiers, state this as a `SOURCE_GAP` and do not fabricate an answer.

2.  **Perform Freshness Check** (for Tiers 1, 3, and 4).
    - [ ] Has the document been verified or updated in the last **30 days**?
        - **Yes:** Continue.
        - **No:** Add a `⚠️ STALE_SOURCE` warning to your output.

3.  **Perform Conflict Detection** (if multiple sources are found).
    - [ ] Do Tier 1 (Canonical) and Tier 2 (Runtime) disagree on the *same assertion*?
        - **Yes:** **Escalate to Tier 1.** The Canonical document defines the intended state. Treat the Runtime disagreement as a **bug or implementation gap** to be flagged, not a reason to override the Canonical source.
    - [ ] Do two sources in the *same tier* conflict?
        - **Yes:** This is an inconsistency. **Flag for human review** (`NEEDS_CLARIFICATION`).

4.  **Document Provenance**.
    - [ ] Proceed to **Artifact 2 (Receipt Template)** to structure your output.

---

## Step 3: Anti‑Fragmentation Check (Before Final Output)

Before posting a comment, creating a document, or closing a ticket, verify the placement:

- [ ] **If this is a durable decision or specification:** Is it being placed in **GitHub** (Markdown, ADR, PR, or Issue)? (If you are about to put this only in Slack, stop and reconsider.)
- [ ] **If this is a transient summary or triage note:** Does it include a **link** to the canonical GitHub artifact?
- [ ] **If this is a design narrative:** Does the Notion page link back to the source GitHub ADRs?

---

**Checklist Completion Signature:**
- **Task:** `[Task Description]`
- **Primary Source Used:** `[Tier] - [File Path/URL]`
- **Freshness:** `[Fresh / Stale]`
- **Confidence:** `[High / Medium / Low]`
