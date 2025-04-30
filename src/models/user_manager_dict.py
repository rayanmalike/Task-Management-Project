import hashlib

class UserManager:
    """
    UserManager handles user registration, authentication,
    password management, and user data persistence to a file.
    """

    def __init__(self, filename):
        """
        Initializes the UserManager instance.

        Args:
            filename (str): Path to the user data file.
        """
        self.filename = filename
        self.users_dict = {}
        self.load_users()

    def hash_password(self, password):
        """
        Hashes a plain-text password using SHA-256.

        Args:
            password (str): The plain-text password.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def load_users(self):
        """
        Loads users from the file into memory (self.users_dict).
        """
        self.users_dict.clear()
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        if len(parts) == 5:
                            username, hashed_password, role, email, user_id = parts
                            self.users_dict[username] = {
                                "password": hashed_password,
                                "role": role,
                                "email": email,
                                "id": user_id
                            }
        except FileNotFoundError:
            print("File does not exist.")

    def _write_all_users_to_file(self):
        """
        Writes all users currently in memory back to the file.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            for u, data in self.users_dict.items():
                line = f"{u},{data['password']},{data['role']},{data['email']},{data['id']}\n"
                file.write(line)

    def save_user(self, username, password, role, email, user_id):
        """
        Saves a new user to memory and updates the file.

        Args:
            username (str): Username.
            password (str): Plain-text password.
            role (str): User role.
            email (str): User email address.
            user_id (str): User ID.
        """
        hashed_password = self.hash_password(password)
        self.users_dict[username] = {
            "password": hashed_password,
            "role": role,
            "email": email,
            "id": user_id
        }
        self._write_all_users_to_file()
        print(f"User '{username}' with role '{role}' saved to file.")

    def user_exists(self, username: str) -> bool:
        """
        Checks if a username already exists.

        Args:
            username (str): Username to check.

        Returns:
            bool: True if user exists, False otherwise.
        """
        return username in self.users_dict

    def register_user(self, username: str, password: str, role: str, email: str, user_id: str) -> bool:
        """
        Registers a new user if the username does not already exist.

        Args:
            username (str): Username.
            password (str): Plain-text password.
            role (str): User role.
            email (str): User email.
            user_id (str): User ID.

        Returns:
            bool: True if registration successful, False if username already exists.
        """
        if self.user_exists(username):
            return False
        self.save_user(username, password, role, email, user_id)
        return True

    def verify_login(self, username: str, password: str) -> bool:
        """
        Verifies user credentials during login.

        Args:
            username (str): Username.
            password (str): Plain-text password.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        user = self.users_dict.get(username)
        if not user:
            return False
        hashed_input = self.hash_password(password)
        return user["password"] == hashed_input

    def delete_user(self, user_id: int) -> bool:
        """
        Deletes a user by ID and updates the file.

        Args:
            user_id (int): User ID.

        Returns:
            bool: True if deletion successful, False otherwise.
        """
        if user_id in self.users_dict:
            del self.users_dict[user_id]
            self._write_all_users_to_file()
            print(f"-> User with ID '{user_id}' has been deleted successfully!")
            return True
        else:
            print(f"User with ID '{user_id}' not found. Unable to delete!")
            return False

    def get_user_role(self, username: str) -> str:
        """
        Retrieves the role of a user.

        Args:
            username (str): Username.

        Returns:
            str: Role if user exists, None otherwise.
        """
        user = self.users_dict.get(username)
        return user["role"] if user else None

    def reset_password(self, username: str, new_password: str) -> bool:
        """
        Resets a user's password.

        Args:
            username (str): Username.
            new_password (str): New plain-text password.

        Returns:
            bool: True if reset successful, False otherwise.
        """
        if not self.user_exists(username):
            print(f"Username '{username}' not found. Password reset failed.")
            return False

        new_hashed = self.hash_password(new_password)
        self.users_dict[username]["password"] = new_hashed
        self._write_all_users_to_file()
        print(f"Password for '{username}' has been reset successfully.")
        return True

    def display_users(self):
        """
        Displays all users currently loaded in memory.
        """
        if self.users_dict:
            for index, (username, data) in enumerate(self.users_dict.items(), start=1):
                print(
                    f"User {index}: {username} ---  Role: {data['role']} --- Email: {data['email']} --- ID: {data['id']}")
        else:
            print("No user information available.")

    def update_role(self, username: str, new_role: str) -> bool:
        """
        Updates the role of a user.

        Args:
            username (str): Username.
            new_role (str): New role to assign ('boss', 'manager', 'employee').

        Returns:
            bool: True if update successful, False otherwise.
        """
        if username not in self.users_dict:
            print(f"User '{username}' not found.")
            return False

        if new_role not in ['boss', 'manager', 'employee']:
            print("Invalid role. Role must be 'boss', 'manager', or 'employee'.")
            return False

        self.users_dict[username]['role'] = new_role
        self._write_all_users_to_file()
        print(f"User '{username}' role updated to '{new_role}'.")
        return True

    def update_user_info(self, username: str, new_email: str = None, new_username: str = None) -> bool:
        """
        Updates a user's email and/or username.

        Args:
            username (str): Current username.
            new_email (str, optional): New email address.
            new_username (str, optional): New username.

        Returns:
            bool: True if update successful, False otherwise.
        """
        if username not in self.users_dict:
            print(f"User '{username}' not found.")
            return False

        user_data = self.users_dict[username]

        if new_email:
            user_data['email'] = new_email

        if new_username and new_username != username:
            if new_username in self.users_dict:
                print(f"Username '{new_username}' already exists.")
                return False
            self.users_dict[new_username] = user_data
            del self.users_dict[username]

        self._write_all_users_to_file()
        print(f"User information updated successfully.")
        return True
