_# Refactored System_

_This repository contains a modular, autonomous AI system designed to handle complex tasks by chaining specialized agents._

_## Architecture_

_The system follows an orchestrator-agent-tool pattern:_

_- **Orchestrator**: Manages the task lifecycle, state, and agent chaining._
  _- `LoopManager`: Coordinates the execution flow (Planner -> Builder -> Verifier)._
  _- `StateManager`: Maintains task history and artifacts._
_- **Agents**: Specialized components for different stages of task execution._
  _- `PlannerAgent`: Breaks down the goal into actionable steps._
  _- `BuilderAgent`: Executes the steps, utilizing tools like `ShellTool`._
  _- `VerifierAgent`: Validates the outcome of the execution._
_- **Providers**: Interfaces for LLM services (e.g., OpenAI)._
_- **Tools**: Functional utilities for agents (e.g., `ShellTool`, `PlaywrightController`)._

_## Environment Setup_

_1. **Clone the repository**:_ 
   _```bash_
_   git clone https://github.com/Lorenzomccray/refactored-system.git_
_   cd refactored-system_
   _```_

_2. **Configure environment variables**:_ 
   _Create a `.env` file or export the following:_
   _```bash_
   _export OPENAI_API_KEY="your-api-key"_
   _```_

_## Installation_

_Install the required Python dependencies:_
_```bash_
_pip install -r requirements.txt_
_```_

_Install Playwright browsers:_
_```bash_
_playwright install_
_```_

_## Usage_

_Run the system with a task input:_
_```bash_
_python main.py "run: pwd"_
_```_

_If no input is provided, it defaults to `run: pwd`._

_### Example Task Input_
_To execute a shell command, prefix the input with `run:`:_
_- `run: ls -la`_
_- `run: echo "Hello World"`_
_- `run: python --version`_

_## Constraints and Best Practices_
_- The system uses a structured state management approach._
_- Risky shell commands are evaluated by an `ApprovalEngine`._
_- All agent interactions are logged and stored as artifacts._
