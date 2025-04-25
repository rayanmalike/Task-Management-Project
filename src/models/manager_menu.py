from datetime import datetime
from task import Task
from manager import Manager
def show_manager_menu(manager: Manager):
    from user_controller import UserController
    from task_controller import TaskManager
    
    # Get user instance
    user_controller = UserController.get_instance()
    task_manager = TaskManager.get_instance()

    while True:
        print(f"""
====== MANAGER DASHBOARD ======
Welcome, {manager.get_username()}!

1. Create Task
2. Update Task Info
3. Delete Task
4. Set Task Priority
5. Track Task Status
6. Change Assigned User
7. Add Task Comment
8. Display All Tasks
9. Return to Main Menu
""")
        choice = input("Select an option: ")

        if choice == '1':
            try:
                id = input("Enter task ID: ")
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                print("Enter due date:")
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
                due_date = datetime(year, month, day)
                priority = input("Enter priority (LOW/MEDIUM/HIGH): ").upper()
                assigned_user_id = int(input("Enter assigned user ID: "))
                
                task = Task(title, description, due_date, assigned_user_id, manager.get_user_id())
                task.set_id(id)
                task.set_priority(priority)
                task_manager.create_task(task)
                task_manager._save_tasks_to_csv()
                print("Task created successfully!")
            except Exception as e:
                print(f"Error creating task: {str(e)}")

        elif choice == '2':
            task_id = input("Enter task ID to update: ")
            task = task_manager.get_task_by_id(task_id)
            if task:
                print("\nCurrent task details:")
                print(f"Title: {task.get_title()}")
                print(f"Description: {task.get_description()}")
                print(f"Due Date: {task.get_due_date()}")
                print(f"Assigned User Id: {task.get_assigned_user()}")
                print(f"Priority: {task.get_priority()}")
                print(f"Status: {task.get_status()}")
                
                task_manager.update_task(task)

        elif choice == '3':
            task_id = input("Enter task ID to delete: ")
            ans = input(f"Are you sure you want to delete task {task_id}? [Y/N]: ").upper()
            if ans =='Y':
                try:
                    task_manager.delete_task(task_id)
                except Exception as e:
                    print(str(e))
            else : 
                print(f"Cancelled deleting task {task_id}.")
                continue

        elif choice == '4':
            task_id = input("Enter task ID to update priority: ")
            priority =input("Enter updated priority [LOW/MEDIUM/HIGH]: ").upper()
            try:
                task_manager.change_task_priority(task_id, priority)
            except Exception as e:
                print(str(e))

        elif choice == '5':
            pass

        elif choice == '6':
            pass

        elif choice == '7':
            pass

        elif choice == '8':
            pass

        elif choice == '9':
            print("Returning to main menu...")
            return

        else:
            print("Invalid option. Please try again.")