from task_controller import TaskManager
from project_controller import ProjectManager
from user_controller import UserController
from task import Task
from project import Project
from datetime import datetime

def option_task(uc : UserController):
    while True:
        print("""
====== MANAGER TASK DASHBOARD ======

1. Create Task
2. Update Task
3. Delete Task
4. Set Task Priority
5. Track Task Status
6. Add Task Comment
7. Display All Tasks
8. Return to Manager Dashboard
""")
        choice = input("Select an option: ")
        tm = TaskManager.get_instance()

        if choice == '1':
            try:
                id = input("Enter task ID: ")
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date_str = input("Enter due date (YYYY-MM-DD): ")
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                priority = input("Enter priority (LOW/MEDIUM/HIGH): ")
                assigned_user_id = int(input("Enter assigned user ID: "))
                
                assigned_user = uc.get_employee(assigned_user_id)
                if assigned_user:
                    task = Task(title, description, due_date, assigned_user, )
                    task.set_id(id)
                    task.set_priority(priority)
                    tm.create_task(task)
                    tm._save_tasks_to_csv()
                    print("Task created successfully!")
                else:
                    print("User not found!")
            except ValueError as e:
                print(f"Error creating task: {str(e)}")

        elif choice == '2':
            try:
                task_id = input("Enter task ID to update: ")
                task = tm.tasks.get(task_id)
                if task:
                    print("\nLeave blank if no change needed")
                    title = input("Enter new title: ")
                    description = input("Enter new description: ")
                    due_date_str = input("Enter new due date (YYYY-MM-DD): ")
                    priority = input("Enter new priority (LOW/MEDIUM/HIGH): ")
                    assigned_user_id = input("Enter new assigned user ID: ")
                    
                    if title:
                        task.set_title(title)
                    if description:
                        task.set_description(description)
                    if due_date_str:
                        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                        task.set_due_date(due_date)
                    if priority:
                        task.set_priority(priority)
                    if assigned_user_id:
                        new_user = uc.get_employee(int(assigned_user_id))
                        if new_user:
                            task.set_assigned_user(new_user)
                        else:
                            print("Warning: User not found, assignment not updated")
                    
                    print("Task updated successfully!")
                else:
                    print("Task not found!")
            except ValueError as e:
                print(f"Error updating task: {str(e)}")

        elif choice == '3':
            try:
                task_id = input("Enter task ID to delete: ")
                tm.delete_task(task_id)
                print("Task deleted successfully!")
            except ValueError as e:
                print(f"Error deleting task: {str(e)}")

        elif choice == '4':
            try:
                task_id = input("Enter task ID: ")
                priority = input("Enter new priority (LOW/MEDIUM/HIGH): ")
                task = tm.tasks.get(task_id)
                if task:
                    task.set_priority(priority)
                    print("Priority updated successfully!")
                else:
                    print("Task not found!")
            except ValueError as e:
                print(f"Error setting priority: {str(e)}")

        elif choice == '5':
            try:
                task_id = input("Enter task ID: ")
                task = tm.tasks.get(task_id)
                if task:
                    status = task.get_status()
                    print(f"Current status: {status}")
                else:
                    print("Task not found!")
            except ValueError as e:
                print(f"Error tracking status: {str(e)}")

        elif choice == '6':
            try:
                task_id = input("Enter task ID: ")
                comment = input("Enter comment: ")
                task = tm.tasks.get(task_id)
                if task:
                    task.add_comment(None, comment)
                    print("Comment added successfully!")
                else:
                    print("Task not found!")
            except ValueError as e:
                print(f"Error adding comment: {str(e)}")

        elif choice == '7':
            print("\nAll Tasks:")
            for task_id, task in tm.tasks.items():
                print(f"\nTask ID: {task_id}")
                print(f"Title: {task.get_title()}")
                print(f"Description: {task.get_description()}")
                print(f"Due Date: {task.get_due_date()}")
                print(f"Status: {task.get_status()}")
                print(f"Priority: {task.get_priority()}")
                print("-" * 50)

        elif choice == '8':
            break

        else:
            print("Invalid option. Please try again.")


def option_project():
    while True:
        print("""
====== MANAGER PROJECT DASHBOARD ======

1. Create Project
2. Update Project
3. Delete Project
4. Add Tasks to Project
5. Display all Projects
6. Return to Manager Dashboard
""")
        choice = input("Select an option: ")
        pm = ProjectManager.get_instance()

        if choice == '1':
            pass

        elif choice == '2':
            pass

        elif choice == '6':
            break

        else:
            print("Invalid option. Please try again.")

def show_manager_menu(username):
    while True:
        print(f"[Manager Menu for {username}]") # -> "username" parameter used to identify whether it's a boss, manager, or employee based on their "role".
        print("""
====== MANAGER DASHBOARD ======
              
1. Create/ Update/ Delete Task
2. Create/ Update/ Delete Project
3. Log out
""")
        choice = input("Select an option: ")
        uc = UserController.get_instance()
        # TODO: need to make a variable to store manager object -> 

        if choice == '1':
            option_task(uc)

        elif choice == '2':
            option_project(uc)

        elif choice == '3':
            print("Logging out...")
            break

        else:
            print("Invalid option. Please try again.")


