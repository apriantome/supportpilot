# === Stage 26: Add weekly summary calculations ===
# Project: SupportPilot
def weekly_summary(board):
    week = board.get_current_week()
    if not week:
        return {}
    stats = {
        "requests_created": sum(1 for r in board.requests if r.created_date and r.created_date.week == week),
        "resolved": sum(1 for r in board.requests if r.resolution and r.created_date and r.created_date.week == week),
        "avg_resolution_hours": (
            sum((r.resolution - r.created_date).total_seconds() / 3600
                for r in board.requests if r.resolution and r.created_date and r.created_date.week == week)
            / max(sum(1 for r in board.requests if r.resolution and r.created_date and r.created_date.week == week), 1)
        ),
    }
    return stats
