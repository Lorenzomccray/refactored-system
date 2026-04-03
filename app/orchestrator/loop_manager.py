from app.orchestrator.router import Router
from app.orchestrator.dispatcher import Dispatcher
from app.orchestrator.state_manager import StateManager


class LoopManager:
    def __init__(self):
        self.router = Router()
        self.dispatcher = Dispatcher()
        self.state = StateManager()

    def run(self, task_id: str, goal: str):
        state = self.state.create(task_id, goal)
        state.status = "running"

        # simple loop
        for step in range(3):
            role = self.router.route(goal)
            result = self.dispatcher.dispatch(role, goal)

            self.state.log(task_id, f"Step {step}: {role} -> {result}")

        state.status = "completed"
        return state
