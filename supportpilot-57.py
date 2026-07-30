# === Stage 57: Add structured result objects for command handlers ===
# Project: SupportPilot
class TriageResult:
    """Structured result for a triage command handler."""
    def __init__(self, status="ok", message="", request_id=None):
        self.status = status
        self.message = message
        self.request_id = request_id

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "request_id": self.request_id,
        }

    def __repr__(self):
        return f"<TriageResult status={self.status!r}>"

class MetricSnapshot:
    """A compact snapshot of service metrics at a point in time."""
    def __init__(self, avg_resolution_time=None, open_count=None, owner_load=None):
        self.avg_resolution_time = avg_resolution_time
        self.open_count = open_count
        self.owner_load = owner_load

    def to_dict(self):
        return {
            "avg_resolution_time": self.avg_resolution_time,
            "open_count": self.open_count,
            "owner_load": self.owner_load,
        }

    def __repr__(self):
        parts = []
        if self.avg_resolution_time is not None:
            parts.append(f"avg_res={self.avg_resolution_time:.1f}s")
        if self.open_count is not None:
            parts.append(f"open={self.open_count}")
        if self.owner_load is not None:
            parts.append(f"load={self.owner_load:.2%}")
        return f"<MetricSnapshot {', '.join(parts)}>"
