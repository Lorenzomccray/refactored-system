from app.agents.planner_agent import PlannerAgent
from app.agents.builder_agent import BuilderAgent
from app.agents.verifier_agent import VerifierAgent


class Dispatcher:
    def __init__(self):
        self.agents = {
            "planner": PlannerAgent(),
            "builder": BuilderAgent(),
            "verifier": VerifierAgent(),
        }

    def dispatch(self, role: str, task: str):
        return self.agents[role].run(task)
