# === Stage 43: Add CSV import for the primary record type ===
# Project: SupportPilot
def import_requests_from_csv(file_path):
    """Import SupportRequest records from a CSV file."""
    requests = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                request_id = int(row['id']) if row.get('id') else None
                title = row['title']
                category = row['category']
                priority = row['priority']
                status = row['status']
                owner_email = row['owner_email']
                created_at = datetime.fromisoformat(row['created_at']).replace(tzinfo=None) if row.get('created_at') else None

                follow_ups = []
                for fu in csv.DictReader(open(os.path.join(file_path, 'followups.csv'), 'r', encoding='utf-8')):
                    if fu['request_id'] == str(request_id):
                        follow_ups.append({
                            'date': datetime.fromisoformat(fu['date']).replace(tzinfo=None) if fu.get('date') else None,
                            'summary': fu['summary'],
                            'status': fu['status'],
                        })

                resolution = row.get('resolution', '')
                request_id = int(row['id']) if row.get('id') else None
            except (KeyError, ValueError):
                continue

            requests.append({
                'request_id': request_id,
                'title': title,
                'category': category,
                'priority': priority,
                'status': status,
                'owner_email': owner_email,
                'created_at': created_at,
                'follow_ups': follow_ups,
                'resolution': resolution,
            })

    return requests
