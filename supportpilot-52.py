# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: SupportPilot
def resolve_ticket(ticket: Ticket, resolution: str) -> None:
    """Mark a ticket as resolved with the given reason."""
    if ticket.status != "open":
        raise ValueError(f"Cannot resolve a {ticket.status} ticket")
    ticket.resolution = resolution
    ticket.status = "resolved"

def escalate_ticket(ticket: Ticket, priority: str) -> None:
    """Upgrade a ticket's priority and notify its owner."""
    if not (1 <= int(priority) <= 5):
        raise ValueError("Priority must be between 1 and 5")
    ticket.priority = int(priority)
    ticket.escalated_at = datetime.datetime.now()

def generate_summary(ticket: Ticket) -> str:
    """Return a human-readable summary of the ticket history."""
    parts = [f"[#{ticket.id}] {ticket.title} ({ticket.status})"]
    if ticket.owner:
        parts.append(f"Owner: {ticket.owner.name}")
    if ticket.resolution:
        parts.append(f"Resolved: {ticket.resolution}")
    return " | ".join(parts)
