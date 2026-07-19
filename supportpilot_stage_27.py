# === Stage 27: Add monthly summary calculations ===
# Project: SupportPilot
def monthly_summary(month, year):
    """Compute a concise monthly summary for all resolved tickets."""
    stats = {
        "month": month,
        "year": year,
        "total_resolved": 0,
        "avg_resolution_days": None,
        "total_follow_ups": 0,
    }
    resolution_times = []
    for ticket in all_tickets:
        if ticket["status"] == "resolved" and ticket["resolution_date"]:
            stats["total_resolved"] += 1
            resolved_dt = datetime.fromisoformat(ticket["resolution_date"])
            created_dt = datetime.fromisoformat(ticket["created_at"])
            resolution_times.append((resolved_dt - created_dt).days)

    if resolution_times:
        stats["avg_resolution_days"] = sum(resolution_times) / len(resolution_times)
    for ticket in all_tickets:
        if ticket.get("follow_ups"):
            stats["total_follow_ups"] += len(ticket["follow_ups"])
    return stats
