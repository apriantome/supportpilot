# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: SupportPilot
def dry_run_mode():
    """Enable a global dry-run flag that, when True, makes every mutating command
    print what *would* happen instead of actually changing anything."""
    import sys
    if '--dry-run' in sys.argv:
        return True
    return False


def _apply_dry_run(func):
    def wrapper(*args, **kwargs):
        if dry_run_mode():
            print(f"[DRY RUN] Would execute: {func.__name__}({', '.join(repr(a) for a in args)})")
        else:
            return func(*args, **kwargs)
    return wrapper


# Apply the decorator to every mutating function so they automatically respect --dry-run.
mutating = [
    create_request, update_owner, close_request, resolve_ticket, mark_follow_up,
    add_metric, delete_request, bulk_assign, archive_board, export_report,
]

for func in mutating:
    _apply_dry_run(func)
