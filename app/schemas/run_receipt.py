from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class RunReceipt:
    run_id: str
    task_id: str
    plan_id: str
    step_id: str
    status: str
    tool_receipt_ids: List[str] = field(default_factory=list)
    verification_ids: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)
