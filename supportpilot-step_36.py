# === Stage 36: Add templates for quickly creating common records ===
# Project: SupportPilot
def new_request_record():
    return {
        'request_id': f'REQ-{int(time.time()) % 10_000}',
        'subject': '',
        'description': '',
        'priority': 'medium',
        'status': 'open',
        'owner': None,
        'created_at': datetime.now().isoformat(),
    }

def new_follow_up(record_id):
    return {
        'follow_up_id': f'FU-{int(time.time()) % 10_000}',
        'record_id': record_id,
        'note': '',
        'assigned_to': None,
        'due_date': None,
        'created_at': datetime.now().isoformat(),
    }

def new_resolution(record):
    return {
        'resolution_id': f'RES-{int(time.time()) % 10_000}',
        'record_id': record.get('request_id', ''),
        'solution': '',
        'resolved_by': None,
        'closed_at': datetime.now().isoformat(),
    }

def new_owner_record():
    return {
        'owner_id': f'OWN-{int(time.time()) % 10_000}',
        'name': '',
        'email': '',
        'role': 'support_agent',
        'capacity': 5,
        'current_load': 0,
    }

def new_service_metric():
    return {
        'metric_id': f'MET-{int(time.time()) % 10_000}',
        'name': '',
        'description': '',
        'threshold': None,
        'alert_enabled': False,
        'last_value': None,
        'timestamp': datetime.now().isoformat(),
    }
