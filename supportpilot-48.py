# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: SupportPilot
import pytest
from support_pilot.models import Ticket, Status


def test_ticket_creation():
    ticket = Ticket(
        id=1001,
        subject="Login fails on mobile",
        description="Cannot sign in after update.",
        status=Status.OPEN,
        priority=Priority.HIGH,
        owner_id=None,
        created_at="2024-06-15T09:30:00Z",
    )
    assert ticket.id == 1001
    assert ticket.status == Status.OPEN
    assert ticket.owner_id is None


def test_ticket_validation():
    with pytest.raises(ValueError):
        Ticket(
            subject="Missing ID",
            status=Status.CLOSED,
        )


def test_status_transitions():
    t = Ticket(id=1002, subject="Test", status=Status.OPEN)
    assert Status.can_transition(t.status, Status.IN_PROGRESS) is True
    assert Status.can_transition(Status.IN_PROGRESS, Status.OPEN) is False
