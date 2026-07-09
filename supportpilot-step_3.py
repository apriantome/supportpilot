# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: SupportPilot
def validate_request(req):
    if not isinstance(req, dict) or 'id' not in req:
        raise ValueError("Request must have a unique ID")
    if not isinstance(req['status'], str) or req['status'] not in ('open', 'in_progress', 'resolved'):
        raise ValueError(f"Invalid status '{req['status']}'")
    if req.get('title') and (not isinstance(req['title'], str) or len(req['title']) > 200):
        raise ValueError("Title must be a string <= 200 chars")
    return True
