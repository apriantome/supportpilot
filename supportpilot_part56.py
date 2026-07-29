# === Stage 56: Add compact error classes for domain failures ===
# Project: SupportPilot
class SupportError(Exception):
    """Base class for all SupportPilot domain errors."""
    pass


class RequestNotFoundError(SupportError):
    """Raised when a request with the given ID does not exist in any store."""
    def __init__(self, request_id: str) -> None:
        self.request_id = request_id
        super().__init__(f"Request '{request_id}' not found.")


class DuplicateOwnerError(SupportError):
    """Raised when a user tries to claim an already-owned request."""
    def __init__(self, owner_email: str) -> None:
        self.owner_email = owner_email
        super().__init__(f"User '{owner_email}' already owns this request.")


class ResolutionConflict(SupportError):
    """Raised when a resolution is set on a non-resolved request or changes an existing status."""
    def __init__(self, current_status: str) -> None:
        self.current_status = current_status
        super().__init__(f"Cannot resolve while current status is '{current_status}'.")


class InvalidFollowUp(SupportError):
    """Raised when a follow-up is attached to the wrong request or by an unauthorised user."""
    def __init__(self, detail: str) -> None:
        self.detail = detail
        super().__init__(f"Invalid follow-up: {detail}")


class MetricCalculationError(SupportError):
    """Raised when service metrics cannot be computed from the stored data."""
    pass
