"""
Omniscient tools: system pulse, repo status, and goal management.
"""

from sovereignty.db import get_db


def get_system_pulse() -> dict:
    """
    Queue a system pulse check by inserting a task into fedora_tasks.
    Poll the returned task_id to get the result.
    """
    try:
        db = get_db()
        cmd = "bash ~/system_pulse.sh 2>/dev/null || echo '{\"error\": \"pulse script not found\"}'"
        result = db.table("fedora_tasks").insert(
            {"status": "pending", "payload": {"command": cmd}}
        ).execute()
        inserted = result.data[0] if result.data else {}
        return {
            "task_id": inserted.get("id"),
            "status": "queued",
            "note": "Poll fedora_tasks for this id to get result",
        }
    except Exception as e:
        return {"error": str(e), "status": "error"}


def get_repo_status(owner: str = "lorenzomccray", repo: str = "Quantum-Commander") -> dict:
    """
    Queue a git repo status check via fedora_tasks. Poll task_id for result.
    """
    try:
        db = get_db()
        cmd = (
            f"cd ~/{repo} && git fetch origin && "
            "echo \"BRANCH:$(git branch --show-current) "
            "BEHIND:$(git rev-list HEAD..origin/main --count) "
            "DIRTY:$(git status --porcelain | wc -l) "
            "LAST_COMMIT:$(git log -1 --oneline)\""
        )
        result = db.table("fedora_tasks").insert(
            {"status": "pending", "payload": {"command": cmd, "owner": owner, "repo": repo}}
        ).execute()
        inserted = result.data[0] if result.data else {}
        return {
            "task_id": inserted.get("id"),
            "status": "queued",
            "note": "Poll fedora_tasks for this id to get result",
        }
    except Exception as e:
        return {"error": str(e), "status": "error"}


def get_goals(status: str = None) -> dict:
    """Query goal_tracker, optionally filtered by status, ordered by priority asc."""
    try:
        db = get_db()
        query = db.table("goal_tracker").select("*").order("priority", desc=False)
        if status:
            query = query.eq("status", status)
        result = query.execute()
        return {"goals": result.data or []}
    except Exception as e:
        return {"error": str(e), "goals": []}


def update_goal(
    goal_id: str,
    status: str = None,
    notes: str = None,
    blockers: str = None,
) -> dict:
    """Update a goal_tracker row, setting updated_at to now()."""
    try:
        db = get_db()
        update: dict = {}
        if status is not None:
            update["status"] = status
        if notes is not None:
            update["notes"] = notes
        if blockers is not None:
            update["blockers"] = blockers

        if not update:
            return {"updated": False, "note": "No fields to update provided"}

        db.table("goal_tracker").update(update).eq("id", goal_id).execute()
        return {"updated": True}
    except Exception as e:
        return {"error": str(e), "updated": False}


def add_goal(
    goal: str,
    priority: int = 3,
    parent_goal_id: str = None,
    notes: str = None,
) -> dict:
    """Insert a new goal into goal_tracker."""
    try:
        db = get_db()
        row: dict = {
            "goal": goal,
            "priority": priority,
        }
        if parent_goal_id is not None:
            row["parent_goal_id"] = parent_goal_id
        if notes is not None:
            row["notes"] = notes

        result = db.table("goal_tracker").insert(row).execute()
        inserted = result.data[0] if result.data else {}
        return {"id": inserted.get("id"), "added": True}
    except Exception as e:
        return {"error": str(e), "added": False}
