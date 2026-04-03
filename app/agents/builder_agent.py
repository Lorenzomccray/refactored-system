from app.tools.shell_tool import ShellTool
from typing import Any, Dict

class BuilderAgent:
    def __init__(self):
        self.shell = ShellTool()

    def run(self, task: Any) -> Dict[str, Any]:
        # Handle input from planner which might be a dict or a string
        task_str = ""
        if isinstance(task, dict):
            # Look for a key that might contain the plan or next step
            if 'steps' in task and task['steps']:
                task_str = task['steps'][0] # Assuming we take the first step
            elif 'plan' in task:
                task_str = task['plan']
            else:
                task_str = str(task)
        else:
            task_str = str(task)

        if task_str.startswith("run:"):
            command = task_str[4:].strip()
            result = self.shell.run(command)
            return {
                "type": "shell_execution",
                "command": command,
                "result": result
            }
        
        return {
            "type": "text_response",
            "result": f"Building: {task_str}"
        }
