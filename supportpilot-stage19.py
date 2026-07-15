# === Stage 19: Add undo support for the last simple mutation ===
# Project: SupportPilot
def undo_last_mutation():
    """Undo the last simple mutation to restore previous state."""
    if not _mutation_stack:
        print("No mutations to undo.")
        return False
    
    last_action = _mutation_stack.pop()
    
    if isinstance(last_action, ('resolve_request', 'assign_owner')):
        # Restore original status
        request_id = last_action.get('request_id')
        if request_id in requests_db:
            old_status = requests_db[request_id].get('status', '')
            requests_db[request_id]['status'] = old_status
    
    elif isinstance(last_action, ('update_followup')):
        # Restore previous follow-up text or date
        followup_id = last_action.get('followup_id')
        if followup_id in followups_db:
            prev_data = last_action.get('previous_data', {})
            for key, value in prev_data.items():
                followups_db[followup_id][key] = value
    
    elif isinstance(last_action, ('add_request')):
        # Remove the request if it was just added
        request_id = last_action.get('request_id')
        if request_id in requests_db:
            del requests_db[request_id]
    
    elif isinstance(last_action, ('remove_owner')):
        # Re-add owner to request
        request_id = last_action.get('request_id')
        owner_email = last_action.get('owner_email')
        if request_id in requests_db and owner_email:
            requests_db[request_id]['assigned_to'] = owner_email
    
    elif isinstance(last_action, ('add_owner')):
        # Remove owner from request
        request_id = last_action.get('request_id')
        owner_email = last_action.get('owner_email')
        if request_id in requests_db and owner_email:
            del requests_db[request_id]['assigned_to']
    
    return True
