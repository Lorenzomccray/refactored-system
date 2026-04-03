from dataclasses import dataclass, field
from typing import Any, Dict, List
import time


@dataclass
class TaskState:
    task_id: str
    goal: str
    plan: List[str] = field(default_factory=list)
    current_step: int = 0
    artifacts: Dict[str, Any] = field(default_factory=dict)
    logs: List[str] = field(default_factory=list)
    created_at: float = field(default_factory=lambda: time.time())
    updated_at: float = field(default_factory=lambda: time.time())
    status: str = "created"


class StateManager:
    def __init__(self):
        self._states: Dict[str, TaskState] = {}

    def create(self, task_id: str, goal: str) -> TaskState:
        state = TaskState(task_id=task_id, goal=goal)
        self._states[task_id] = state
        return state

    def get(self, task_id: str) -> TaskState | None:
        return self._states.get(task_id)

    def update(self, task_id: str, **kwargs) -> TaskState | None:
        state = self._states.get(task_id)
        if not state:
            return None
        for k, v in kwargs.items():
            setattr(state, k, v)
        state.updated_at = time.time()
        return state

    def log(self, task_id: str, message: str) -> None:
        state = self._states.get(task_id)
        if state:
            state.logs.append(message)
            state.updated_at = time.time()
