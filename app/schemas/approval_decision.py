from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class ApprovalDecision:
    request_id: str
    approved: bool
    policy_rule: str
    reason: str
    reviewer: str = "policy"
    requires_human: bool = False
    escalation_target: Optional[str] = None
