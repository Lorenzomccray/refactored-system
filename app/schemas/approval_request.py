from dataclasses import dataclass


@dataclass(slots=True)
class ApprovalRequest:
    request_id: str
    task_id: str
    step_id: str
    risk_class: str
    reason: str
    requested_by: str = "system"
