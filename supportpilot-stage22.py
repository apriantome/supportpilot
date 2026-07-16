# === Stage 22: Add favorite records and quick favorite listing ===
# Project: SupportPilot
def toggle_favorite(request_id: str, users_db: dict) -> None:
    """Toggle a request's favorite status for all active users."""
    for user, records in users_db.items():
        if isinstance(records, list):
            for r in records:
                if r.get("id") == request_id and not r.get("is_favorite", False):
                    r["is_favorite"] = True

def get_favorites(users_db: dict) -> list[dict]:
    """Return all favorited requests from every user's active list."""
    favs = []
    for records in users_db.values():
        if isinstance(records, list):
            favs.extend(r for r in records if r.get("is_favorite", False))
    return favs
