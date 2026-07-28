# === Stage 53: Add command help text and usage examples ===
# Project: SupportPilot
def print_help():
    """Display command help text and usage examples for SupportPilot."""
    help_text = f"""SupportPilot - Lightweight Support Triage Board

Usage: python support_pilot.py <command> [options]

Commands:
  add_request        Add a new support request to the board.
  list_requests      List all current requests with their owners and status.
  update_status      Update the status of a specific request (open, in_progress, resolved).
  add_owner          Assign an owner to a pending request.
  add_followup       Record a follow-up action for a given request.
  resolve_request    Mark a request as resolved with optional resolution notes.
  show_metrics       Display service metrics like total requests and average response time.

Options:
  -h, --help         Show this help message and exit.

Examples:
  python support_pilot.py add_request --title "Login Issue" --priority high --category auth
  python support_pilot.py list_requests --format table
  python support_pilot.py update_status --request_id REQ001 --status in_progress
  python support_pilot.py add_owner --request_id REQ001 --owner john_doe
  python support_pilot.py add_followup --request_id REQ001 --note "Checked logs, no errors found"
  python support_pilot.py resolve_request --request_id REQ001 --resolution "Fixed by restarting service"
  python support_pilot.py show_metrics

For more information about each command, run: python support_pilot.py <command> --help"""
    print(help_text)
