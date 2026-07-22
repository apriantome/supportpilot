# === Stage 38: Add data integrity checks for broken references ===
# Project: SupportPilot
def check_references(records):
    """Validate that all owner and follow-up references are intact."""
    owners = {r['owner'] for r in records if 'owner' in r}
    followups = [r for r in records if 'follow_ups' in r]
    broken = []
    for fu in followups:
        ref = fu.get('resolution_ref') or fu.get('current_owner')
        if ref and ref not in owners:
            broken.append({'type': fu['id'], 'ref': ref, 'status': 'broken'})
    return broken
