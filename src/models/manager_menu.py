from datetime import datetime
from task import Task
from manager import Manager
def show_manager_menu_task(manager: Manager):
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
                task = Task(input("Enter task title: "),
                            input("Enter task description: "), 
                            datetime(int(input("Enter due date: \nYear: ")), int(input("Month: ")), int(input("Day: "))), 
                            int(input("Enter assigned user ID: ")), 
                            manager.get_user_id())
                task.set_id(id)
                task.set_priority(input("Enter priority (LOW/MEDIUM/HIGH): ").upper())
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
            priority = input("Enter updated priority [LOW/MEDIUM/HIGH]: ").upper()
            try:
                task_manager.change_task_priority(task_id, priority)
            except Exception as e:
                print(str(e))

        elif choice == '5':
            task_id = input("Enter task ID to track status: ")
            try:
                task = task_manager.get_task_by_id(task_id)
                print(f"Current status for task [{task_id}]: {task.get_status()}")
            except Exception as e:
                print(str(e))

        elif choice == '6':
            task_id = input("Enter task ID to change assigned user: ")
            try:
                task = task_manager.get_task_by_id(task_id)
                task.set_assigned_user(input("Enter new assigned user ID: "))
                task_manager._save_tasks_to_csv()
                print(f"Changed task {task_id} assigned user ID successfully.")
            except Exception as e:
                print(str(e))


        elif choice == '7':
            task_id = input("Enter task ID to add comment: ")
            try:
                task = task_manager.get_task_by_id(task_id)
                task_manager.view_task_comments(task)
                task_manager.add_comment_to_task(task, manager, input("Enter comment for task: "))
            except Exception as e:
                print(str(e))

        elif choice == '8':
            task_manager.list_tasks()

        elif choice == '9':
            print("Returning to main menu...")
            return False

        else:
            print("Invalid option. Please try again.")

def show_manager_menu_project(manager: Manager): #TODO: implement project menu
    pass