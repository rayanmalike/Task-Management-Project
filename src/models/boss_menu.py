from user_controller import UserController
def show_boss_menu(username, manager): # -> "username" parameter used to identify whether it's a boss, manager, or employee based on their "role".
    """
    Displays the Boss Dashboard menu which allows a boss to manage each user.

    The boss can:
    -View all users
    -Add new user accounts
    -Reset passwords
    -Update user info
    -Delete users
    -Promote or demote users
    -Log off

    Args:
        username(str): The username of the currently logged-in boss.
        manager(object): The user management system instance that handles user actions like register, delete, or update.
    """
    while True:
        print("""
======> BOSS DASHBOARD <======
1. Display all users
2. Add new Account
3. Reset Password for Manager
4. Reset Password for Employee
5. Promote/Demote Role
6. Reset Password for Boss
7. Delete User
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
            role = "manager"
            while True:
                username = input("Username to reset Manager password: ")
                user = manager.get_user_by_username(username)
                if not user:
                    print("-> Username not found!")
                    continue
                if user["role"] != role:
                    print(f"-> '{username}' is not a Manager (it's a '{user['role']}').")
                    continue
                input_id = input("User ID to reset password: ")
                id_belongs_to = None
                for uname, info in manager.users_dict.items():
                    if info["id"] == input_id:
                        id_belongs_to = uname
                        break
                if not id_belongs_to:
                    print("-> ID not found in the system.")
                    continue
                if user["id"] != input_id:
                    actual_owner = id_belongs_to
                    actual_role = manager.users_dict[actual_owner]["role"]
                    print(
                        f"-> ID '{input_id}' belongs to '{actual_owner}' (a '{actual_role}'). It does not match username '{username}'!")
                    continue
                break
            new_password = input("New password: ")
            manager.reset_password(username, new_password)
            uc.update_password(input_id, new_password, False)
            print(f"-> Password for manager '{username}' has been reset.")





        elif choice == '4':

            role = "employee"

            while True:
                username = input("Username to reset Employee password: ")
                user = manager.get_user_by_username(username)

                if not user:
                    print("-> Username not found!")
                    continue

                if user["role"] != role:
                    print(f"-> '{username}' is not an Employee (it's a '{user['role']}').")
                    continue

                input_id = input("User ID to reset password: ")
                id_belongs_to = None
                for uname, info in manager.users_dict.items():
                    if info["id"] == input_id:
                        id_belongs_to = uname
                        break
                if not id_belongs_to:
                    print("-> ID not found in the system.")
                    continue
                if user["id"] != input_id:
                    actual_owner = id_belongs_to
                    actual_role = manager.users_dict[actual_owner]["role"]
                    print(
                        f"-> ID '{input_id}' belongs to '{actual_owner}' (a '{actual_role}'). It does not match username '{username}'!")
                    continue
                break

            new_password = input("New password: ")
            manager.reset_password(username, new_password)
            uc.update_password(input_id, new_password, False)
            print(f"-> Password for employee '{username}' has been reset.")





        elif choice == '5':
            while True:
                username = input("Username to promote/demote: ")
                user = manager.get_user_by_username(username)
                if not user:
                    print("-> Username not found!")
                    continue
                input_id = input("User ID to confirm identity: ")
                id_belongs_to = None
                for uname, info in manager.users_dict.items():
                    if info['id'] == input_id:
                        id_belongs_to = uname
                        break
                if not id_belongs_to:
                    print("-> ID not found in the system.")
                    continue
                if user["id"] != input_id:
                    actual_owner = id_belongs_to
                    actual_role = manager.users_dict[actual_owner]["role"]
                    print(
                        f"-> ID '{input_id}' belongs to '{actual_owner}' (a '{actual_role}'). It does not match username '{username}'!")
                    continue
                break

            new_role = input("New role (boss/manager/employee): ")
            manager.update_role(username, new_role)


        elif choice == '6':
            role = "boss"
            while True:
                username = input("Username to reset Boss password: ")
                user = manager.get_user_by_username(username)

                if not user:
                    print("-> Username not found!")
                    continue

                if user["role"] != role:
                    print(f"-> '{username}' is not a Boss (it's a '{user['role']}').")
                    continue

                id = input("User ID to reset password: ")
                if user["id"] != id:
                    print("-> ID does not match this username!")
                    continue

                break

            new_password = input("New password: ")
            manager.reset_password(username, new_password)
            uc.update_password(id, new_password, False)
            print(f"-> Password for boss '{username}' has been reset.")


        elif choice == '7':
            while True:
                username = input("Username to delete: ")
                user = manager.get_user_by_username(username)
                if not user:
                    print("-> Username not found!")
                    continue
                id = input("User ID to delete: ")
                if user["id"] != id:
                    matched_user = None
                    for uname, udata in manager.users_dict.items():
                        if udata["id"] == id:
                            matched_user = uname
                            break
                    if matched_user:
                        print(f"-> ID '{id}' belongs to '{matched_user}' (not '{username}').")
                    else:
                        print("-> ID does not match this username!")
                    continue
                break

            confirm = input(f"Are you sure you want to delete '{username}'? (yes/no): ")
            if confirm.lower() == 'yes':
                role = manager.get_user_role(username)
                if role == 'manager':
                    uc.delete_manager(id)
                elif role == 'employee':
                    uc.delete_employee(id)
                manager.delete_user(username)
                print(f"-> User '{username}' and associated data deleted successfully.")
            else:
                print("-> Delete operation cancelled.")



        elif choice == '8':
            print("Logging out...")
            break

        else:
            print("Invalid option.")