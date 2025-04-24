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
        with open(self.filename, 'w', encoding='utf-8') as file:
            for u, data in self.users_dict.items():
                line = f"{u},{data['password']},{data['role']},{data['email']},{data['id']}\n"
                file.write(line)

    def save_user(self, username, password, role, email, user_id):
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
        return username in self.users_dict

    def register_user(self, username: str, password: str, role: str, email: str, user_id: str) -> bool:
        if self.user_exists(username):
            return False
        self.save_user(username, password, role, email,  user_id)
        return True

    def verify_login(self, username: str, password: str) -> bool:
        user = self.users_dict.get(username)
        if not user:
            return False
        hashed_input = self.hash_password(password)
        return user["password"] == hashed_input

    def delete_user(self, user_id: int) -> bool:
        if user_id in self.users_dict:
            del self.users_dict[user_id]
            self._write_all_users_to_file()
            print(f"-> User with ID '{user_id}' has been deleted successfully!")
            return True
        else:
            print(f"User with ID '{user_id}' not found. Unable to delete!")
            return False

    def get_user_role(self, username: str) -> str:
        user = self.users_dict.get(username)
        return user["role"] if user else None

    def reset_password(self, username: str, new_password: str) -> bool:
        if not self.user_exists(username):
            print(f"Username '{username}' not found. Password reset failed.")
            return False

        new_hashed = self.hash_password(new_password)
        self.users_dict[username]["password"] = new_hashed
        self._write_all_users_to_file()
        print(f"Password for '{username}' has been reset successfully.")
        return True

    def display_users(self):
        if self.users_dict:
            for index, (username, data) in enumerate(self.users_dict.items(), start=1):
                print(
                    f"User {index}: {username} --- Password: {data['password']}  ---  Role: {data['role']} --- Email: {data['email']} --- ID: {data['id']}")
        else:
            print("No user information available.")

    def update_role(self, username: str, new_role: str) -> bool:
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

