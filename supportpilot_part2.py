# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: SupportPilot
from __future__ import annotations
import dataclasses
from datetime import date, timedelta
from typing import Optional


@dataclasses.dataclass(frozen=True)
class SupportRequest:
    id: str
    title: str
    description: str
    status: str  # open | triaged | resolved | closed
    priority: int = 1          # 1=low … 5=critical
    owner_id: Optional[str] = None
    created: date = dataclasses.field(default_factory=lambda: date.today())
    updated: date = dataclasses.field(default_factory=lambda: date.today())

    @property
    def age_days(self) -> int:
        return (date.today() - self.created).days


@dataclasses.dataclass(frozen=True)
class FollowUp:
    request_id: str
    author: str
    note: str
    due_date: Optional[date] = None

    @property
    def overdue(self) -> bool:
        return (self.due_date is not None) and self.due_date < date.today()


@dataclasses.dataclass(frozen=True)
class Resolution:
    request_id: str
    summary: str
    closed_by: str
    closed_on: date = dataclasses.field(default_factory=lambda: date.today())
