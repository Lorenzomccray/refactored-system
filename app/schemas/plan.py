from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(slots=True)
class PlanStep:
    step_id: str
    description: str
    risk_class: str = "READ_ONLY"
    requires_tool: bool = False
    tool_name: Optional[str] = None


@dataclass(slots=True)
class Plan:
    plan_id: str
    task_id: str
    steps: List[PlanStep] = field(default_factory=list)
    success_criteria: List[str] = field(default_factory=list)
