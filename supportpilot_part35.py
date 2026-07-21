# === Stage 35: Add active user switching and user-specific records ===
# Project: SupportPilot
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def is_active(self):
        return True

    def mark_inactive(self):
        self.is_active = False


def add_users():
    users = []
    for i in range(1, 6):
        user = User(f"User{i}", f"user{i}@example.com")
        if i % 2:
            user.mark_inactive()
        users.append(user)
    return users
