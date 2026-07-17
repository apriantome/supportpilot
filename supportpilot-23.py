# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: SupportPilot
def tag_request(req):
    """Return a single-line summary listing all non-empty tags of `req`."""
    return ", ".join(f"<{t}>" for t in req.tags if t) or "(untagged)"

def add_tags(req, tags):
    """Append new tags to an existing request list. Returns the updated dict."""
    req["tags"] = list(set(tags + (req.get("tags") or [])))
    return req

def remove_tags(req, tags_to_remove):
    """Remove specified tags from a request. Returns the updated dict."""
    keep = [t for t in (req.get("tags") or []) if t not in tags_to_remove]
    req["tags"] = keep
    return req
