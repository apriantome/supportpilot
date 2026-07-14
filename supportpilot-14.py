# === Stage 14: Add file load support with fallback demo data ===
# Project: SupportPilot
def load_board(path):
    """Load a SupportPilot board from disk, falling back to demo data when the file is missing."""
    try:
        with open(path) as f:
            return pickle.load(f)
    except FileNotFoundError:
        return _demo_board()

def _demo_board():
    now = datetime.now(timezone.utc)
    owners = {"alice": "Alice", "bob": "Bob", "carol": "Carol"}
    requests = [
        {
            "id": 1,
            "title": "Login fails on mobile",
            "owner": "alice",
            "follow_ups": [{"date": now - timedelta(days=2), "note": "Reproduced on device X"}],
            "status": "open",
        },
        {
            "id": 2,
            "title": "Slow checkout flow",
            "owner": "bob",
            "follow_ups": [{"date": now - timedelta(days=5), "note": "Needs perf review"}],
            "status": "open",
        },
        {
            "id": 3,
            "title": "Password reset email not sent",
            "owner": "carol",
            "follow_ups": [{"date": now - timedelta(days=1), "note": "SMTP host misconfigured"}],
            "status": "resolved",
        },
    ]
    return {"requests": requests, "owners": owners}
