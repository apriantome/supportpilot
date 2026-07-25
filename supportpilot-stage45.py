# === Stage 45: Add restore from backup with validation ===
# Project: SupportPilot
def restore(self, archive_path: str) -> bool:
        """Restore board state from a JSON backup and validate integrity."""
        import json
        with open(archive_path, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Backup must be a JSON object")
        required_keys = {"requests": list, "owners": list}
        for k, v in required_keys.items():
            if k not in data or not isinstance(data[k], v):
                raise ValueError(f"Missing or invalid key: {k}")
        self._state["requests"] = data["requests"]
        self._state["owners"] = data["owners"]
        return True
