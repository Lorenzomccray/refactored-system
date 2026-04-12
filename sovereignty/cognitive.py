"""
Cognitive tools: decision journaling, lesson tracking, cost ledger,
session state, and worker dispatch.
"""

from sovereignty.db import get_db


def log_decision(
    session_id: str,
    task_context: str,
    action: str,
    reason: str,
    cost_estimate: float = None,
) -> dict:
    """Log a decision to the decision_journal table."""
    try:
        db = get_db()
        row = {
            "session_id": session_id,
            "task_context": task_context,
            "action": action,
            "reason": reason,
        }
        if cost_estimate is not None:
            row["cost_estimate"] = cost_estimate
        result = db.table("decision_journal").insert(row).execute()
        inserted = result.data[0] if result.data else {}
        return {"id": inserted.get("id"), "logged": True}
    except Exception as e:
        return {"error": str(e), "logged": False}


def get_decisions(session_id: str = None, limit: int = 20) -> dict:
    """Query decision_journal ordered by timestamp desc."""
    try:
        db = get_db()
        query = db.table("decision_journal").select("*").order("timestamp", desc=True).limit(limit)
        if session_id:
            query = query.eq("session_id", session_id)
        result = query.execute()
        return {"decisions": result.data or []}
    except Exception as e:
        return {"error": str(e), "decisions": []}


def log_lesson(
    category: str,
    context: str,
    action_tried: str,
    outcome: str,
    lesson: str,
    confidence: float = 0.9,
) -> dict:
    """Log a lesson learned to the lessons table."""
    try:
        db = get_db()
        row = {
            "category": category,
            "context": context,
            "action_tried": action_tried,
            "outcome": outcome,
            "lesson": lesson,
            "confidence": confidence,
        }
        result = db.table("lessons").insert(row).execute()
        inserted = result.data[0] if result.data else {}
        return {"id": inserted.get("id"), "logged": True}
    except Exception as e:
        return {"error": str(e), "logged": False}


def check_lessons(category: str = None, action_tried: str = None) -> dict:
    """
    PRE-FLIGHT check: query lessons where category matches OR action_tried
    ilike the search term. Call before any significant action.
    """
    try:
        db = get_db()
        query = db.table("lessons").select("*")

        if category and action_tried:
            query = query.or_(
                f"category.eq.{category},action_tried.ilike.%{action_tried}%"
            )
        elif category:
            query = query.eq("category", category)
        elif action_tried:
            query = query.ilike("action_tried", f"%{action_tried}%")

        result = query.order("confidence", desc=True).limit(10).execute()
        return {"lessons": result.data or []}
    except Exception as e:
        return {"error": str(e), "lessons": []}


def track_cost(
    session_id: str,
    operation_type: str,
    operation_detail: str,
    estimated_credits: float,
    task_context: str,
    was_duplicate: bool = False,
) -> dict:
    """Track an operation's cost in the cost_ledger table."""
    try:
        db = get_db()
        row = {
            "session_id": session_id,
            "operation_type": operation_type,
            "operation_detail": operation_detail,
            "estimated_credits": estimated_credits,
            "task_context": task_context,
            "was_duplicate": was_duplicate,
        }
        result = db.table("cost_ledger").insert(row).execute()
        inserted = result.data[0] if result.data else {}
        return {"id": inserted.get("id"), "tracked": True}
    except Exception as e:
        return {"error": str(e), "tracked": False}


def get_session_cost(session_id: str) -> dict:
    """Sum estimated_credits from cost_ledger for a given session."""
    try:
        db = get_db()
        result = db.table("cost_ledger").select("*").eq("session_id", session_id).execute()
        rows = result.data or []
        total = sum(r.get("estimated_credits", 0) for r in rows)
        return {
            "session_id": session_id,
            "total_credits": total,
            "operations": rows,
        }
    except Exception as e:
        return {"error": str(e), "session_id": session_id, "total_credits": 0, "operations": []}


def save_session(
    active_task: str,
    task_stack: list,
    system_snapshot: dict,
    pending_actions: list,
    open_questions: list,
    key_discoveries: list,
    next_session_priority: str,
) -> dict:
    """Save current session state to session_state table."""
    try:
        db = get_db()
        row = {
            "active_task": active_task,
            "task_stack": task_stack,
            "system_snapshot": system_snapshot,
            "pending_actions": pending_actions,
            "open_questions": open_questions,
            "key_discoveries": key_discoveries,
            "next_session_priority": next_session_priority,
        }
        result = db.table("session_state").insert(row).execute()
        inserted = result.data[0] if result.data else {}
        return {"id": inserted.get("id"), "saved": True}
    except Exception as e:
        return {"error": str(e), "saved": False}


def load_last_session() -> dict:
    """Load the most recent session state from session_state table."""
    try:
        db = get_db()
        result = (
            db.table("session_state")
            .select("*")
            .order("ended_at", desc=True)
            .limit(1)
            .execute()
        )
        rows = result.data or []
        if rows:
            return {"session": rows[0]}
        return {"session": None, "note": "No previous session found"}
    except Exception as e:
        return {"error": str(e), "session": None}


def log_worker(
    worker: str,
    task: str,
    expected_completion: str,
    next_action: str,
) -> dict:
    """Dispatch a worker by inserting into worker_dispatch with status='working'."""
    try:
        db = get_db()
        row = {
            "worker": worker,
            "task": task,
            "expected_completion": expected_completion,
            "next_action": next_action,
            "status": "working",
        }
        result = db.table("worker_dispatch").insert(row).execute()
        inserted = result.data[0] if result.data else {}
        return {"id": inserted.get("id"), "dispatched": True}
    except Exception as e:
        return {"error": str(e), "dispatched": False}


def update_worker(worker_id: str, status: str, result_location: str = None) -> dict:
    """Update a worker_dispatch row by ID."""
    try:
        db = get_db()
        update = {"status": status}
        if result_location is not None:
            update["result_location"] = result_location
        db.table("worker_dispatch").update(update).eq("id", worker_id).execute()
        return {"updated": True}
    except Exception as e:
        return {"error": str(e), "updated": False}


def get_active_workers() -> dict:
    """Query worker_dispatch for all workers with status='working'."""
    try:
        db = get_db()
        result = db.table("worker_dispatch").select("*").eq("status", "working").execute()
        return {"workers": result.data or []}
    except Exception as e:
        return {"error": str(e), "workers": []}
