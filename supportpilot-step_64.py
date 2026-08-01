# === Stage 64: Add validation for relationship references ===
# Project: SupportPilot
def validate_relationship_refs(requests_data, owners_data):
    """Validate that all relationship references in requests and owners are valid."""
    errors = []
    
    # Validate request references to owners
    for req_id, req_info in requests_data.items():
        if 'owner' not in req_info:
            continue
        owner_ref = req_info['owner']
        if owner_ref not in owners_data:
            errors.append(f"Request {req_id} references non-existent owner '{owner_ref}'")
    
    # Validate owner self-references (optional constraint)
    for oid, oinfo in owners_data.items():
        if 'requests' not in oinfo:
            continue
        for ref in oinfo['requests']:
            if ref not in requests_data and ref != 'none':
                errors.append(f"Owner {oid} references non-existent request '{ref}'")
    
    return errors
