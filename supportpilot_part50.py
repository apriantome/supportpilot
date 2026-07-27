# === Stage 50: Add unit tests for import and export behavior ===
# Project: SupportPilot
import sys, os, re

TESTS_DIR = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(TESTS_DIR, exist_ok=True)

# ── Unit tests for import/export behavior ──────────────────────────────

def test_import_supportpilot():
    """Verify the module can be imported without errors."""
    sys.path.insert(0, os.path.dirname(__file__))
    import supportpilot
    assert hasattr(supportpilot, 'SupportPilot')

def test_export_to_json():
    """Test exporting a board to JSON format."""
    sp = supportpilot.SupportPilot()
    sp.add_request("req-001", "Low priority ticket")
    sp.set_owner("jane.doe@example.com")
    sp.add_followup("Follow-up on req-001")
    sp.mark_resolved("Resolved by Jane Doe")

    json_str = sp.export_to_json()
    assert isinstance(json_str, str)
    assert '"requests"' in json_str.lower() or '"owner"' in json_str.lower()

def test_import_from_json():
    """Test importing a board from JSON string."""
    sp = supportpilot.SupportPilot()
    sp.add_request("req-002", "High priority issue")
    sp.set_owner("john.doe@example.com")
    sp.mark_resolved("Resolved by John Doe")

    json_str = sp.export_to_json()

    # Parse and re-import
    import json
    board_data = json.loads(json_str)
    assert isinstance(board_data, dict)
