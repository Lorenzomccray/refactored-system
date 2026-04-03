import uuid
import sys
from app.orchestrator.loop_manager import LoopManager

def run(task: str) -> None:
    loop_manager = LoopManager()
    task_id = str(uuid.uuid4())
    
    print(f"Starting task: {task_id}")
    print(f"Goal: {task}")
    
    state = loop_manager.run(task_id, task)
    
    print("\n" + "="*20)
    print(f"Task ID: {state.task_id}")
    print(f"Status: {state.status}")
    print("="*20)
    
    print("\nLogs:")
    for log in state.logs:
        print(f"- {log}")
        
    print("\nArtifacts:")
    for stage, artifact in state.artifacts.items():
        print(f"{stage.upper()}: {artifact}")

if __name__ == "__main__":
    task_input = "run: pwd" if len(sys.argv) < 2 else sys.argv[1]
    run(task_input)
