from app.orchestrator.context_loader import ContextLoader
from app.orchestrator.dispatcher import Dispatcher
from app.orchestrator.source_router import SourceRouter
from app.orchestrator.state_manager import StateManager
from app.orchestrator.task_classifier import TaskClassifier


class LoopManager:
    def __init__(self):
        self.dispatcher = Dispatcher()
        self.state = StateManager()
        self.task_classifier = TaskClassifier()
        self.source_router = SourceRouter()
        self.context_loader = ContextLoader()

    def run(self, task_id: str, goal: str):
        state = self.state.create(task_id, goal)
        state.status = "running"

        task = self.task_classifier.classify(task_id, goal)
        resolution = self.source_router.resolve(task)
        context = self.context_loader.load(task, resolution)

        state.artifacts["task"] = task.to_dict()
        state.artifacts["source_resolution"] = resolution.to_dict()
        state.artifacts["context"] = context
        self.state.log(task_id, f"Task classified as: {task.task_kind.value}")
        self.state.log(task_id, f"Preferred source tier: {resolution.preferred_tier.value}")

        if resolution.fail_closed:
            self.state.log(task_id, "High-impact source conflict detected; failing closed.")
            state.status = "failed"
            return state

        stages = ["planner", "builder", "verifier"]
        last_result = goal

        for stage in stages:
            self.state.log(task_id, f"Starting stage: {stage}")
            try:
                result = self.dispatcher.dispatch(stage, last_result)
                state.artifacts[stage] = result
                self.state.log(task_id, f"Completed stage: {stage} with result: {result}")
                last_result = result
            except Exception as exc:
                self.state.log(task_id, f"Error in stage {stage}: {str(exc)}")
                state.status = "failed"
                return state

        state.status = "completed"
        self.state.log(task_id, "Task completed successfully")
        return state
