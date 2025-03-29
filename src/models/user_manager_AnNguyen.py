import hashlib

class UserManager:
    def __init__(self, filename):
        self.filename = filename

    def hash_password(self, password):  # Hash password using SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def save_user(self, username, password):  # Save user information to file
        hashed_password = self.hash_password(password)
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"{username},{hashed_password}\n")
        print(f"User information for '{username}' has been saved to the file.")

    def load_users(self):  # Read all user information from file and return as a list
        users = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    username, hashed_password = line.strip().split(',')
                    users.append((username, hashed_password))
        except FileNotFoundError:
            print("File does not exist.")
        return users

    def display_users(self):  # Display all users and their hashed passwords
        users = self.load_users()
        if users:
            for username, hashed_password in users:
                print(f"Username: {username}, Hashed password: {hashed_password}")
        else:
            print("No user information available.")
