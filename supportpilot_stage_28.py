# === Stage 28: Add overdue item detection based on due dates ===
# Project: SupportPilot
def detect_overdue(items, now=None):
    if now is None:
        now = datetime.now()
    overdue = []
    for item in items:
        due = item.get("due_date") or item.get("deadline")
        if due and isinstance(due, str) and due < now.strftime("%Y-%m-%d"):
            overdue.append(item)
    return overdue
