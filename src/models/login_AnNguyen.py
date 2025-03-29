import hashlib
import json
from typing import Dict

# File name to store the users database
DB_FILE = "users_db.txt"


# Load users from file (if exists) or return an empty dict
def load_users() -> Dict[str, str]:
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}


# Save the users database to file
def save_users(users: Dict[str, str]):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)


# Simulate the user database from file
users_db: Dict[str, str] = load_users()


# Password hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Register account
def register(username, password):
    if username in users_db:
        print("Username has been used!")
    else:
        hashed_password = hash_password(password)
        users_db[username] = hashed_password
        save_users(users_db)  # Save the database after registration
        print("Register Successfully!")


# Login
def login(username, password):
    hashed_password = hash_password(password)
    if username in users_db and users_db[username] == hashed_password:
        return True  # Use True instead of true
    else:
        return False  # Use False instead of false


# Function to clear the console screen
def clear_screen():
    print("\n" * 10)
    # os.system('cls' if os.name == 'nt' else 'clear')


# Other functions (e.g., display dashboard)
def RunSystem():
    print("Welcome to Dashboard!")


# Run the clear_screen program
while True:
    clear_screen()
    action = input("(r): register \n(l): login \n(v): view users \n(q): quit \nYour choice: ").lower()
    if action == 'q':
        break
    elif action == 'r':
        username = input("Insert Username: ")
        password = input("Insert Password: ")
        register(username, password)
    elif action == 'v':
        print("------ User List -------")
        print(users_db)
        print("------------------------")
    elif action == 'l':
        username = input("Insert Username: ")
        password = input("Insert Password: ")
        if login(username, password):
            RunSystem()
        else:
            print("Wrong Username or Password!")
    else:
        print("Invalid Choice!")
