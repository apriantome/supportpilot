# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: SupportPilot
import datetime

def archive_records(records, cutoff=None):
    if cutoff is None:
        cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=365)
    archived = []
    for r in records:
        if (r.get("status") == "resolved" or r.get("status") == "closed") and \
           (not r.get("created_at") or datetime.datetime.fromisoformat(r["created_at"]) < cutoff):
            r["archived"] = True
            archived.append(r)
    return archived

def restore_records(archive, records=None):
    if records is None:
        records = []
    for a in archive:
        a.pop("archived", None)
        records.append(a)
    return records
