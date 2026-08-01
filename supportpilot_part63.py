# === Stage 63: Add relationships between records where useful ===
# Project: SupportPilot
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent / "supportpilot.json"
DATA = json.loads(REPO.read_text()) if REPO.exists() else {"requests": [], "owners": [], "follow_ups": [], "resolutions": []}


def link_request_to_owner(request_id: str, owner_name: str) -> None:
    for r in DATA["requests"]:
        if r["id"] == request_id:
            r.setdefault("assigned_to", []).append(owner_name)
            break


def link_follow_up_to_request(fu_id: str, req_id: str) -> None:
    for fu in DATA["follow_ups"]:
        if fu["id"] == fu_id:
            fu["request_id"] = req_id
            break


def link_resolution_to_request(res_id: str, req_id: str) -> None:
    for res in DATA["resolutions"]:
        if res["id"] == res_id:
            res["request_id"] = req_id
            break


if __name__ == "__main__":
    # Example linking existing records together.
    link_request_to_owner("req-001", "alice")
    link_follow_up_to_request("fu-004", "req-002")
    link_resolution_to_request("res-003", "req-001")

    REPO.write_text(json.dumps(DATA, indent=2))
