# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: SupportPilot
def _sort_key(record):
    return (record['priority'], record.get('date', ''), record.get('last_update', ''))

def _apply_sort(records, field='title'):
    if not records:
        return []
    
    # Normalize the title to lowercase for case-insensitive sorting
    def normalize_title(r):
        return r[field].lower() if isinstance(r[field], str) else r[field] or ''
    
    sorted_records = sorted(records, key=lambda r: (normalize_title(r), _sort_key(r)))
    return sorted_records

def display_sorted_board(sorted_data):
    """Display the sorted support board."""
    if not sorted_data:
        print("No requests found.")
        return
    
    # Print header with column names
    print(f"{'ID':<6} {'Priority':<12} {'Title':<35} {'Date':<10} {'Last Update':<15}")
    print("-" * 78)
    
    for record in sorted_data:
        title = record.get('title', '')[:34] if isinstance(record['title'], str) else ''
        date = record.get('date', '-') or '-'
        last_update = record.get('last_update', '-') or '-'
        
        print(f"{record['id']:<6} {record['priority']:<12} {title:<35} {date:<10} {last_update:<15}")

# Example usage:
# sorted_board = _apply_sort(requests, field='title')
# display_sorted_board(sorted_board)
