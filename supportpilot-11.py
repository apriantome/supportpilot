# === Stage 11: Add JSON export for the current application state ===
# Project: SupportPilot
def export_state():
    state = {
        "requests": [
            {"id": r["request_id"], "title": r.get("title", ""), "status": r["status"]}
            for r in requests
        ],
        "owners": [
            {"name": o["owner_name"], "email": o.get("owner_email", "")}
            for o in owners
        ],
        "followups_count": len(followups),
        "resolved_count": sum(1 for f in followups if f["status"] == "resolved"),
    }
    with open("supportpilot_state.json", "w") as f:
        json.dump(state, f, indent=2)
