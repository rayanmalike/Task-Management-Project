from project import Project
from task import Task
import csv
from datetime import datetime
# from user import User # to be deleted

class ProjectManager:
    _instance = None

    def __init__(self):
        if ProjectManager._instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            ProjectManager._instance = self
            self.projects = {}
    
    @staticmethod
    def get_instance():
        if ProjectManager._instance is None:
            ProjectManager()
        return ProjectManager._instance
    
    def check_manager(self, project: Project):
        if (project._creator.get_role() != "Manager".lower()):
            raise Exception ("Only Manager can create/update/delete project.")

    def create_project(self, project : Project):
        self.projects[project.get_id()] = project
        print(f"Created project {project.get_id()} successfully.")
    
    def add_task_to_project(self, project: Project, task: Task) -> bool:
        if project and task:
            if project.get_id() in self.projects:
                project.get_assigned_tasks().append(task)  # Assuming project.tasks is the list attribute
                print(f"Added task {task.get_id()} to project {project.get_id()} successfully.")
                return True
        return False

    def delete_task_from_project(self, project: Project, task: Task) -> bool:
        if project and task:
            if project.get_id() in self.projects:
                if task in project.get_assigned_tasks():  # Assuming project.tasks is the list attribute
                    project.get_assigned_tasks().remove(task)
                    print(f"Removed task {task.get_id()} from project {project.get_id()} successfully.")
                    return True
        print("Failed to remove task from project.")
        return False

    def update_project(self, project: Project):
        self.check_manager(project)
        if project.get_id() in self.projects:
            project.set_title(input("Enter new project name: "))
            project.set_description(input("Enter new description: "))
            project.set_due_date(datetime(int(input("Enter year: ")), int(input("Enter month: ")), int(input("Enter date: "))))
            print(f"Updated project {project.get_id()} successfully.")
        else:
            print("Project not found")

    def delete_project(self, project: Project):
        self.check_manager(project)
        if project.get_id() in self.projects:
            del self.projects[project.get_id()]
            print(f"Deleted project {project.get_id()} successfully")
        else:
            print("Project not found")

    def _save_project_to_file(self):
        try:
            with open("projects.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Project_ID", "Project_Title", "Project_Description", "Project_Due_Date", 
                    "Creator_ID", "Task_ID", "Task_Title", "Task_Description", "Task_Due_Date", "Task_Status"
                ])
                for project in self.projects.values():
                    tasks = project.get_tasks()
                    if tasks:  # If project has tasks
                        for task in tasks:
                            writer.writerow([
                                project.get_id(),
                                project.get_title(),
                                project.get_description(),
                                project.get_due_date(),
                                project.get_creator(),
                                task.get_id(),
                                task.get_title(),
                                task.get_description(),
                                task.get_due_date(),
                                task.get_status()
                            ])
                    else:  # If project has no tasks
                        writer.writerow([
                            project.get_id(),
                            project.get_title(),
                            project.get_description(),
                            project.get_due_date(),
                            project.get_creator(),
                            "", "", "", "", ""  # Empty task fields
                        ])
                print("Projects successfully saved to file.")
        except Exception as e:
            print(f"Error saving projects to file: {str(e)}")


# pm = ProjectManager.get_instance()
# user1 = User(1, 'Bob', 'bob@gmail.com', 'pw123', 'staff')
# user2 = User(2, 'Alice', 'alice@gmail.com', 'pw456','manager')

# task1 = Task('analyze data', 'create excel sheet', datetime(2025,4,5), user1, user2)
# task2 = Task('analyze sheet', 'create chart', datetime(2025,4,5), user1, user2)
# task3 = Task('lala', 'lili', datetime(2025, 6, 4), user1, user2)

# project1 = Project('ProjA', 'big project', datetime(2025, 7, 8),user2)
# pm.create_project(project1)
# pm.add_task_to_project(project1, task3)
# pm.add_task_to_project(project1, task1)
# # pm.update_project(project1)
# pm.delete_task_from_project(project1, task3)
# pm.delete_project(project1)
# pm._save_project_to_file()

