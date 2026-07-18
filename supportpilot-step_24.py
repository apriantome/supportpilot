# === Stage 24: Add grouped summaries by category or status ===
# Project: SupportPilot
def grouped_summary(board):
    groups = {}
    for req in board:
        key = (req["category"], req["status"])
        groups.setdefault(key, []).append(req)
    out = []
    for (cat, st), items in sorted(groups.items()):
        owners = {r.get("owner") for r in items if "owner" in r}
        out.append({
            "group": {"category": cat, "status": st},
            "count": len(items),
            "owners": sorted(owners) if owners else [],
            "avg_time_hours": (
                sum(r.get("time_to_resolve_hrs", 0) for r in items) / len(items)
                if any("time_to_resolve_hrs" in r for r in items) else None
            ),
        })
    return out
