from user import User
from task import Task
from datetime import datetime
import csv

class Employee(User):
    """
    Employee class that inherits from the User class.
    Represents an employee who is assigned tasks and can interact with them.

    Attributes:
        assigned_tasks (dict): A dictionary of tasks assigned to the employee.
        task_comments (dict): A dictionary of comments associated with the tasks.
    """
    
    def __init__(self, id, name, email, password, role):
        """
        Initializes an Employee object with the provided details.

        Args:
            id (int): Unique identifier for the employee.
            name (str): Name of the employee.
            email (str): Email address of the employee.
            password (str): Password for the employee's account.
            role (str): Role of the employee (typically "employee").
        """
        super().__init__(id, name, email, password, role)
        self.assigned_tasks = {}
        self.task_comments = {}
        self._load_tasks_from_csv()

    def _load_tasks_from_csv(self):
        """
        Loads tasks assigned to the employee from a CSV file and stores them in the assigned_tasks dictionary.

        The CSV file is expected to contain tasks with columns such as Task_ID, Title, Description, etc.
        Only tasks where the Assigned_User_ID matches the employee's user ID will be loaded.

        Raises:
            FileNotFoundError: If the 'tasks.csv' file is not found.
        """
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
        """
        Retrieves the tasks assigned to the employee.

        Returns:
            dict: A dictionary of tasks assigned to the employee, where the key is the task ID and the value is the task object.
        """
        return self.assigned_tasks
    
    def display_tasks(self):
        """
        Displays the tasks assigned to the employee in a readable format. 

        This method loads the tasks from the CSV file, if not already loaded, and prints the task details.
        If no tasks are assigned, a message is displayed indicating that there are no tasks.
        """
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
