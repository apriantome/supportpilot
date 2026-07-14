# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: SupportPilot
def dispatch(text):
    text = text.strip().lower()
    if "help" in text:
        print("Available commands: help, new, list, show <id>, resolve <id>")
    elif text.startswith("new"):
        parts = text.split(maxsplit=2)
        owner = parts[1] if len(parts) > 1 else ""
        subject = parts[2] if len(parts) > 2 else "New Request"
        return {"type": "create", "owner": owner, "subject": subject}
    elif text.startswith("list"):
        return {"type": "list"}
    elif text.startswith("show"):
        try:
            rid = int(text.split(None,1)[1])
            return {"type": "show", "id": rid}
        except ValueError:
            return {"type": "error", "message": "Invalid request id"}
    elif text.startswith("resolve"):
        try:
            rid = int(text.split(None,1)[1])
            return {"type": "resolve", "id": rid}
        except ValueError:
            return {"type": "error", "message": "Invalid request id"}
    else:
        return {"type": "unknown"}
