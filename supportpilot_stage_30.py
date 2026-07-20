# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: SupportPilot
def parse_date(date_str: str) -> datetime.date:
    """Parse a date string in YYYY-MM-DD or DD/MM/YYYY format, returning a date object."""
    try:
        return datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        pass
    try:
        return datetime.datetime.strptime(date_str.strip(), "%d/%m/%Y").date()
    except ValueError:
        pass
    raise ValueError(f"Unsupported date format for '{date_str}'. Expected YYYY-MM-DD or DD/MM/YYYY.")

def parse_datetime(dt_str: str) -> datetime.datetime:
    """Parse a datetime string in YYYY-MM-DD HH:MM:SS format, returning a datetime object."""
    try:
        return datetime.datetime.strptime(dt_str.strip(), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(f"Unsupported datetime format for '{dt_str}'. Expected YYYY-MM-DD HH:MM:SS.")

def parse_duration(duration_str: str) -> timedelta:
    """Parse a duration string like '2 days 3 hours' or '1 week', returning a timedelta."""
    parts = duration_str.strip().lower()
    if "day" in parts and "hour" not in parts:
        return datetime.timedelta(days=int(parts.replace("days", "").replace("day", "")))
    if "week" in parts:
        return datetime.timedelta(weeks=int(parts.replace("weeks", "").replace("week", "")))
    raise ValueError(f"Unsupported duration format for '{duration_str}'. Expected 'X days', 'Y weeks'.")
