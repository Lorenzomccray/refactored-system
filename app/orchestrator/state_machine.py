from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List


class RunState(str, Enum):
    INTAKE = "INTAKE"
    CONTEXT_LOAD = "CONTEXT_LOAD"
    PLAN = "PLAN"
    AUTHORIZE = "AUTHORIZE"
    EXECUTE = "EXECUTE"
    OBSERVE = "OBSERVE"
    VERIFY = "VERIFY"
    RETRY_OR_REPLAN = "RETRY_OR_REPLAN"
    PERSIST = "PERSIST"
    RESPOND = "RESPOND"
    FAIL_CLOSED = "FAIL_CLOSED"


_ALLOWED_TRANSITIONS: Dict[RunState, List[RunState]] = {
    RunState.INTAKE: [RunState.CONTEXT_LOAD],
    RunState.CONTEXT_LOAD: [RunState.PLAN],
    RunState.PLAN: [RunState.AUTHORIZE],
    RunState.AUTHORIZE: [RunState.EXECUTE, RunState.FAIL_CLOSED],
    RunState.EXECUTE: [RunState.OBSERVE, RunState.FAIL_CLOSED],
    RunState.OBSERVE: [RunState.VERIFY, RunState.FAIL_CLOSED],
    RunState.VERIFY: [RunState.PERSIST, RunState.RETRY_OR_REPLAN, RunState.FAIL_CLOSED],
    RunState.RETRY_OR_REPLAN: [RunState.PLAN, RunState.FAIL_CLOSED],
    RunState.PERSIST: [RunState.RESPOND],
    RunState.RESPOND: [],
    RunState.FAIL_CLOSED: [],
}


@dataclass(slots=True)
class ExecutionState:
    run_id: str
    task_id: str
    current: RunState = RunState.INTAKE
    history: List[RunState] = field(default_factory=lambda: [RunState.INTAKE])


class StateMachine:
    """Minimal canonical state machine scaffold for the first code milestone."""

    def __init__(self, state: ExecutionState):
        self.state = state

    def can_transition(self, next_state: RunState) -> bool:
        return next_state in _ALLOWED_TRANSITIONS[self.state.current]

    def transition(self, next_state: RunState) -> RunState:
        if not self.can_transition(next_state):
            raise ValueError(f"Invalid state transition: {self.state.current.value} -> {next_state.value}")
        self.state.current = next_state
        self.state.history.append(next_state)
        return self.state.current
