def show_employee_menu(username):
    while True:
        print(f"""
====== Employee DASHBOARD ======
Welcome, {username}!

1. View Tasks
2. View Project
3. Track Task Status 
4. Submit Task Completion
5. Add Task Comment
6. View Task Comments
7. Logout
""")
        choice = input("Select an option: ")

        if choice == '1':
            pass

        elif choice == '2':
            pass

        elif choice == '3':
            pass

        # elif choice == '4':
        #     print("Logging out...")
        #     break

        # else:
        #     print("Invalid option. Please try again.")