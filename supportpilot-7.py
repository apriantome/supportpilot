# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: SupportPilot
def format_request(req):
    status = req.get("status", "unknown")
    owner = req.get("owner", "unassigned")
    followups = len(req.get("follow_ups", []))
    resolution = req.get("resolution", "")
    return (f"  [{req['id']}]\n"
            f"    Status: {status}\n"
            f"    Owner: {owner}\n"
            f"    Follow-ups: {followups}\n"
            f"    Resolution: {'Yes' if resolution else 'No'}\n")

def format_metrics(metrics):
    total = metrics.get("total_requests", 0)
    resolved = metrics.get("resolved_count", 0)
    avg_time = metrics.get("avg_resolution_time_hours", 0)
    return (f"Total Requests: {total}\n"
            f"Resolved: {resolved} ({round(resolved/total*100,1)}%)\n"
            f"Avg Resolution Time: {avg_time:.2f} hours")
