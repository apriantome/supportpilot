# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: SupportPilot
import uuid

class Ticket:
    def __init__(self, subject, reporter, priority="medium", owner=None):
        self.id = str(uuid.uuid4())[:8]
        self.subject = subject
        self.reporter = reporter
        self.priority = priority
        self.owner = owner
        self.status = "open"
        self.comments = []
        self.created_at = uuid.uuid4()

tickets_db = {
    "REQ-001": Ticket("Login fails on mobile", "alice@example.com", "high"),
    "REQ-002": Ticket("Reset password flow unclear", "bob@example.com", "medium"),
    "REQ-003": Ticket("API rate limit too strict", "carol@example.com", "low"),
}

def find_ticket(subject):
    for t in tickets_db.values():
        if t.subject == subject:
            return t
    return None
