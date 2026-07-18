# === Stage 25: Add daily summary calculations ===
# Project: SupportPilot
def daily_summary(board):
    """Compute a single-day summary for each request owner."""
    summaries = {}
    today = date.today()
    for req in board.requests:
        if req.created_on == today and req.resolved is None:
            key = (req.owner, req.status)
            s = summaries.get(key, {"open": 0, "resolved": 0})
            if req.status == "open":
                s["open"] += 1
            elif req.status == "resolved":
                s["resolved"] += 1
    for key, val in summaries.items():
        print(f"{key[0]}: {val}")
