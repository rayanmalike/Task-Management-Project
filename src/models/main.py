from user_manager import UserManager
def main():
    manager = UserManager('users.csv')
    while True:
        print("\n=== User Management ===")
        print("1. Register")
        print("2. Login")
        print("3. Reset Password")
        print("4. Display All Users")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1': #Register
            user = input("Enter new username: ")
            password = input("Enter new password: ")
            manager.register_user(user, password)

        elif choice == '2': #Login
            user = input("Username: ")
            password = input("Password: ")
            if manager.verify_login(user, password):
                print(f"\nWelcome to our Dashboard,  {user} !!!\n")
                
                print("[Main Screen]")
                break
            else:
                print("Invalid credentials.")

        elif choice == '3': #Reset Password
            user = input("Username to reset: ")
            new_pwd = input("Enter new password: ")
            manager.reset_password(user, new_pwd)

        elif choice == '4': #Display All Users
            manager.display_users()

        elif choice == '5': #Exit our Program
            print("Exiting application.")
            break

        else:
            print("Invalid option, please try again.")

main()
