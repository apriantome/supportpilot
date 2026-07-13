# === Stage 13: Add file save support using a configurable path ===
# Project: SupportPilot
def save_request(request, config=None):
    """Save a request to disk using a configurable path."""
    if config is None:
        config = {}
    filepath = config.get("save_path", "requests.json")
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    request_dict = {
        "id": request["id"],
        "subject": request["subject"],
        "description": request["description"],
        "status": request["status"],
        "owner": request.get("owner"),
        "priority": request.get("priority"),
        "category": request.get("category"),
        "created_at": request["created_at"]
    }
    data.append(request_dict)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
