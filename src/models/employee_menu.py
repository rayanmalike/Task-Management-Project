def show_employee_menu(username):
    while True:
        print(f"""
====== Employee DASHBOARD ======
Welcome, {username}!

1. [Coming soon...]
2. [Coming soon...]
3. [Coming soon...]
4. Logout
""")
        choice = input("Select an option: ")

        if choice == '1':
            pass

        elif choice == '2':
            pass

        elif choice == '3':
            pass

        elif choice == '4':
            print("Logging out...")
            break

        else:
            print("Invalid option. Please try again.")
