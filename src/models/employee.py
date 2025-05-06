from user import User
from task import Task
from datetime import datetime
from task_controller import TaskManager

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
        self.task_comments = {}

    def get_assigned_tasks(self):
        """
        Retrieves tasks assigned to this employee from TaskManager.
        
        Returns:
            list: A list of Task objects.
        """
        manager = TaskManager.get_instance()
        return manager.get_user_assigned_tasks(self.user_id) or []
    
    def display_tasks(self):
        """
        Displays the tasks assigned to the employee in a readable format.
        """
        tasks = self.get_assigned_tasks()
        if not tasks:
            print(f"No tasks assigned to {self.username}")
            return
        
        print(f"\nTasks assigned to {self.username}:")
        for task in tasks:
            print(f"\nTask {task.get_id()}: {task.get_title()}")
            print(f"Description: {task.get_description()}")
            print(f"Due Date: {task.get_due_date()}")
            print(f"Status: {task.get_status()}")
            print(f"Priority: {task.get_priority()}")
            print("-" * 50)