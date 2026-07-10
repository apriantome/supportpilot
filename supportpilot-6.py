# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: SupportPilot
def delete_request(self, request_id: str) -> bool:
    """Delete a support request if it has no follow-ups and is resolved."""
    req = self.requests.get(request_id)
    if not req or req.status != "resolved":
        return False
    if req.follow_ups:
        return False
    del self.requests[request_id]
    print(f"Deleted request {request_id}")
    return True

def delete_followup(self, request_id: str, followup_index: int) -> bool:
    """Remove a specific follow-up from a resolved request."""
    req = self.requests.get(request_id)
    if not req or req.status != "resolved":
        return False
    if 0 <= followup_index < len(req.follow_ups):
        del req.follow_ups[followup_index]
        print(f"Deleted follow-up {followup_index} from request {request_id}")
        return True
    return False

def delete_response(self, request_id: str) -> bool:
    """Remove a resolved request's response and the request itself."""
    req = self.requests.get(request_id)
    if not req or req.status != "resolved":
        return False
    del self.responses[request_id]
    del self.requests[request_id]
    print(f"Deleted request {request_id} and its response")
    return True

def delete_owner(self, owner_id: str) -> bool:
    """Remove an owner record if they have no active or pending requests."""
    if not any(o["id"] == owner_id for o in self.owners):
        return False
    owners = [o for o in self.owners if o["id"] != owner_id]
    if any(r["owner_id"] == owner_id and r.status in ("open", "pending") for r in self.requests.values()):
        return False
    del self.owners[self.owners.index(next(o for o in self.owners if o["id"] == owner_id))]
    print(f"Deleted owner {owner_id}")
    return True

def delete_service_level(self, request_id: str) -> bool:
    """Delete a service-level agreement record."""
    slas = [s for s in self.service_levels.values()]
    if any(s["request_id"] == request_id for s in slas):
        del self.service_levels[request_id]
        print(f"Deleted SLA for request {request_id}")
        return True
    return False
