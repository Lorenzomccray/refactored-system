from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(slots=True)
class Task:
    task_id: str
    goal: str
    task_type: str = "general"
    source: str = "manual"
    metadata: Dict[str, Any] = field(default_factory=dict)
