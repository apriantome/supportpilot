# === Stage 42: Add CSV export without external dependencies ===
# Project: SupportPilot
import csv

def export_to_csv(board, filename="support_board.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for request in board.requests:
            owner = request.owner if hasattr(request, "owner") else None
            follow_ups = getattr(request, "follow_ups", [])
            resolution = getattr(request, "resolution", "")
            service_metrics = getattr(request, "service_metrics", {})

            writer.writerow([
                request.id,
                request.title,
                owner if isinstance(owner, str) else (owner.name if hasattr(owner, "name") else ""),
                ", ".join(follow_ups) if follow_ups else "",
                resolution,
                service_metrics.get("response_time", "") or "",
                service_metrics.get("resolution_time", "") or "",
            ])

export_to_csv(board, "support_board_export.csv")
