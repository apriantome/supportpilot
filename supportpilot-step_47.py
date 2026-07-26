# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: SupportPilot
def run_demo():
    """Run a compact end-to-end demo of SupportPilot."""
    from support_pilot.board import Board
    b = Board()
    # 1. Create a request
    req = b.add_request("Login fails after password reset", "user@example.com")
    print(f"Created request #{req.id}")
    # 2. Assign owner and add follow-up
    b.assign_owners(req, ["alice"])
    b.add_follow_up(req, "Check auth service logs", "bob")
    print(f"Owner: {b.get_owner(req)}, Follow-ups: {len(b.get_follow_ups(req))}")
    # 3. Resolve
    resolution = {"status": "resolved", "note": "Password cache cleared"}
    b.resolve_request(req, resolution)
    print(f"Resolutions: {b.get_resolutions(req)}")
    # 4. Print metrics
    print("Metrics:", b.metrics())

run_demo()
