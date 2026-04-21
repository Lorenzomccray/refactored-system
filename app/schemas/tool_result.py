from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass(slots=True)
class ToolResult:
    call_id: str
    tool_name: str
    ok: bool
    output: Any = None
    error: Optional[str] = None
    artifacts: List[str] = field(default_factory=list)
