from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(slots=True)
class ToolCall:
    call_id: str
    task_id: str
    step_id: str
    tool_name: str
    arguments: Dict[str, Any] = field(default_factory=dict)
