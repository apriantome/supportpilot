# === Stage 41: Add plain text import for a simple line-based format ===
# Project: SupportPilot
def load_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        return [line.rstrip("\n\r") for line in f if line.strip()]
