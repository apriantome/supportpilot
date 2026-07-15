# === Stage 18: Add an activity log with timestamps and action names ===
# Project: SupportPilot
class ActivityLog:
    """Records timestamped actions for audit and metrics."""

    def __init__(self):
        self._entries = []

    def log(self, action: str, user_id: int, details: str = "") -> "Entry":
        entry = Entry(action=action, user_id=user_id, details=details, timestamp=datetime.now())
        self._entries.append(entry)
        return entry

    @property
    def entries(self):
        return list(self._entries)

    def __len__(self):
        return len(self._entries)


class Entry:
    """Immutable record of a single action."""

    def __init__(self, action: str, user_id: int, details: str = "", timestamp: datetime = None):
        self.action = action
        self.user_id = user_id
        self.details = details or ""
        self.timestamp = timestamp or datetime.now()

    def to_dict(self) -> dict:
        return {
            "action": self.action,
            "user_id": self.user_id,
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
        }

    def __repr__(self):
        return f"Entry({self.action}, user={self.user_id}, ts={self.timestamp})"
