# === Stage 16: Add argparse support for the most common commands ===
# Project: SupportPilot
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="SupportPilot - lightweight support triage board")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list requests
    p_list = subparsers.add_parser("list", help="List all support requests")
    p_list.add_argument("--status", choices=["open","in_progress","resolved"], help="Filter by status")

    # show request details
    p_show = subparsers.add_parser("show", help="Show a single request by ID")
    p_show.add_argument("request_id", type=int, help="Request identifier")

    # add follow-up
    p_followup = subparsers.add_parser("followup", help="Add a follow-up to an existing request")
    p_followup.add_argument("request_id", type=int)
    p_followup.add_argument("--user", required=True, help="Who is following up")
    p_followup.add_argument("--message", required=True, help="Follow-up message")

    # resolve a request
    p_resolve = subparsers.add_parser("resolve", help="Mark a request as resolved")
    p_resolve.add_argument("request_id", type=int)
    p_resolve.add_argument("--resolution", default="", help="Resolution note (optional)")

    return parser
