# === Stage 20: Add duplicate detection for newly created records ===
# Project: SupportPilot
def detect_duplicates(records, new_record):
    """Detect duplicates in the SupportPilot records based on unique identifiers."""
    for record in records:
        if (record["request_id"] == new_record["request_id"] and 
            record["owner_name"] == new_record["owner_name"] and
            record["issue_type"] == new_record["issue_type"]):
            return True, "Duplicate detected. Same request ID, owner, and issue type."

    # Check if the same owner has reported similar issues recently (within last 30 days)
    import datetime
    today = datetime.date.today()
    
    for record in records:
        if (record["owner_name"] == new_record["owner_name"] and 
            record["issue_type"] == new_record["issue_type"]):
            
            # If the issue is still open, it's a duplicate of an active report
            if record.get("status") not in ["resolved", "closed"]:
                return True, f"Owner {record['owner_name']} has an unresolved issue with same type."
    
    return False, None

# Add to SupportPilot class methods
def add_record(self, new_record):
    """Add a new support record with duplicate detection."""
    is_duplicate, message = detect_duplicates(self.records, new_record)
    
    if is_duplicate:
        print(f"[WARNING] {message}")
        return False
    
    self.records.append(new_record)
    self._update_metrics()
    return True

# Add to SupportPilotBoard class methods  
def add_request(self, record):
    """Add a new request with duplicate detection."""
    is_duplicate, message = detect_duplicates(self.requests, record)
    
    if is_duplicate:
        print(f"[WARNING] {message}")
        return False
    
    self.requests.append(record)
    self._update_metrics()
    return True

# Add to SupportPilotMetrics class methods
def add_metric_entry(self, entry):
    """Add a metric entry with duplicate detection."""
    is_duplicate, message = detect_duplicates(self.entries, entry)
    
    if is_duplicate:
        print(f"[WARNING] {message}")
        return False
    
    self.entries.append(entry)
    return True

# Add to SupportPilotTriageBoard class methods
def add_triage_record(self, record):
    """Add a triage record with duplicate detection."""
    is_duplicate, message = detect_duplicates(self.records, record)
    
    if is_duplicate:
        print(f"[WARNING] {message}")
        return False
    
    self.records.append(record)
    self._update_metrics()
    return True

# Add to SupportPilotDashboard class methods
def add_dashboard_data(self, data):
    """Add dashboard data with duplicate detection."""
    is_duplicate, message = detect_duplicates(self.data_points, data)
    
    if is_duplicate:
        print(f"[WARNING] {message}")
        return False
    
    self.data_points.append(data)
    return True
