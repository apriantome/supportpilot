# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: SupportPilot
def bulk_delete_requests(board, ids, confirm=False):
    """Delete multiple requests by ID; require explicit confirmation for safety."""
    if not ids:
        return []
    if not confirm and len(ids) > 10:
        raise ValueError(
            f"Refusing to delete {len(ids)} requests without explicit confirmation. "
            "Set confirm=True or provide fewer than 10 IDs."
        )

    deleted = []
    for rid in ids:
        if rid in board.requests:
            del board.requests[rid]
            deleted.append(rid)
    return deleted
