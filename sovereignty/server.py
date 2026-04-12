"""
Tasklet Sovereignty MCP Server — FastMCP stdio server exposing sovereign tools.
"""

from mcp.server.fastmcp import FastMCP

from sovereignty.cognitive import (
    log_decision,
    get_decisions,
    log_lesson,
    check_lessons,
    track_cost,
    get_session_cost,
    save_session,
    load_last_session,
    log_worker,
    update_worker,
    get_active_workers,
)
from sovereignty.execution import preflight_check, dedup_check, log_operation
from sovereignty.omniscient import (
    get_system_pulse,
    get_repo_status,
    get_goals,
    update_goal,
    add_goal,
)

mcp = FastMCP("tasklet-sovereignty")


# ─── Cognitive Tools ──────────────────────────────────────────────────────────


@mcp.tool()
def tool_log_decision(
    session_id: str,
    task_context: str,
    action: str,
    reason: str,
    cost_estimate: float = None,
) -> dict:
    """
    Log a decision to the decision_journal table for auditability and
    future review. Call this after any significant agentic decision.
    """
    return log_decision(session_id, task_context, action, reason, cost_estimate)


@mcp.tool()
def tool_get_decisions(session_id: str = None, limit: int = 20) -> dict:
    """
    Retrieve past decisions from decision_journal, ordered by timestamp desc.
    Optionally filter by session_id.
    """
    return get_decisions(session_id, limit)


@mcp.tool()
def tool_log_lesson(
    category: str,
    context: str,
    action_tried: str,
    outcome: str,
    lesson: str,
    confidence: float = 0.9,
) -> dict:
    """
    Log a lesson learned (from success or failure) to the lessons table.
    Future actions can use check_lessons to benefit from this knowledge.
    """
    return log_lesson(category, context, action_tried, outcome, lesson, confidence)


@mcp.tool()
def tool_check_lessons(category: str = None, action_tried: str = None) -> dict:
    """
    PRE-FLIGHT check: retrieve relevant lessons before performing an action.
    Searches by category match OR action_tried similarity. Call this before
    any significant action to avoid repeating past mistakes.
    """
    return check_lessons(category, action_tried)


@mcp.tool()
def tool_track_cost(
    session_id: str,
    operation_type: str,
    operation_detail: str,
    estimated_credits: float,
    task_context: str,
    was_duplicate: bool = False,
) -> dict:
    """
    Track the estimated cost of an operation in the cost_ledger table.
    Use this to monitor credit consumption per session.
    """
    return track_cost(
        session_id,
        operation_type,
        operation_detail,
        estimated_credits,
        task_context,
        was_duplicate,
    )


@mcp.tool()
def tool_get_session_cost(session_id: str) -> dict:
    """
    Get the total estimated credit cost for a session, plus all individual
    operations logged under that session_id.
    """
    return get_session_cost(session_id)


@mcp.tool()
def tool_save_session(
    active_task: str,
    task_stack: list,
    system_snapshot: dict,
    pending_actions: list,
    open_questions: list,
    key_discoveries: list,
    next_session_priority: str,
) -> dict:
    """
    Save the current session state snapshot to session_state table so the
    next session can resume with full context.
    """
    return save_session(
        active_task,
        task_stack,
        system_snapshot,
        pending_actions,
        open_questions,
        key_discoveries,
        next_session_priority,
    )


@mcp.tool()
def tool_load_last_session() -> dict:
    """
    Load the most recent session state from session_state table to resume
    work from where the previous session left off.
    """
    return load_last_session()


@mcp.tool()
def tool_log_worker(
    worker: str,
    task: str,
    expected_completion: str,
    next_action: str,
) -> dict:
    """
    Dispatch a worker by recording it in worker_dispatch with status='working'.
    Use this to track subagents or background tasks.
    """
    return log_worker(worker, task, expected_completion, next_action)


@mcp.tool()
def tool_update_worker(
    worker_id: str, status: str, result_location: str = None
) -> dict:
    """
    Update a worker's status in worker_dispatch. Set status to 'done',
    'failed', etc. Optionally record where the result was stored.
    """
    return update_worker(worker_id, status, result_location)


@mcp.tool()
def tool_get_active_workers() -> dict:
    """
    Retrieve all workers currently in 'working' status from worker_dispatch.
    Use to monitor background task progress.
    """
    return get_active_workers()


# ─── Execution Safety Tools ───────────────────────────────────────────────────


@mcp.tool()
def tool_preflight_check(action_description: str, category: str = None) -> dict:
    """
    Run a preflight safety check before performing an action. Checks the
    lessons table and operation_log for past failures and recent duplicates.
    Returns safe=True/False with a list of warnings and a recommendation.
    """
    return preflight_check(action_description, category)


@mcp.tool()
def tool_dedup_check(
    operation_type: str, operation_args_str: str, ttl_seconds: int = 60
) -> dict:
    """
    Check whether the same operation (by type + args MD5 hash) was run
    within the last ttl_seconds. Returns is_duplicate=True with cached
    result if found, so the caller can skip re-execution.
    """
    return dedup_check(operation_type, operation_args_str, ttl_seconds)


@mcp.tool()
def tool_log_operation(
    operation_type: str,
    operation_args: str,
    result_summary: str,
    ttl_seconds: int = 60,
) -> dict:
    """
    Log a completed operation to operation_log for future dedup checks.
    Computes an MD5 hash of operation_type + operation_args as the dedup key.
    """
    return log_operation(operation_type, operation_args, result_summary, ttl_seconds)


# ─── Omniscient Tools ─────────────────────────────────────────────────────────


@mcp.tool()
def tool_get_system_pulse() -> dict:
    """
    Queue a full system health check via fedora_tasks. The pulse script
    reports service status, Docker containers, resource usage, and git state.
    Returns a task_id — poll fedora_tasks to retrieve the result.
    """
    return get_system_pulse()


@mcp.tool()
def tool_get_repo_status(
    owner: str = "lorenzomccray", repo: str = "Quantum-Commander"
) -> dict:
    """
    Queue a git repository status check via fedora_tasks. Reports current
    branch, commits behind origin/main, dirty files, and last commit.
    Returns a task_id — poll fedora_tasks to retrieve the result.
    """
    return get_repo_status(owner, repo)


@mcp.tool()
def tool_get_goals(status: str = None) -> dict:
    """
    Retrieve goals from goal_tracker, ordered by priority ascending.
    Optionally filter by status (e.g., 'active', 'completed', 'blocked').
    """
    return get_goals(status)


@mcp.tool()
def tool_update_goal(
    goal_id: str,
    status: str = None,
    notes: str = None,
    blockers: str = None,
) -> dict:
    """
    Update a goal in goal_tracker. Can update status, notes, and/or blockers.
    Automatically sets updated_at to the current timestamp.
    """
    return update_goal(goal_id, status, notes, blockers)


@mcp.tool()
def tool_add_goal(
    goal: str,
    priority: int = 3,
    parent_goal_id: str = None,
    notes: str = None,
) -> dict:
    """
    Add a new goal to goal_tracker. Priority 1=highest, 5=lowest.
    Optionally link to a parent goal for hierarchical planning.
    """
    return add_goal(goal, priority, parent_goal_id, notes)


def run():
    """Entry point — run the MCP server over stdio."""
    mcp.run(transport="stdio")
