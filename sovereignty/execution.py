"""
Execution safety tools: preflight check, dedup check, operation logging.
DB columns: operation_log(id, timestamp, operation_hash, operation_type, operation_args jsonb, result_summary, ttl_seconds)
"""

import hashlib

from sovereignty.db import get_db
from sovereignty.cognitive import check_lessons


def preflight_check(action_description: str, category: str = None) -> dict:
    """
    Run a preflight safety check before performing an action.
    Checks lessons and operation_log for past failures and recent duplicates.
    Returns safe=True if no blockers found, with any warnings.
    """
    warnings = []
    recommendation = "Proceed"

    try:
        # Check lessons for relevant warnings
        lessons_result = check_lessons(
            category=category, action_tried=action_description
        )
        lessons = lessons_result.get("lessons", [])
        for lesson in lessons:
            outcome = lesson.get("outcome", "")
            lesson_text = lesson.get("lesson", "")
            if outcome and ("fail" in outcome.lower() or "hang" in outcome.lower() or "block" in outcome.lower()):
                warnings.append(
                    f"[LESSON] Failed before: {lesson_text} (confidence: {lesson.get('confidence', '?')})"
                )
            elif lesson_text:
                warnings.append(f"[LESSON] {lesson_text}")

        # Check for recent duplicates in operation_log
        try:
            db = get_db()
            result = (
                db.table("operation_log")
                .select("*")
                .ilike("operation_type", f"%{action_description[:50]}%")
                .order("timestamp", desc=True)
                .limit(3)
                .execute()
            )
            dupes = result.data or []
            for dupe in dupes:
                warnings.append(
                    f"[DUPE_RISK] Similar operation ran recently: {dupe.get('operation_type')} "
                    f"at {dupe.get('timestamp')}"
                )
        except Exception:
            pass  # Don't fail preflight on operation_log errors

        if warnings:
            recommendation = (
                "Review warnings before proceeding. Potential duplicate or past failures detected."
            )

        return {
            "safe": len([w for w in warnings if "[LESSON] Failed" in w]) == 0,
            "warnings": warnings,
            "recommendation": recommendation,
        }
    except Exception as e:
        return {
            "safe": True,
            "warnings": [f"Preflight check error (non-blocking): {str(e)}"],
            "recommendation": "Proceed with caution — preflight check encountered an error.",
        }


def dedup_check(operation_type: str, operation_args_str: str, ttl_seconds: int = 60) -> dict:
    """
    Check if the same operation was run recently (within ttl_seconds).
    Returns is_duplicate=True if a recent matching operation is found.
    """
    try:
        db = get_db()
        op_hash = hashlib.md5(
            f"{operation_type}:{operation_args_str}".encode()
        ).hexdigest()

        result = (
            db.table("operation_log")
            .select("*")
            .eq("operation_hash", op_hash)
            .order("timestamp", desc=True)
            .limit(1)
            .execute()
        )
        rows = result.data or []

        if not rows:
            return {"is_duplicate": False, "last_run": None, "cached_result": None}

        row = rows[0]
        run_timestamp = row.get("timestamp")
        cached_result = row.get("result_summary")

        # Check if within TTL
        try:
            from dateutil import parser as dateparser
            from datetime import datetime, timezone

            run_time = dateparser.parse(run_timestamp)
            if run_time.tzinfo is None:
                run_time = run_time.replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)
            age_seconds = (now - run_time).total_seconds()
            is_duplicate = age_seconds < ttl_seconds
        except Exception:
            is_duplicate = True  # Treat as duplicate if we can't parse the time

        return {
            "is_duplicate": is_duplicate,
            "last_run": run_timestamp,
            "cached_result": cached_result,
        }
    except Exception as e:
        return {"error": str(e), "is_duplicate": False, "last_run": None, "cached_result": None}


def log_operation(
    operation_type: str,
    operation_args: str,
    result_summary: str,
    ttl_seconds: int = 60,
) -> dict:
    """
    Log a completed operation to operation_log for dedup tracking.
    Computes MD5 hash of operation_type + operation_args as the dedup key.
    """
    try:
        db = get_db()
        op_hash = hashlib.md5(
            f"{operation_type}:{operation_args}".encode()
        ).hexdigest()

        row = {
            "operation_type": operation_type,
            "operation_args": {"args": operation_args},  # jsonb column — wrap in dict
            "operation_hash": op_hash,
            "result_summary": result_summary,
            "ttl_seconds": ttl_seconds,
        }
        db.table("operation_log").insert(row).execute()
        return {"logged": True}
    except Exception as e:
        return {"error": str(e), "logged": False}
