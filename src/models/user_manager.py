import hashlib

class UserManager:
    def __init__(self, filename):
        self.filename = filename

    def hash_password(self, password):
        """
        Hashes the given password using SHA-256 and returns the hexadecimal digest.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def load_users(self):
        """
        Reads all user information from the file (CSV format),
        and returns it as a list of (username, hashed_password) tuples.
        """
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
        """
        Appends the given user (username, hashed password) to the CSV file.
        """
        hashed_password = self.hash_password(password)
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"{username},{hashed_password}\n")
        print(f"User information for '{username}' has been successfully saved to the file.")

    def user_exists(self, username: str) -> bool:
        """
        Checks if the given username already exists in the file.
        """
        users = self.load_users()
        for u, _ in users:
            if u == username:
                return True
        return False

    def register_user(self, username: str, password: str) -> bool:
        """
        Returns True if registration is successful,
        False if the username already exists.
        """
        if self.user_exists(username):
            return False
        else:
            self.save_user(username, password)
            return True

    def verify_login(self, username: str, password: str) -> bool:
        """
        Checks if the username exists and whether the hashed password matches.
        """
        hashed_input = self.hash_password(password)
        users = self.load_users()
        for u, hashed_pass in users:
            if u == username and hashed_pass == hashed_input:
                return True
        return False

    def display_users(self):
        """
        Displays all users and their hashed passwords.
        """
        users = self.load_users()
        if users:
            for username, hashed_password in users:
                print(f"Username: {username}, Hashed password: {hashed_password}")
        else:
            print("No user information available.")
