import hashlib

class UserManager:
    def __init__(self, filename):
        self.filename = filename
        self.users_dict = {}
        self.load_users()

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def load_users(self):
        self.users_dict.clear()
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        username, hashed_password = line.split(',', 1)
                        self.users_dict[username] = hashed_password
        except FileNotFoundError:
            print("File does not exist.")

    def save_user(self, username, password):
        hashed_password = self.hash_password(password)
        self.users_dict[username] = hashed_password
        self._write_all_users_to_file()
        print(f"User information for '{username}' has been successfully saved to the file.")

    def _write_all_users_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for u, p in self.users_dict.items():
                file.write(f"{u},{p}\n")

    def user_exists(self, username: str) -> bool:
        return username in self.users_dict

    def register_user(self, username: str, password: str) -> bool:
        if self.user_exists(username):
            return False
        self.save_user(username, password)
        return True

    def verify_login(self, username: str, password: str) -> bool:
        hashed_input = self.hash_password(password)
        return self.users_dict.get(username) == hashed_input

    def reset_password(self, username: str, new_password: str) -> bool:
        if not self.user_exists(username):
            print(f"Username '{username}' not found. Password reset failed.")
            return False

        new_hashed = self.hash_password(new_password)
        self.users_dict[username] = new_hashed
        self._write_all_users_to_file()
        print(f"Password for '{username}' has been reset successfully.")
        return True

    def display_users(self):
        if self.users_dict:
            for index, (username, hashed_password) in enumerate(self.users_dict.items(), start=1):
                print(f"Username {index}: {username} --- Hashed password: {hashed_password}")
        else:
            print("No user information available.")
