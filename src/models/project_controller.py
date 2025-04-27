from project import Project
from task import Task
import csv
from datetime import datetime

class ProjectManager:
    _instance = None

    def __init__(self):
        if ProjectManager._instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            ProjectManager._instance = self
            self.projects = {}
            self._load_projects_from_csv()
    
    @staticmethod
    def get_instance():
        if ProjectManager._instance is None:
            ProjectManager()
        return ProjectManager._instance

    def create_project(self, project : Project):
        self.projects[project.get_id()] = project
        self._save_project_to_file()
        print(f"Created project {project.get_id()} successfully.")
    
    def add_task_to_project(self, project: Project, task: Task) -> bool:
        if project and task:
            if project.get_id() in self.projects:
                project.get_assigned_tasks()[task.get_id()] = task 
                print(f"Added task {task.get_id()} to project {project.get_id()} successfully.")
                self._save_project_to_file()
                return True
        return False

    def delete_task_from_project(self, project: Project, task: Task) -> bool:
        if project and task:
            if project.get_id() in self.projects:
                if task.get_id() in project.get_assigned_tasks():
                    del project.get_assigned_tasks()[task.get_id()]
                    print(f"Removed task {task.get_id()} from project {project.get_id()} successfully.")
                    self._save_project_to_file()
                    return True
            print("Failed to remove task from project.")
            return False

    def update_project(self, project: Project):
            project.set_title(input("Enter new project title: "))
            project.set_description(input("Enter new description: "))
            project.set_due_date(datetime(int(input("Enter year: ")), int(input("Enter month: ")), int(input("Enter date: "))))
            self._save_project_to_file()
            print(f"Updated project {project.get_id()} successfully.")

    def delete_project(self, project: Project):
            del self.projects[project.get_id()]
            self._save_project_to_file()
            print(f"Deleted project {project.get_id()} successfully")

    def _save_project_to_file(self):
        try:
            with open("projects.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Project_ID", "Project_Title", "Project_Description", "Project_Due_Date", 
                    "Creator_ID", "Task_ID", "Task_Title", "Task_Description", "Task_Due_Date", "Task_Status"
                ])
                for project in self.projects.values():
                    tasks = project.get_assigned_tasks()
                    if tasks:  # If project has tasks
                        for task_id, task in tasks.items():
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

    def _load_projects_from_csv(self):
        try:
            with open("projects.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Skip if project ID is empty or project already exists
                    if not row['Project_ID'] or row['Project_ID'] in self.projects:
                        continue
                    
                    # Convert string date to datetime
                    due_date = datetime.fromisoformat(row['Project_Due_Date'])
                    
                    # Create new project
                    project = Project(
                        row['Project_Title'],
                        row['Project_Description'],
                        due_date,
                        row['Creator_ID']
                    )
                    project.set_id(row['Project_ID'])
                    
                    # Add task if task fields are not empty
                    if row['Task_ID']:
                        task_due_date = datetime.fromisoformat(row['Task_Due_Date'])
                        task = Task(
                            row['Task_Title'],
                            row['Task_Description'],
                            task_due_date
                        )
                        task.set_id(row['Task_ID'])
                        task.set_status(row['Task_Status'])
                        project.get_assigned_tasks()[task.get_id()] = task
                    
                    # Store project in projects dictionary
                    self.projects[project.get_id()] = project
                    
            print("Projects loaded successfully from CSV.")
        except FileNotFoundError:
            print("No projects.csv file found.")
        except Exception as e:
            print(f"Error loading projects: {str(e)}")


    def get_project_by_id(self, project_id):
        try:
            if project_id in self.projects:
                return self.projects.get(project_id)
        except:
            print("Project not found")

    def get_all_projects(self):
        """
        Returns a list of all projects in the system
        
        Returns:
            List[Project]: List containing all project objects
        """
        return list(self.projects.values())

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

