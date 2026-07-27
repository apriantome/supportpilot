# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: SupportPilot
import unittest
from support_pilot.core.board import Board

class TestBoardUpdateDelete(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_update_nonexistent_request_raises_error(self):
        with self.assertRaises(ValueError):
            self.board.update_request("999", {"status": "closed"})

    def test_delete_nonexistent_request_raises_error(self):
        with self.assertRaises(ValueError):
            self.board.delete_request("999")

    def test_update_and_delete_same_request(self):
        request_id = "100"
        self.board.add_request(request_id, {"subject": "test", "status": "open"})
        self.board.update_request(request_id, {"status": "closed"})
        self.board.delete_request(request_id)

    def test_update_preserves_existing_fields(self):
        request_id = "200"
        self.board.add_request(request_id, {"subject": "original", "priority": "high"})
        self.board.update_request(request_id, {"status": "closed"})
        requests = self.board.get_all_requests()
        updated = [r for r in requests if r["request_id"] == request_id][0]
        self.assertEqual(updated["subject"], "original")

    def test_delete_removes_from_all_views(self):
        request_id = "300"
        self.board.add_request(request_id, {"subject": "to be deleted"})
        requests = self.board.get_all_requests()
        self.assertTrue(any(r["request_id"] == request_id for r in requests))
        self.board.delete_request(request_id)
        requests_after = self.board.get_all_requests()
        self.assertFalse(any(r["request_id"] == request_id for r in requests_after))

if __name__ == "__main__":
    unittest.main()
