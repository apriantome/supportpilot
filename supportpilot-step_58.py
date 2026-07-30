# === Stage 58: Add bulk update behavior for selected records ===
# Project: SupportPilot
def bulk_update_records(self, records: list[dict]) -> int:
    """Update multiple records in one call and return how many were changed."""
    if not records:
        return 0
    changed = 0
    for rec in records:
        key = tuple(sorted(rec.items()))
        if key != self._records[key]:
            self._records[key] = dict(rec)
            changed += 1
    return changed
