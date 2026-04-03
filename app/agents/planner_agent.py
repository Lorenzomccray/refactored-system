from typing import Dict, List, Any

class PlannerAgent:
    def run(self, task: str) -> Dict[str, Any]:
        # Return a structured planning object as required
        return {
            "plan": f"Execute the requested task: {task}",
            "steps": [task],
            "task_type": "shell" if task.startswith("run:") else "general"
        }
