# === Stage 37: Add recommendations for the next useful action ===
# Project: SupportPilot
def resolve_request(board: dict, request_id: str) -> None:
    """Mark a support request as resolved and notify the assigned owner."""
    requests = board.get("requests", {})
    if request_id in requests:
        req = requests[request_id]
        req["status"] = "resolved"
        req["resolution"] = _generate_resolution(req)
        if "owner" in req:
            owners = board.get("owners", {})
            if req["owner"] in owners:
                owners[req["owner"]]["metrics"]["resolved_count"] += 1

def _generate_resolution(request: dict) -> str:
    """Produce a human-readable resolution string from the request data."""
    parts = []
    if "title" in request:
        parts.append(f'Title: {request["title"]}')
    if "priority" in request:
        parts.append(f'Priority handled as {request["priority"]}')
    if "category" in request:
        parts.append(f'Category: {request["category"]}')
    if "resolution_time" in request and request["resolution_time"] is not None:
        hours = int(request["resolution_time"]) // 3600
        minutes = (int(request["resolution_time"]) % 3600) // 60
        parts.append(f'Resolved in {hours}h{minutes}m')
    return "; ".join(parts) if parts else "Resolved"
