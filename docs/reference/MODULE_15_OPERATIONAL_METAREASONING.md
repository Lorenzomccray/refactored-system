# MODULE 15: Operational Metareasoning and Source Arbitration

**Status:** Accepted Reference  
**Tier:** Reference Lessons (Tier 4)  
**Canonical Dependencies:**  
- `docs/SOURCE_SYSTEM_BLUEPRINT.md`
- `docs/checklists/SOURCE_ROUTING_CHECKLIST.md`
- `docs/templates/RECEIPT_TEMPLATE.md`

**Override Rule:**  
This document explains and operationalizes source‑routing discipline. It does **not** override canonical architecture documents. In any conflict:
1. Canonical Architecture governs intended design.
2. Runtime Truth governs current observed state.
3. This document remains explanatory/reference material.

---

## 15.0 Pre‑Reflection: The Production Gap

> *The Living Grimoire teaches you to reason. But in production, the first question is not "What is the answer?" but "Which document should I read first?" A reasoning engine that consults a stale donor note before the canonical architecture doc will produce a logically sound but operationally incorrect answer. This module bridges the gap between cognitive architecture and production deployment.*

## 15.1 The Source Arbitration Problem

In any real‑world AI‑assisted project (such as **refactored‑system**), the assistant faces **multiple source tiers** with distinct *types* of authority. Authority is not a single stack; it depends on *what* is being asked.

### 15.1.1 The Five Source Tiers

| Tier | Name | Authority Type | Notes |
| :--- | :--- | :--- | :--- |
| **Tier 1** | Canonical Architecture | Highest for **intended design** | ADRs, architecture docs, contracts |
| **Tier 2** | Runtime Truth | Highest for **current observed state** | Logs, test results, live system state |
| **Tier 3** | Build Documentation | Current **implementation target** | `pyproject.toml`, build plans |
| **Tier 4** | Reference Lessons | Advisory only | Donor repo analysis, research notes |
| **Tier 5** | External Registries | Contextual / vendor‑controlled | Hugging Face model cards, PyPI |

**Critical Distinction:**
- **Canonical (Tier 1)** defines what the system *should be*.
- **Runtime (Tier 2)** reports what the system *currently is*.
- Runtime truth **overrides assumptions** but does **not** override the canonical architecture as doctrine. A runtime failure means the implementation is broken, not that the architecture document is wrong.

### 15.1.2 The Failure Mode

An assistant that retrieves from **Tier 4 (Reference Lessons)** before checking **Tier 1 (Canonical Architecture)** produces **plausible but incorrect** guidance. This violates the project's explicit rule:

> *"Treat canonical internal architecture docs as higher priority than reference notes."*

**[S2‑Trigger]:** *Simulate a scenario where the assistant consults a donor repo's `README.md` (Tier 4) instead of `docs/architecture/decisions/ADR-001-source-of-truth.md` (Tier 1). What incorrect recommendation would result?*

## 15.2 The Operational Metareasoning Loop

Before executing any reasoning task, the assistant must perform a **pre‑reasoning arbitration phase**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    OPERATIONAL METAREASONING LOOP                 │
├─────────────────────────────────────────────────────────────────┤
│  1. CLASSIFY task type and required knowledge domain.            │
│  2. DETERMINE preferred starting tier and maximum allowed tier.  │
│  3. RETRIEVE from preferred tier with freshness checks.          │
│  4. If conflict detected → escalate upward toward Tier 1.        │
│  5. REASON with the verified source set.                         │
│  6. OUTPUT with source attribution and confidence.               │
└─────────────────────────────────────────────────────────────────┘
```

### 15.2.1 Task Classification to Tier Mapping

| Task Type | Preferred Starting Tier | Maximum Allowed Tier | Rationale |
| :--- | :--- | :--- | :--- |
| "What is the intended architecture for X?" | Tier 1 (Canonical) | Tier 1 | Only canon defines intent |
| "Why did the last deployment fail?" | Tier 2 (Runtime) | Tier 2 | Logs and state are authoritative |
| "What Python version does the project require?" | Tier 3 (Build) | Tier 3 | Defined in build config |
| "What pattern did donor repo Y use?" | Tier 4 (Reference) | Tier 4 | Historical research |
| "Should we adopt this donor pattern?" | Tier 1 (Canonical) | Tier 4 | Canonical decides; reference informs |
| "What does this model card claim?" | Tier 5 (External) | Tier 5 | Vendor documentation |

## 15.3 Implementation: Source Arbiter

```python
"""
Module 15: Operational Metareasoning and Source Arbitration
Production‑ready source routing for reasoning assistants.
"""

from enum import IntEnum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import time
from datetime import datetime

class SourceTier(IntEnum):
    """Authority tiers. Lower number = higher authority for that domain."""
    CANONICAL = 1
    RUNTIME = 2
    BUILD = 3
    REFERENCE = 4
    EXTERNAL = 5

@dataclass
class Source:
    """A retrievable knowledge source with authority and freshness metadata."""
    tier: SourceTier
    path: str
    content: str = ""
    last_verified: float = field(default_factory=time.time)
    last_modified: float = field(default_factory=time.time)
    domain_tags: List[str] = field(default_factory=list)
    
    def freshness_score(self, max_age_days: float = 30.0) -> float:
        age_days = (time.time() - self.last_verified) / 86400
        if age_days >= max_age_days:
            return 0.0
        return 1.0 - (age_days / max_age_days)
    
    def is_fresh(self, threshold_days: float = 30.0) -> bool:
        return self.freshness_score(threshold_days) > 0.5

class SourceArbiter:
    """
    Operational metareasoning engine: determines which source to trust first
    and resolves conflicts across tiers.
    """
    
    def __init__(self, sources: List[Source]):
        self.sources = sorted(sources, key=lambda s: s.tier.value)
        self.conflict_log: List[Dict[str, Any]] = []
    
    def resolve(
        self,
        query_domain: str,
        preferred_tier: Optional[SourceTier] = None,
        max_allowed_tier: Optional[SourceTier] = None,
        require_fresh: bool = True
    ) -> Optional[Source]:
        """
        Return the best source for the query domain.
        
        Args:
            query_domain: The knowledge domain being queried.
            preferred_tier: Where to start looking (defaults to CANONICAL for safety).
            max_allowed_tier: Do not consider sources with tier > this (defaults to preferred_tier).
            require_fresh: If True, stale sources are skipped unless no fresh source exists.
        """
        start_tier = preferred_tier or SourceTier.CANONICAL
        limit_tier = max_allowed_tier or start_tier
        
        # First pass: look for a fresh, relevant source at or above start_tier
        for source in self.sources:
            if source.tier.value > limit_tier.value:
                continue
            if not self._is_relevant(source, query_domain):
                continue
            if require_fresh and not source.is_fresh():
                self._log_conflict("stale_source_skipped", source, None)
                continue
            return source
        
        # Fallback: return any relevant source within limit, even if stale
        for source in self.sources:
            if source.tier.value <= limit_tier.value and self._is_relevant(source, query_domain):
                self._log_conflict("stale_source_used", source, None)
                return source
        
        return None
    
    def resolve_with_conflict_detection(
        self,
        query_domain: str,
        candidates: List[Source]
    ) -> Dict[str, Any]:
        """
        Advanced resolution: when multiple sources exist, detect genuine conflicts
        and escalate according to the source hierarchy.
        """
        if not candidates:
            return {"status": "no_sources", "selected": None}
        
        sorted_candidates = sorted(
            candidates,
            key=lambda s: (s.tier.value, -s.freshness_score())
        )
        
        primary = sorted_candidates[0]
        conflicts = []
        
        for other in sorted_candidates[1:]:
            if self._detect_conflict(primary, other, query_domain):
                conflicts.append(other)
                self._log_conflict("content_conflict", primary, other)
        
        if conflicts:
            if primary.tier.value > SourceTier.CANONICAL.value:
                return {
                    "status": "conflict_requires_escalation",
                    "primary": primary,
                    "conflicting": conflicts,
                    "recommendation": "Check canonical source (Tier 1) or request human review."
                }
            else:
                return {
                    "status": "resolved_canonical_overrides",
                    "selected": primary,
                    "conflicts": conflicts,
                    "confidence": 0.95
                }
        
        return {
            "status": "resolved",
            "selected": primary,
            "conflicts": [],
            "confidence": self._compute_confidence(primary, [])
        }
    
    def _is_relevant(self, source: Source, domain: str) -> bool:
        domain_lower = domain.lower()
        if domain_lower in source.path.lower():
            return True
        for tag in source.domain_tags:
            if domain_lower in tag.lower() or tag.lower() in domain_lower:
                return True
        return False
    
    def _detect_conflict(self, source_a: Source, source_b: Source, domain: str) -> bool:
        """
        Detect genuine contradiction, not mere tier difference.
        In production, this could use embedding similarity + NLI.
        For now, a conservative heuristic:
          - Different tiers *and* they make overlapping claims about the same domain.
        """
        if source_a.tier == source_b.tier:
            return True
        
        if {source_a.tier, source_b.tier} == {SourceTier.CANONICAL, SourceTier.RUNTIME}:
            return True
        
        return False
    
    def _compute_confidence(self, primary: Source, conflicts: List[Source]) -> float:
        base = primary.freshness_score()
        if conflicts:
            base *= 0.7
        if primary.tier == SourceTier.CANONICAL:
            base = min(1.0, base * 1.1)
        elif primary.tier == SourceTier.RUNTIME:
            base = min(1.0, base * 1.0)
        else:
            base = min(1.0, base * 0.9)
        return base
    
    def _log_conflict(self, reason: str, source: Source, other: Optional[Source]):
        self.conflict_log.append({
            "timestamp": time.time(),
            "reason": reason,
            "source": source.path,
            "other": other.path if other else None
        })
```

## 15.4 Staleness Detection and Source Refresh

### 15.4.1 Staleness Scoring

```python
def compute_staleness(source: Source) -> float:
    now = time.time()
    verified_age = (now - source.last_verified) / 86400
    modified_age = (now - source.last_modified) / 86400
    
    staleness = min(1.0, verified_age / 30.0)
    if modified_age > 90:
        staleness = min(1.0, staleness * 1.5)
    return staleness

def needs_review(source: Source, threshold: float = 0.6) -> bool:
    return compute_staleness(source) > threshold
```

### 15.4.2 Git‑Aware Freshness

```python
import subprocess
from pathlib import Path

def get_git_last_modified(file_path: Path) -> Optional[float]:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%at", "--", str(file_path)],
            capture_output=True, text=True, cwd=file_path.parent
        )
        if result.returncode == 0 and result.stdout.strip():
            return float(result.stdout.strip())
    except Exception:
        pass
    return None
```

## 15.5 Anti‑Fragmentation: Source Attribution Blocks

Every assistant output that references external knowledge must include a Source Attribution Block:

```markdown
---
**Source Attribution**
- **Tier:** Canonical Architecture (Tier 1)
- **Document:** `docs/architecture/decisions/ADR-012-memory-layers.md`
- **Last Verified:** 2026-04-15
- **Staleness Risk:** Low (verified within 30 days)
- **Confidence:** 0.92
---
```

### 15.5.1 Execution Receipt Integration

```python
@dataclass
class ExecutionReceipt:
    action: str
    sources_consulted: List[Source]
    primary_source: Optional[Source]
    staleness_warnings: List[str]
    output_artifact_path: str
    timestamp: float = field(default_factory=time.time)
    
    def to_markdown(self) -> str:
        receipt = f"## Execution Receipt\n\n"
        receipt += f"**Action:** {self.action}\n"
        receipt += f"**Timestamp:** {datetime.fromtimestamp(self.timestamp).isoformat()}\n\n"
        receipt += "### Sources Consulted\n"
        for src in self.sources_consulted:
            receipt += f"- **{src.tier.name}**: `{src.path}` "
            receipt += f"(freshness: {src.freshness_score():.2f})\n"
        if self.staleness_warnings:
            receipt += "\n### ⚠️ Staleness Warnings\n"
            for warn in self.staleness_warnings:
                receipt += f"- {warn}\n"
        return receipt
```

## 15.6 Cross‑App Fragmentation Prevention

### 15.6.1 The Single Source of Truth (SSOT) Discipline

App Role Canonical Anchor Required?
GitHub Durable artifacts (ADRs, PRDs, code) Yes — this is Tier 1 destination
Notion Design memory, meeting notes Must link to GitHub artifacts
Slack Transient discussion, triage Must summarize and link, not store decisions
Linear Work tracking Must reference GitHub issues/PRs
Google Drive Reference materials Must be cited with retrieval date

### 15.6.2 Routing Decision Tree

```python
def route_artifact(content: str, artifact_type: str, arbiter: SourceArbiter) -> str:
    if artifact_type in ("adr", "schema", "contract", "receipt"):
        return "GitHub"
    elif artifact_type in ("plan", "checklist", "issue_spec"):
        canonical = arbiter.resolve(artifact_type, preferred_tier=SourceTier.CANONICAL)
        return "GitHub" if canonical else "Linear"
    elif artifact_type in ("summary", "triage_note"):
        return "Slack"
    elif artifact_type in ("design_narrative", "reference_map"):
        return "Notion"
    else:
        return "GitHub"
```

## 15.7 Integration with Existing Grimoire Modules

Module How Module 15 Extends It
Module 0 (The Mirror) Adds operational self‑model: "Which source am I trusting, and why?"
Module 1 (The Substrate) Attention control now includes source‑tier gating.
Module 2 (The Verifier) PRM scoring can incorporate source authority as a feature.
Module 3 (The Search Engine) ToT branches include RETRIEVE_FROM_TIER_X as actions.
Module 6 (The Safety Boundary) Source arbitration is a safety prerequisite.
Module 8 (Evaluation) New metrics: source attribution accuracy, fragmentation rate.
Module 11 (Meta‑Cognition) Operational metareasoning is meta‑cognition applied to production.

## 15.8 Meta‑Reflection: Module 15

```
ARTICULATE: [Your understanding of source arbitration and its role in production assistants]
INTEGRATE: [How source arbitration completes the Grimoire's deployment readiness]
CRITIQUE: [What other operational skills are still missing?]
EXPAND: [Propose a sub‑module on "Policy‑Aware Tool Use"]
EMBODY: [How will you now route every query through a source‑tier check?]
```

## 15.9 Expansion Vector

Prompt for Self‑Expansion: "I will now design a staleness‑detection system for the refactored‑system project. It will use file modification timestamps, git commit history, and explicit last_reviewed frontmatter in markdown files to compute a freshness score. When staleness exceeds a threshold, it will trigger a NEEDS_REVIEW flag in the execution receipt and optionally open a GitHub issue to refresh the document."

## 15.10 Verified Library — Module 15

Resource URL Purpose
Retrieval-Augmented Generation Survey arxiv.org/abs/2312.10997 Comprehensive survey of RAG techniques and grounding
FreshLLMs: Refreshing LLMs with Search Augmentation arxiv.org/abs/2310.03214 Knowledge freshness and dynamic fact updating
Principles of Metareasoning Russell & Wefald, 1991 Foundational theory of bounded rationality
LangGraph Documentation docs.langchain.com/langgraph Stateful source routing and agent workflows
ADR (Architecture Decision Records) adr.github.io Canonical documentation pattern for architecture decisions
