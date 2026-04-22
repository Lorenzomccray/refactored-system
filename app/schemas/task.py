from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
import time
from typing import Any, Dict, List


class TaskKind(str, Enum):
    ARCHITECTURE = "architecture"
    RUNTIME = "runtime"
    BUILD = "build"
    REFERENCE = "reference"
    EXTERNAL = "external"


class RequestedActionClass(str, Enum):
    READ_ONLY = "READ_ONLY"
    LOCAL_WRITE = "LOCAL_WRITE"
    LOCAL_EXECUTION = "LOCAL_EXECUTION"
    EXTERNAL_API_CALL = "EXTERNAL_API_CALL"


@dataclass(frozen=True)
class Task:
    task_id: str
    raw_input: str
    normalized_goal: str
    task_kind: TaskKind
    requested_action_class: RequestedActionClass
    rationale: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    high_impact: bool = False
    created_at: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        payload = asdict(self)
        payload["task_kind"] = self.task_kind.value
        payload["requested_action_class"] = self.requested_action_class.value
        return payload
