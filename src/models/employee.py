from user import User
from task import *
from datetime import datetime
import csv

class Employee(User):
    def __init__(self, id, name, email, password, role):
        super().__init__(id, name, email,password, role)
        self.assigned_tasks = {}
        self.task_comments = {}
        self._load_tasks_from_csv()

    def _load_tasks_from_csv(self):
        try:
            with open('tasks.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row['Assigned_User_ID']) == int(self.user_id):
                        duedate = datetime.fromisoformat(row['Due_Date'])
                        task = Task(row['Title'],
                                    row['Description'],
                                    duedate,
                                    self.user_id,
                                    row['Creator_ID'])
                        task.set_id(row['Task_ID'])
                        task.set_status(row['Status'])
                        task.set_priority(row['Priority'])
                        self.assigned_tasks[task.get_id()] = task
        
        except FileNotFoundError:
            print("Tasks file not found.")

    def get_assigned_tasks(self):
        return self.assigned_tasks
    
    def display_tasks(self):
        self._load_tasks_from_csv()
        if not self.assigned_tasks:
            print(f"No tasks assigned to {self.username}")
            return
            
        print(f"\nTasks assigned to {self.username}:")
        for task_id, task in self.assigned_tasks.items():
            print(f"\nTask {task_id}: {task.get_title()}")
            print(f"Description: {task.get_description()}")
            print(f"Due Date: {task.get_due_date()}")
            print(f"Status: {task.get_status()}")
            print(f"Priority: {task.get_priority()}")
            print("-" * 50)

    