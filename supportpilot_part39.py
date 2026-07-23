# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: SupportPilot
def repair_board(board):
    """Fix simple integrity issues: missing statuses, empty owners, and stale timestamps."""
    for req in board.requests:
        if not req.status:
            req.status = "open"
        if not req.owner:
            req.owner = "unassigned"
        if not req.created_at:
            req.created_at = datetime.now()
        if not req.updated_at:
            req.updated_at = datetime.now()
    for follow in board.followups:
        if not follow.status:
            follow.status = "pending"
        if not follow.owner:
            follow.owner = "unassigned"
    return board
