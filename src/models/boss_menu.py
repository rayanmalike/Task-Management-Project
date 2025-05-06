from user_controller import UserController
def show_boss_menu(username, manager): # -> "username" parameter used to identify whether it's a boss, manager, or employee based on their "role".
    """
    Displays the Boss Dashboard menu which allows a boss to manage each user.

    The boss can:
    -View all users
    -Add new user accounts
    -Reset passwords
    -Delete users
    -Promote or demote users
    -Log off

    Args:
        username(str): The username of the currently logged-in boss.
        manager(object): The user management system instance that handles user actions like register, delete, or update.
    """
    while True:
        print("""
------> BOSS DASHBOARD <------
1. Display all users
2. Add new Account
3. Reset Password for Manager
4. Reset Password for Employee
5. Promote/Demote Role
6. Delete User
7. Logout
""")
        uc = UserController.get_instance() # Create the User Controller object
        choice = input("Select an option: ")
        if choice == '1':
            manager.display_users()

        elif choice == '2':
            username = input("Enter new user's Username: ")
            password = input("Enter new user's Password: ")
            email = input("Enter new user's Email: ")
            
            while True:
                role = input("Enter new user's Role (manager/employee): ").lower()
                if role in ['manager', 'employee']:
                    break  
                else:
                    print("Invalid role. Please enter 'manager' or 'employee' only.")

            id = input("Enter new user's ID: ")
            manager.register_user(username, password, role, email, id)
            if (role == 'manager'):
                uc.create_manager(id, username, email, password)
            elif (role == 'employee'):
                uc.create_employee(id, username, email, password)

        elif choice == '3':
            username = input("Username to reset password: ")
            id = input("User ID to reset password: ")
            new_password = input("New password: ")
            manager.reset_password(username, new_password)
            uc.update_password(id, new_password, True)
            
        elif choice == '4':
            username = input("Username to reset password: ")
            id = input("User ID to reset password: ")
            new_password = input("New password: ")
            manager.reset_password(username, new_password)
            uc.update_password(id, new_password, False)

        elif choice == '5':
            username = input("Username to promote/demote: ")
            new_role = input("New role (boss/manager/employee): ")
            manager.update_role(username, new_role)

        elif choice == '6':
            username = input("Username to delete: ")
            id = input("User ID to delete: ")
            confirm = input(f"Are you sure you want to delete '{username}'? (yes/no): ")
            if confirm.lower() == 'yes':
                role = manager.get_user_role(username)
                if role == 'manager':
                    uc.delete_manager(id)
                elif role == 'employee':
                    uc.delete_employee(id)
                manager.delete_user(username)
                print(f"User '{username}' and associated data deleted successfully.")
            else:
                print("Delete operation cancelled.")


        elif choice == '7':
            print("Logging out...")
            break

        else:
            print("Invalid option.")
