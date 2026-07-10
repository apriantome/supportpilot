# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: SupportPilot
def update_request(request_id, updates):
    """Update a request's fields. Returns (updated_dict, success)."""
    try:
        idx = requests.index({r['requestId']: r for r in requests}[request_id])
        rec = dict(requests[idx])
        for k, v in updates.items():
            if k not in ('requestId',):
                rec[k] = v
        requests[idx] = rec
        return rec, True
    except KeyError:
        print(f"Request {request_id} not found")
        return None, False

def update_owner(owner_name, updates):
    """Update an owner's profile fields. Returns (updated_dict, success)."""
    try:
        idx = owners.index({o['ownerName']: o for o in owners}[owner_name])
        rec = dict(owners[idx])
        for k, v in updates.items():
            if k not in ('ownerName',):
                rec[k] = v
        owners[idx] = rec
        return rec, True
    except KeyError:
        print(f"Owner {owner_name} not found")
        return None, False

def update_followup(followup_id, updates):
    """Update a follow-up. Returns (updated_dict, success)."""
    try:
        idx = followups.index({f['followUpId']: f for f in followups}[followup_id])
        rec = dict(followups[idx])
        for k, v in updates.items():
            if k not in ('followUpId',):
                rec[k] = v
        followups[idx] = rec
        return rec, True
    except KeyError:
        print(f"Follow-up {followup_id} not found")
        return None, False

def update_resolution(resolution_id, updates):
    """Update a resolution. Returns (updated_dict, success)."""
    try:
        idx = resolutions.index({r['resolutionId']: r for r in resolutions}[resolution_id])
        rec = dict(resolutions[idx])
        for k, v in updates.items():
            if k not in ('resolutionId',):
                rec[k] = v
        resolutions[idx] = rec
        return rec, True
    except KeyError:
        print(f"Resolution {resolution_id} not found")
        return None, False

def update_metric(metric_name, value):
    """Update a service metric. Returns (updated_dict, success)."""
    try:
        idx = metrics.index({m['metricName']: m for m in metrics}[metric_name])
        rec = dict(metrics[idx])
        rec['value'] = value
        metrics[idx] = rec
        return rec, True
    except KeyError:
        print(f"Metric {metric_name} not found")
        return None, False
