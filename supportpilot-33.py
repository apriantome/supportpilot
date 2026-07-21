# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: SupportPilot
def load_settings():
    return {
        'max_requests': 50,
        'default_priority': 'medium',
        'followup_days': 7,
        'escalation_hours': 24,
        'resolution_target_days': 30,
        'display_languages': ['en'],
        'timezone': 'UTC'
    }

def update_settings(settings, key, value):
    if key not in settings:
        raise KeyError(f"Unknown setting: {key}")
    settings[key] = value
    return settings

settings = load_settings()
