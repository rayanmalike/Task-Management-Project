from user_manager_dict import UserManager

def main():
    def clear_screen():
        print("\n" * 10)  # os.system('cls' if os.name == 'nt' else 'clear')

    def RunSystem():
        print("---[Main Screen]---")


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
                clear_screen()
                print(f"\nWelcome to our Dashboard,  {user} !!!\n")
                RunSystem() # -> Run system after successfully logging in. 
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
