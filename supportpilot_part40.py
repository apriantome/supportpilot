# === Stage 40: Add plain text report export ===
# Project: SupportPilot
def export_report(board, filename="support_pilot.txt"):
    """Export a compact plain-text report of all support requests."""
    lines = [f"SupportPilot Report — {datetime.now()}"]
    for req in board.requests:
        status = "Resolved" if req.status == "resolved" else "Open"
        owner = req.owner or "Unassigned"
        followup_count = len(req.followups)
        lines.append(f"\n{status} | ID:{req.id} | Owner:{owner}")
        for fu in req.followups:
            lines.append(f"  Follow-up by {fu.author}: {fu.message}")
    lines.append("\n--- Service Metrics ---")
    total = len(board.requests)
    resolved = sum(1 for r in board.requests if r.status == "resolved")
    avg_time = (board.total_response_seconds / total) if total else 0
    lines.append(f"Total: {total} | Resolved: {resolved} | Avg Response: {avg_time:.1f}s")
    return "\n".join(lines), filename
