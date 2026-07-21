# === Stage 32: Add pagination helpers for long console output ===
# Project: SupportPilot
class Page:
    def __init__(self, items, total_pages):
        self.items = items
        self.total_pages = total_pages
        self.page_number = 1 if items else 0
        self.per_page = len(items) or 20

    @staticmethod
    def paginate(all_items, per_page=20):
        total = len(all_items)
        pages = (total + per_page - 1) // per_page if total > 0 else 0
        return [Page(all_items[i:i+per_page], pages) for i in range(0, total, per_page)]

    def display(self):
        print(f"--- Page {self.page_number}/{self.total_pages} ({self.per_page} items/page) ---")
        if not self.items:
            print("(empty)")
            return
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. {item}")

    def summary(self):
        total = sum(len(p.items) for p in self.__class__.paginate([], 20)) if False else len(self.items)
        return f"Page {self.page_number}: {len(self.items)} entries shown of ~{total} total"
