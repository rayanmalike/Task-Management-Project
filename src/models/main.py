from user_manager_dict import UserManager
from boss_menu import show_boss_menu
from manager_menu import *
from employee_menu import show_employee_menu
from user_controller import UserController
from employee import Employee

def clear_screen():
    print("\n" * 10)  

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
                # --------------------
                if role == "boss":
                    show_boss_menu(username, manager)  # Show menu for BOSS if account logging in identied as "BOSS".


                # --------------------
                elif role == "manager":
                    user_controller = UserController.get_instance()
                    current_user = user_controller.get_manager_by_username(username)
                    if not current_user or current_user.get_role().lower() != "manager":
                        print("Error: Invalid user or insufficient permissions")
                        return
                    while True:
                        choice = input(
""" \n======= MAIN MENU FOR MANAGER ========

1. Create/update/delete Tasks 
2. Create/update/delete Projects 
3. Logout
Enter choice: """)
                        if choice == '1': 
                            if show_manager_menu_task(current_user) == False:
                                continue  
                        elif choice == '2' : 
                            if show_manager_menu_project(current_user) == False:
                                continue
                        elif choice == '3':
                            print("Logging out...") 
                            break
                        else: 
                            print("Invalid option. Try again.")
                            choice = input(
""" \n======= MAIN MENU FOR MANAGER ========

1. Create/update/delete Tasks 
2. Create/update/delete Projects 
3. Logout
Enter choice: """)
                            return
                        
                # --------------------
                elif role == "employee":
                    user_controller = UserController.get_instance()
                    current_user = user_controller.get_employee_by_username(username)
                    if not current_user or current_user.get_role().lower() != "employee":
                        print("Error: Invalid user")
                        return
                    show_employee_menu(current_user)  
                        
                break
            else:
                print("Invalid credentials.")

        elif choice == '2': #Exit Program.
            print("Exiting application, see you again!")
            break

        else:
            print("Invalid option, please try again.")

main()
