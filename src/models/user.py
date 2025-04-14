
class User:
    def __init__(self, id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role
    # --- Getters ---
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    # --- Setters (optional) ---
    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.id})"