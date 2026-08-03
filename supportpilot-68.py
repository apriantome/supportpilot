# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: SupportPilot
def generate_changelog(activity_log, max_entries=5):
    """Generate a compact changelog from an activity log."""
    if not activity_log:
        return []
    
    entries = sorted(set(activity_log), key=lambda x: len(x), reverse=True)[:max_entries]
    lines = [f"## Changelog\n"]
    for entry in entries:
        lines.append(f"- {entry}")
    return "\n".join(lines)
