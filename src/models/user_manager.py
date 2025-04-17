import hashlib

class UserManager:
    def __init__(self, filename):
        self.filename = filename

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def load_users(self):
        users = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    username, hashed_password = line.strip().split(',')
                    users.append((username, hashed_password))
        except FileNotFoundError:
            print("File does not exist.")
        return users

    def save_user(self, username, password):
        hashed_password = self.hash_password(password)
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"{username},{hashed_password}\n")
        print(f"User information for '{username}' has been successfully saved to the file.")

    def user_exists(self, username: str) -> bool:
        users = self.load_users()
        for u, _ in users:
            if u == username:
                return True
        return False

    def register_user(self, username: str, password: str) -> bool:
        if self.user_exists(username):
            return False
        else:
            self.save_user(username, password)
            return True

    def verify_login(self, username: str, password: str) -> bool:
        hashed_input = self.hash_password(password)
        users = self.load_users()
        for u, hashed_pass in users:
            if u == username and hashed_pass == hashed_input:
                return True
        return False

    def reset_password(self, username: str, new_password: str) -> bool:
        # Check existence first
        if not self.user_exists(username):
            print(f"Username '{username}' not found. Password reset failed.")
            return False

        users = self.load_users()
        # Rewrite the entire file with updated password
        with open(self.filename, 'w', encoding='utf-8') as file:
            for u, hashed_pass in users:
                if u == username:
                    new_hashed = self.hash_password(new_password)
                    file.write(f"{u},{new_hashed}\n")
                else:
                    file.write(f"{u},{hashed_pass}\n")
        print(f"Password for '{username}' has been reset successfully.")
        return True

    def display_users(self): #Display user's account with username and hashed password. 
        users = self.load_users()
        if users:
            for index, (username, hashed_password) in enumerate(users,start = 1):
                print(f"Username {index}: {username}, Hashed password: {hashed_password}")
        else:
            print("No user information available.")
