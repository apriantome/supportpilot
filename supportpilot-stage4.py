# === Stage 4: Implement create operations for the primary records ===
# Project: SupportPilot
def create_request(self, title: str, description: str = "", priority: int = 1) -> Request:
    """Create a new support request."""
    return Request(
        id=next_id(),
        title=title,
        description=description or "No details provided.",
        created_at=datetime.now(timezone.utc),
        status="open",
        priority=priority,
    )

def create_ownership(self, owner: str) -> Ownership:
    """Create an ownership record."""
    return Ownership(
        id=next_id(),
        owner=owner,
        created_at=datetime.now(timezone.utc),
    )

def create_followup(self, request_id: int, note: str = "") -> FollowUp:
    """Create a follow-up entry for an existing request."""
    return FollowUp(
        id=next_id(),
        request_id=request_id,
        created_at=datetime.now(timezone.utc),
        status="open",
        priority=1,
        note=note or "No details provided.",
    )

def create_resolution(self, request_id: int) -> Resolution:
    """Resolve an existing support request."""
    return Resolution(
        id=next_id(),
        request_id=request_id,
        created_at=datetime.now(timezone.utc),
        status="resolved",
        priority=1,
    )
