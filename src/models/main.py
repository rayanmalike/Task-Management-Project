from user_manager_dict import UserManager
from boss_menu import show_boss_menu
from manager_menu import show_manager_menu
from employee_menu import show_employee_menu


def clear_screen():
    print("\n" * 10)  # Simulate clearing screen

def main():
    manager = UserManager('users.csv')

    if not manager.users_dict:
    # Boss is allowed to create account first when program is first used (meaning he owned it).
    # After Boss created his own account, then he can register and create new account for the Manager and Employee.
        print("No users found. Please create the first Boss account.")
        username = input("Enter boss username: ")
        password = input("Enter boss password: ")
        email = input("Enter boss email: ")
        user_id = input("Enter boss ID: ")
        manager.register_user(username, password, role="boss", email=email, user_id=user_id)

    while True: #Main for Login after Boss created his account.
        print("\n=== User Management ===")
        print("1. Login")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1': #Log in
            username = input("Username: ")
            password = input("Password: ")
            if manager.verify_login(username, password):
                clear_screen()
                print(f"\nWelcome to our Dashboard,  {username} !!!\n")
                role = manager.get_user_role(username)

                if role == "boss":
                    show_boss_menu(username, manager)  # Show menu for BOSS if account logging in identied as "BOSS".

                elif role == "manager":
                    show_manager_menu(username)  # Show Manager's menu if account logging in identied as "Manager".

                elif role == "employee":
                    show_employee_menu(username)  ##Show Employee's menu if account logging in identied as "Manager".
                break
            else:
                print("Invalid credentials.")

        elif choice == '2': #Exit Program.
            print("Exiting application, see you again!")
            break

        else:
            print("Invalid option, please try again.")

main()
