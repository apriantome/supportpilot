# === Stage 66: Add export of a short status dashboard ===
# Project: SupportPilot
def dashboard():
    print("=== SupportPilot Status ===")
    print(f"Requests: {len(requests)}")
    for r in requests:
        status = "Open" if r.owner is None else "Assigned"
        if r.resolution:
            status += " -> Resolved"
        print(f"  #{r.id}: [{status}] {r.title} (owner={r.owner})")
