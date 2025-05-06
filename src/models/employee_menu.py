from task import *
from task_controller import TaskManager
from project_controller import ProjectManager

def show_employee_menu(employee):
    """
    Displays the Employee Dashboard Menu.

    Allows employee to:
    -View their assigned tasks
    -Track status of a task
    -Submit tasks as completed
    -Add comments to tasks
    -View all comments on their assigned tasks
    -View details of a specific project
    -Logout and return to the main menu

    Args:
        employee(Employee): The employee object currently logged in.
    """
    task_manager = TaskManager.get_instance()
    project_manager = ProjectManager.get_instance()

    while True:
        print(f"""
------> Employee DASHBOARD <------
Welcome, {employee.get_username()}!

1. View My Tasks
2. Track Task Status
3. Submit Task Completion
4. Add Task Comment
5. View Task Comments
6. View Project Details
7. Logout
""")
        choice = input("Select an option: ")

        if choice == '1':
            employee.display_tasks()

        elif choice == '2':
            task_id = input("Enter task ID to track status: ")
            try:
                task = task_manager.get_task_by_id(task_id)
                if task:
                    print(f"Current status for task [{task_id}]: {task.get_status()}")
                else:
                    print("Task not found")
            except Exception as e:
                print(str(e))

        elif choice == '3':
            task_id = input("Enter task ID to submit: ")
            task = task_manager.get_task_by_id(task_id)
            if task:
                task_manager.mark_task_as_completed(task)
            else:
                print("Error submitting task")

        elif choice == '4':
            task_id = input("Enter task ID to add comment: ")
            comment = input("Enter your comment: ")
            if task_manager.add_comment(task_id, employee.get_user_id(), comment):
                print("Comment added successfully")
            else:
                print("Failed to add comment")
        
        elif choice == '5':
            print("\n=== Task Comments ===")
            tasks = task_manager.get_user_assigned_tasks(employee.get_user_id()) 
            if not tasks:
                print("No tasks assigned.")
                continue

            print("\nDisplaying comments for your tasks:")
            for task in tasks:
                task_id = task.get_id()
                comments = task_manager.get_task_comments(task_id)  
                if comments:
                    print (f"Task {task_id}")
                    for comment in comments:
                        print(f"[{comment.timestamp}] User {comment.user_id}: {comment.comment}")
                    print("-" * 50)
                # else:
                #     print("No comments to display for this task.")
                # print("-" * 50)


        elif choice == '6':
            project_id = input("Enter Project ID to view: ")
            project = project_manager.get_project_by_id(project_id)
            if project:
                print("\nProject Details:")
                print(f"ID: {project.get_id()}")
                print(f"Title: {project.get_title()}")
                print(f"Description: {project.get_description()}")
                print(f"Due Date: {project.get_due_date()}")
                print(f"\nTasks in Project:")
                tasks = project.get_assigned_tasks()
                if tasks:
                    for task_id, task in tasks.items():
                        print(f"\nTask ID: {task.get_id()}")
                        print(f"Title: {task.get_title()}")
                        print(f"Status: {task.get_status()}")
                        print(f"Due Date: {task.get_due_date()}")
                else:
                    print("No tasks assigned to this project.")
            else:
                print("Project not found.")


        elif choice == '7':
            print("Logging out...")
            return False

        else:
            print("Invalid option. Please try again.")
