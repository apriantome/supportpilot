# === Stage 55: Add a setting to disable colorized output ===
# Project: SupportPilot
# settings.py — disable colorized output when no TTY is available
import os


def _is_terminal():
    """Return True if stdout is an interactive terminal."""
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def use_color():
    """Color support: ON by default; OFF when not on a TTY or env flag set.

    Environment variable ``SUPPORTPILOT_NO_COLOR`` (truthy) forces colour off
    regardless of terminal state — useful for CI, piped output, etc.
    """
    if os.environ.get("SUPPORTPILOT_NO_COLOR", "").strip().lower() in ("1", "true", "yes"):
        return False
    return _is_terminal()


# Expose a module-level flag so other files can read it without importing this one.
USE_COLOR = use_color()
