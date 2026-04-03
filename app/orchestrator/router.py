class Router:
    def route(self, task: str) -> str:
        if "code" in task:
            return "builder"
        if "research" in task:
            return "research"
        return "planner"
