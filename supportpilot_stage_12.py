# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: SupportPilot
import json


def load_with_error_handling(file_path, default=None):
    """Load JSON from a file with friendly error handling for malformed data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return default if default is not None else {}
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{file_path}': {e}")
        return default if default is not None else {}
    except PermissionError:
        print(f"Error: Permission denied accessing '{file_path}'.")
        return default if default is not None else {}
