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
        
        # Chained agents: planner -> builder -> verifier
        stages = ["planner", "builder", "verifier"]
        
        last_result = goal
        for stage in stages:
            self.state.log(task_id, f"Starting stage: {stage}")
            try:
                result = self.dispatcher.dispatch(stage, last_result)
                state.artifacts[stage] = result
                self.state.log(task_id, f"Completed stage: {stage} with result: {result}")
                last_result = result
            except Exception as e:
                self.state.log(task_id, f"Error in stage {stage}: {str(e)}")
                state.status = "failed"
                return state

        state.status = "completed"
        self.state.log(task_id, "Task completed successfully")
        return state
