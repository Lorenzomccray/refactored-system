from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(slots=True)
class VerificationResult:
    verification_id: str
    run_id: str
    task_id: str
    step_id: str
    layer: str
    passed: bool
    evidence_summary: str
    artifacts: List[str] = field(default_factory=list)
    failure_reason: Optional[str] = None
