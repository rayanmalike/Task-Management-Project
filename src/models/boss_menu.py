def show_boss_menu(username, manager): # -> "username" parameter used to identify whether it's a boss, manager, or employee based on their "role".
    while True:
        print("""
====== BOSS DASHBOARD ======
1. Display all users
2. Add new Account
3. Reset Password for users
4. Delete User
5. Promote/Demote Role
6. Display all Projects/Task -> Missing (need to fill in)
7. Assign specific Project/Task -> Missing (need to fill in)
8. Logout
""")

        choice = input("Select an option: ")
        if choice == '1':
            manager.display_users()

        elif choice == '2':
            username = input("Enter new user's Username: ")
            password = input("Enter new user's Password: ")
            email = input("Enter new user's Email")

            while True:
                role = input("Enter new user's Role (manager/employee): ").lower()
                if role in ['manager', 'employee']:
                    break  # Nhập đúng, thoát khỏi vòng lặp
                else:
                    print("Invalid role. Please enter 'manager' or 'employee' only.")

            id = input("Enter new user's ID: ")
            manager.register_user(username, password, role, email, id)

        elif choice == '3':
            username = input("Username to reset password: ")
            new_password = input("New password: ")
            manager.reset_password(username, new_password)

        elif choice == '4':
            username = input("Username to delete: ")
            confirm = input(f"Are you sure you want to delete '{username}'? (yes/no): ")
            if confirm.lower() == 'yes':
                manager.delete_user(username)
            else:
                print("Cancelled.")

        elif choice == '5':
            username = input("Username to promote/demote: ")
            new_role = input("New role (boss/manager/employee): ")
            manager.update_role(username, new_role)

        elif choice == '6':
            print("[Placeholder] Display all tasks") # -> Need to be filled in

        elif choice == '7':
            print("[Placeholder] Assign tasks") # - > Need to be filled in

        elif choice == '8':
            print("Logging out...")
            break

        else:
            print("Invalid option.")
