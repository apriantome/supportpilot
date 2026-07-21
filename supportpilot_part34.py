# === Stage 34: Add support for multiple local user profiles ===
# Project: SupportPilot
import json, os

def load_profiles():
    """Load user profiles from a local JSON file."""
    path = "profiles.json"
    if not os.path.exists(path):
        return [{"id": 1, "name": "Admin", "email": "admin@example.com", "role": "admin"}]
    with open(path) as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = [data]
    return data

def save_profiles(profiles):
    """Save user profiles to a local JSON file."""
    os.makedirs("data", exist_ok=True)
    with open("data/profiles.json", "w") as f:
        json.dump(profiles, f, indent=2)

def get_profile(user_id):
    """Get a single profile by ID."""
    profiles = load_profiles()
    for p in profiles:
        if p["id"] == user_id:
            return p
    return None
