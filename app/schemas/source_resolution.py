from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
import time
from typing import Any, Dict, List


class SourceTier(str, Enum):
    CANONICAL = "canonical"
    RUNTIME = "runtime"
    BUILD = "build"
    REFERENCE = "reference"
    EXTERNAL = "external"


class ConflictState(str, Enum):
    NONE = "none"
    CANONICAL_RUNTIME_MISMATCH = "canonical_runtime_mismatch"
    SOURCE_GAP = "source_gap"
    NEEDS_REVIEW = "needs_review"


@dataclass(frozen=True)
class SourceReference:
    tier: SourceTier
    path: str
    rationale: str
    authoritative: bool = False
    available: bool = True

    def to_dict(self) -> Dict[str, Any]:
        payload = asdict(self)
        payload["tier"] = self.tier.value
        return payload


@dataclass
class SourceResolution:
    task_id: str
    preferred_tier: SourceTier
    consulted_tiers: List[SourceTier] = field(default_factory=list)
    selected_sources: List[SourceReference] = field(default_factory=list)
    conflict_state: ConflictState = ConflictState.NONE
    escalation_required: bool = False
    fail_closed: bool = False
    confidence: float = 1.0
    rationale: List[str] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "preferred_tier": self.preferred_tier.value,
            "consulted_tiers": [tier.value for tier in self.consulted_tiers],
            "selected_sources": [source.to_dict() for source in self.selected_sources],
            "conflict_state": self.conflict_state.value,
            "escalation_required": self.escalation_required,
            "fail_closed": self.fail_closed,
            "confidence": self.confidence,
            "rationale": list(self.rationale),
            "created_at": self.created_at,
        }

    def receipt_inputs(self) -> Dict[str, Any]:
        return {
            "preferred_tier": self.preferred_tier.value,
            "consulted_tiers": [tier.value for tier in self.consulted_tiers],
            "selected_paths": [source.path for source in self.selected_sources],
            "conflict_state": self.conflict_state.value,
            "escalation_required": self.escalation_required,
            "confidence": self.confidence,
        }
