# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: SupportPilot
from datetime import datetime, timedelta


def upcoming_items(items: list[dict], days_ahead: int = 7) -> list[dict]:
    """Return items whose next_due is within `days_ahead` calendar days."""
    now = datetime.utcnow()
    return [
        item for item in items
        if (item.get("next_due") or item.get("created_at")) and _is_upcoming(item, now, days_ahead)
    ]


def _is_upcoming(item: dict, now: datetime, window_days: int) -> bool:
    due = datetime.fromisoformat(item["next_due"]) if isinstance(item["next_due"], str) else item["next_due"]
    return now <= due < now + timedelta(days=window_days)


def upcoming_followups(followups: list[dict], days_ahead: int = 7) -> list[dict]:
    """Return follow-ups that are due within `days_ahead`."""
    now = datetime.utcnow()
    return [
        f for f in followups
        if isinstance(f.get("due"), str) and datetime.fromisoformat(f["due"]) >= now
        and datetime.fromisoformat(f["due"]) < now + timedelta(days=days_ahead)
    ]


def upcoming_resolutions(resolutions: list[dict], days_ahead: int = 7) -> list[dict]:
    """Return items whose resolution is due within `days_ahead`."""
    return _is_upcoming_list(resolutions, days_ahead)


def _is_upcoming_list(items: list[dict], window_days: int) -> list[dict]:
    now = datetime.utcnow()
    return [
        i for i in items
        if isinstance(i.get("next_due"), str) and datetime.fromisoformat(i["next_due"]) >= now
        and datetime.fromisoformat(i["next_due"]) < now + timedelta(days=window_days)
    ]


def upcoming_requests(requests: list[dict], days_ahead: int = 7) -> list[dict]:
    """Return requests due within `days_ahead`."""
    return _is_upcoming_list(requests, days_ahead)
