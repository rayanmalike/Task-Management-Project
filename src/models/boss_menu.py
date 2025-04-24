from user_controller import UserController
def show_boss_menu(username, manager): # -> "username" parameter used to identify whether it's a boss, manager, or employee based on their "role".
    while True:
        print("""
====== BOSS DASHBOARD ======
1. Display all users
2. Add new Account
3. Reset Password for Manager
4. Reset Password for Employee
5. Update User Info
6. Delete User
7. Promote/Demote Role
8. Logout
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
            print("\n=== Update User Information ===")
            username = input("Enter username to update: ")
            if manager.user_exists(username):
                new_username = input("Enter new username (or press Enter to skip): ")
                new_email = input("Enter new email (or press Enter to skip): ")
                
                # Only pass values that were actually entered
                if new_username or new_email:
                    manager.update_user_info(
                        username,
                        new_email if new_email else None,
                        new_username if new_username else None
                    )
                else:
                    print("No changes made.")
            else:
                print(f"User '{username}' not found.")

        elif choice == '6':
            username = input("Username to delete: ")
            confirm = input(f"Are you sure you want to delete '{username}'? (yes/no): ")
            if confirm.lower() == 'yes':
                manager.delete_user(username)
                
            else:
                print("Cancelled.")

        elif choice == '7':
            username = input("Username to promote/demote: ")
            new_role = input("New role (boss/manager/employee): ")
            manager.update_role(username, new_role)

        elif choice == '8':
            print("Logging out...")
            break

        else:
            print("Invalid option.")
