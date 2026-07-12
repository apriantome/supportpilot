# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: SupportPilot
def search_requests(q: str, board=None):
    """Case-insensitive substring search across title, description, owner, and tags."""
    if board is None:
        return []
    q = q.strip().lower()
    matches = [r for r in board.requests if any(
        q in (getattr(r, k, '') or '').lower() for k in ('title', 'description', 'owner', 'tags')
    )]
    return matches
