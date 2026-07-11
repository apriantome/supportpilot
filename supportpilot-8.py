# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: SupportPilot
def filter_requests(reqs, status=None, category=None, owner=None, tag=None):
    """Filter support requests by one or more criteria."""
    results = []
    for r in reqs:
        if status and r['status'] != status: continue
        if category and r.get('category') != category: continue
        if owner and r.get('owner') != owner: continue
        if tag and not any(tag == t for t in r.get('tags', [])): continue
        results.append(r)
    return results
