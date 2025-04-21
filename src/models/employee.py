from user import User
from project import Project
from task import Task, TaskPriority, TaskStatus
from task_controller import TaskManager
from datetime import datetime
from manager import Manager #to be removed
import csv

file = open("tasks.csv", "r")

class Employee(User):
    def __init__(self, id, name, email, password, role):
        super().__init__(id, name, email,password, role)
        self.assigned_tasks = []

    def _load_tasks_from_csv(self):
        try:
            with open('tasks.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Assigned User ID'] == str(self.get_user_id()):
                        # Get the task from TaskManager instance instead of creating new one
                        task_id = row['ID']  # Assuming there's an ID column in CSV
                        task = TaskManager.get_instance().tasks.get(task_id)
                        
                        if task:
                            self.assigned_tasks.append(task)
                        
        except FileNotFoundError:
            print("Tasks file not found.")
                            
        # except Exception as e:
        #     print(f"Error loading tasks: {str(e)}")
    
    def get_assigned_tasks(self):
        return self.assigned_tasks
    
    def display_tasks(self):
        if not self.assigned_tasks:
            print(f"No tasks assigned to {self.get_username()}")
            return
            
        print(f"\nTasks assigned to {self.get_username()}:")
        for task in self.assigned_tasks:
            print(f"\nTask: {task.get_title()}")
            print(f"Description: {task.get_description()}")
            print(f"Due Date: {task.get_due_date()}")
            print(f"Status: {task.get_status()}")
            print(f"Priority: {task.get_priority()}")
            print("-" * 50)

    def submit_task(self, task: Task):
        return TaskManager.mark_task_as_completed(TaskManager, task)

    def get_task_description(self, task: Task):
        return task.get_description()

    def get_task_due_date(self, task: Task):
        return task.get_due_date()

    def get_task_priority(self, task: Task):
        return task.get_priority()

    def get_project_description(self, project):
        return project.get_description()

    def get_project_due_date(self, project):
        return project.get_due_date()


file.close()

# tm = TaskManager.get_instance()
# user1 = Employee(1, 'Bob', 'bob@gmail.com', 'pw123', 'staff')
# user2 = Manager(2, 'Alice', 'alice@gmail.com', 'pw456','manager')

# task1 = Task('analyze data', 'create excel sheet', datetime(2025,4,5), user1, user2)
# task2 = Task('analyze sheet', 'create chart', datetime(2025,4,5), user1, user2)

# tm.create_task(task1)
# tm.create_task(task2)
# tm._save_tasks_to_csv()



# user1._load_tasks_from_csv()
# user1.get_assigned_tasks()
# user1.display_tasks()

# # print(emp.get_task_priority(emp.assigned_tasks[0]))
# # print(emp.get_task_description(emp.assigned_tasks[1]))
# user1.submit_task(user1.assigned_tasks[0])
# user1.display_tasks()
# tm._save_tasks_to_csv()


