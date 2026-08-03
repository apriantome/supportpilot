# === Stage 67: Add a function that returns key project metrics ===
# Project: SupportPilot
def get_project_metrics():
    """Return key project metrics."""
    total = len(requests)
    open_count = sum(1 for r in requests if r.status in ("open", "in_progress"))
    closed_count = sum(1 for r in requests if r.status == "closed")
    avg_followups = (sum(r.followup_count for r in requests) / total) if total else 0.0
    return {
        "total": total,
        "open": open_count,
        "closed": closed_count,
        "avg_followups_per_request": round(avg_followups, 2),
    }
