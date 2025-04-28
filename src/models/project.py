from datetime import datetime

class Project:
    """"
    Represents a project containing tasks with attributes such as title, description, due date, and creator.
    """"
    def __init__(self, title, description = '', due_date = None, creator_id = None):
        """
        Initializes a new Project instane.

        Args:
            title(str): Title of project
            description (str, optional): A brief description of the project.
            due_date (datetime, optional): The due date for each project.
            creator_id (any, optional): The ID of the creator of the project.
        """
        self._id = None
        self._title = title
        self._description = description
        self._due_date = due_date
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._assigned_tasks = {} # dict of Task objects
        self._creator = creator_id

    # Getters and setters
    def get_id(self):
        """Returns the ID of the project."""
        return self._id

    def get_title(self):
        """Returns the title of the project."""
        return self._title

    def get_description(self):
        """Returns the description of the project."""
        return self._description
    
    def get_due_date(self):
        """Returns the due date of the project."""
        return self._due_date

    def get_created_at(self):
        """Returns the timestamp when project was created."""
        return self._created_at

    def get_updated_at(self):
        """Returns the timestamp when the project was last updated."""
        return self._updated_at

    def get_assigned_tasks_by_id(self, task_id):
        """
        Returns a specific assigned task by its ID.

        Args:
            task_id (any): The ID of the task to retrieve.
        Returns:
            Task: the task object that correlates with the ID.
        """
        try:
            if task_id in self._assigned_tasks:
                return self._assigned_tasks.get(task_id)
        except:
            print ("Task not found")

    def get_assigned_tasks (self):
        """Returns all assigned tasks in the project."""
        return self._assigned_tasks
    
    def get_creator(self):
        """Returns the ID of the creator of the project."""
        return self._creator
    
    def set_id(self, id):
        """
        Sets a unique ID for the project.

        Args:
            title(str): The new title of the project.
        """
        self._id = id

    def set_title(self, title):
        """
        Updates the title of the project.

        Args:
            title(str): The new title of the project.
        """
        self._title = title

    def set_description(self, description):
        """
        Updates the description of the project

        Args:
            description(str): New description of the project.
        """
        self._description = description

    def set_due_date(self, due_date):
        """
        Updates the due date of the project.

        Args:
            due_date(datetime): New due date for the project.
        """
        self._due_date = due_date
        self._updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the project in which it shows the title, due date, and summary.

        Returns:
            str: String description of the project.
        """
        tasks_str = "No tasks added yet." if not self._assigned_tasks else ", ".join(str(task) for task in self._assigned_tasks)
        return f"Project {self._id}: {self._title} | Due: {self._due_date} | Tasks: {tasks_str}"

            
