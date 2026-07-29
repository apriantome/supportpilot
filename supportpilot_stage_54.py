# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: SupportPilot
def colorize(text, fg=None):
    """Apply ANSI colour to text: return unchanged if no colour given."""
    codes = {"red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
             "cyan": "\033[36m", "bold": "\033[1m"}
    if fg is None:
        return text
    prefix = codes.get(fg) or ""
    suffix = "\033[0m"  # reset
    return prefix + text + suffix

def print_status_table(statuses):
    """Pretty-print a list of dicts with colour by status key."""
    header = ["ID", "Owner", "Status", "Follow-ups"]
    print(colorize("─" * 80, "cyan"))
    for h in header:
        print(f"{colorize(h.center(20), 'yellow')}")
    print(colorize("─" * 80, "cyan"))
    for s in statuses:
        row = [str(s.get(k, "")) for k in header]
        print(colorize(row[0], "bold"), "|",
              colorize(str(s["owner"]), "green") if s["owner"] else str(s["owner"]),
              "|", colorize(str(s["status"]), {"open": "yellow", "resolved": "green"}.get(s["status"], "")),
              "|", row[3])

# Example usage:
if __name__ == "__main__":
    demo = [
        {"id": 1, "owner": "Alice",   "status": "open",     "follow-ups": 2},
        {"id": 2, "owner": "Bob",     "status": "resolved", "follow-ups": 0},
        {"id": 3, "owner": "",        "status": "backlog",  "follow-ups": 1},
    ]
    print_status_table(demo)
