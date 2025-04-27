from datetime import datetime
from task import Task
from project import Project
from manager import Manager
from task_controller import TaskManager

def show_manager_menu_task(manager: Manager):
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
    from project_controller import ProjectManager
    pm = ProjectManager.get_instance()
    tm = TaskManager.get_instance()
    while True:
            print(f"""
====== MANAGER DASHBOARD ======
Welcome, {manager.get_username()}!

1. Create Project
2. Update Project Info
3. Delete Project
4. Add Task to Project
5. Remove Task from Project
6. View Project
7. Display all Projects
8. Return to Main Menu

    """)
            choice = input("Select an option: ")

            if choice == '1':
                try:
                    id = input("Enter Project ID: ")
                    project = Project(input("Enter Project Title: "),
                                    input("Enter Project Description: "),
                                    datetime(int(input("Enter due date: \nYear: ")), int(input("Month: ")), int(input("Day: "))),
                                    manager.get_user_id())
                    project.set_id(id)
                    pm.create_project(project)
                    pm._save_project_to_file()
                    print("Project created successfully.")
                except Exception as e:
                    print(str(e))

            elif choice == '2':
                proj_id = input("Enter Project ID to update: ")
                project = pm.get_project_by_id(proj_id)
                if project:
                    print("Current Project Info: ")
                    print(f"Title: {project.get_title()}")
                    print(f"Description: {project.get_description()}")
                    print(f"Due Date: {project.get_due_date()}")
                    
                    pm.update_project(project)
                else:
                    print("Project not found")

            elif choice == '3':
                proj_id = input("Enter Project ID to deleted: ")
                project = pm.get_project_by_id(proj_id)
                if project:
                    ans = input(f"Are you sure you want to delete project {proj_id}? [Y/N]: ").upper()
                    if ans == 'Y':
                        try:
                            pm.delete_project(project)
                        except Exception as e:
                            print(str(e))
                    else:
                        print("Cancelled deleting task.")
                        continue
                else:
                    print("Project not found")

            elif choice == '4':
                proj_id = input("Enter Project ID to add Tasks: ")
                project = pm.get_project_by_id(proj_id)
                if project:
                    task_id = input("Enter Task ID: ")
                    task = tm.get_task_by_id(task_id)
                    if task:
                        try:
                            pm.add_task_to_project(project, task)
                        except Exception as e:
                            print(str(e))
                    else:
                        print("Task not found")

            elif choice == '5':
                proj_id = input("Enter Project ID to remove Tasks: ")
                project = pm.get_project_by_id(proj_id)
                if project:
                    task_id = input("Enter Task ID to remove: ")
                    task = tm.get_task_by_id(task_id)
                    if task:
                        try:
                            pm.delete_task_from_project(project, task)
                        except Exception as e:
                            print(str(e))
                    else:
                        print("Task not found")

            elif choice == '6':
                project_id = input("Enter Project ID to view: ")
                project = pm.get_project_by_id(project_id)
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
                print("\nAll Projects:")
                projects = pm.get_all_projects()
                if projects:
                    for project in projects:
                        print(f"\nProject ID: {project.get_id()}")
                        print(f"Title: {project.get_title()}")
                        print(f"Description: {project.get_description()}")
                        print(f"Due Date: {project.get_due_date()}")
                        print("Tasks:", len(project.get_assigned_tasks()))
                        print("-" * 30)
                else:
                    print("No projects found.")

            elif choice == '8':
                print("Returning to main menu...")
                return False
            
            else:
                print("Invalid option. Please try again.")