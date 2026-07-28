# === Stage 51: Add unit tests for search and filter behavior ===
# Project: SupportPilot
import unittest


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        from support_pilot.board import Board, Request, FollowUp, Resolution
        self.board = Board()

    def test_search_by_owner_name(self):
        req1 = Request("client A", "help me", owner="alice")
        req2 = Request("client B", "info needed", owner="bob")
        board.add_request(req1)
        board.add_request(req2)
        results = self.board.search(owners=["alice"])
        self.assertEqual(len(results), 1)
        self.assertTrue(all(r.owner == "alice" for r in results))

    def test_search_by_subject_keyword(self):
        req1 = Request("client A", "login fails on Windows", owner="alice")
        req2 = Request("client B", "reset password", owner="bob")
        board.add_request(req1)
        board.add_request(req2)
        results = self.board.search(subjects=["windows"])
        self.assertEqual(len(results), 1)

    def test_search_by_status(self):
        req1 = Request("client A", "issue X", owner="alice")
        req2 = Request("client B", "issue Y", owner="bob")
        board.add_request(req1)
        board.add_request(req2)
        board.resolve(req1)
        results = self.board.search(statuses=["resolved"])
        self.assertEqual(len(results), 1)

    def test_search_empty_query(self):
        req1 = Request("client A", "issue X", owner="alice")
        board.add_request(req1)
        results = self.board.search()
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
