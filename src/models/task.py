from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    """
    Enum representing the status of a task.
    """
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class TaskPriority(Enum):
    """
    Enum representing the priority level of a task.
    """
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    UNDEFINED = 4


class Task:
    """
    Task represents a work item with attributes like title, description,
    due date, priority, status, assigned user, and creator.
    """

    def __init__(self, title, description='', due_date=None, assigned_user=None, creator=None):
        """
        Initializes a new Task object.

        Args:
            title (str): Title of the task.
            description (str, optional): Description of the task.
            due_date (datetime, optional): Due date for the task.
            assigned_user (optional): ID of the assigned user.
            creator (optional): ID of the user who created the task.
        """
        self._id = None
        self._title = title
        self._description = description
        self._due_date = due_date
        self._priority = TaskPriority.UNDEFINED
        self._status = TaskStatus.PENDING
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._assigned_user = assigned_user
        self._creator = creator

    # --- Getters ---

    def get_id(self):
        """
        Returns the task ID.
        """
        return self._id

    def get_title(self):
        """
        Returns the task title.
        """
        return self._title

    def get_description(self):
        """
        Returns the task description.
        """
        return self._description

    def get_due_date(self):
        """
        Returns the task due date.
        """
        return self._due_date

    def get_priority(self):
        """
        Returns the task priority as a string.
        """
        return self._priority.name

    def get_status(self):
        """
        Returns the task status as a string.
        """
        return self._status.name

    def get_created_at(self):
        """
        Returns the task creation timestamp.
        """
        return self._created_at

    def get_updated_at(self):
        """
        Returns the last updated timestamp.
        """
        return self._updated_at

    def get_assigned_user(self):
        """
        Returns the ID of the assigned user.
        """
        return self._assigned_user

    def get_creator_id(self):
        """
        Returns the ID of the creator of the task.
        """
        return self._creator

    def get_task(self, task_id):
        """
        Placeholder: Returns a task by ID if managed internally.

        Args:
            task_id (int): Task ID to retrieve.

        Returns:
            Task: The task object if exists.
        """
        return self.tasks.get(task_id)

    # --- Setters ---

    def set_id(self, task_id: int):
        """
        Sets the task ID.

        Args:
            task_id (int): The new task ID.
        """
        self._id = task_id

    def set_title(self, title):
        """
        Sets a new title for the task.

        Args:
            title (str): The new title.
        """
        self._title = title
        self._updated_at = datetime.now()

    def set_description(self, description):
        """
        Sets a new description for the task.

        Args:
            description (str): The new description.
        """
        self._description = description
        self._updated_at = datetime.now()

    def set_due_date(self, due_date):
        """
        Sets a new due date for the task.

        Args:
            due_date (datetime): The new due date.
        """
        self._due_date = due_date
        self._updated_at = datetime.now()

    def set_priority(self, priority):
        """
        Sets the priority of the task.

        Args:
            priority (str): The new priority ("HIGH", "MEDIUM", "LOW").
        """
        if priority == 'LOW':
            self._priority = TaskPriority.LOW
        elif priority == 'MEDIUM':
            self._priority = TaskPriority.MEDIUM
        elif priority == 'HIGH':
            self._priority = TaskPriority.HIGH
        self._updated_at = datetime.now()

    def set_status(self, status):
        """
        Sets the status of the task.

        Args:
            status (str): The new status ("PENDING", "IN PROGRESS", "COMPLETED").
        """
        if status == 'COMPLETED':
            self._status = TaskStatus.COMPLETED
        elif status == 'PENDING':
            self._status = TaskStatus.PENDING
        elif status == 'IN PROGRESS':
            self._status = TaskStatus.IN_PROGRESS
        self._updated_at = datetime.now()

    def set_assigned_user(self, user_id):
        """
        Sets the assigned user for the task.

        Args:
            user_id (int): ID of the assigned user.
        """
        self._assigned_user = user_id
        self._updated_at = datetime.now()

    def set_creator(self, creator_id):
        """
        Sets the creator of the task.

        Args:
            creator_id (int): ID of the creator.
        """
        self._creator = creator_id
        self._updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        base_str = (f"ID: {self._id} | Title: {self._title} | Status: [{self._status.name}]"
                    f" | Priority: {self._priority.name} | Due: {self._due_date}"
                    f" | Assigned to user ID: {self._assigned_user if self._assigned_user else 'Unassigned'}")
        return base_str


class TaskComment:
    """
    TaskComment represents a comment made on a task,
    including task ID, user ID, comment text, and timestamp.
    """

    def __init__(self, task_id: int, user_id: int, comment: str, timestamp: datetime):
        """
        Initializes a new TaskComment.

        Args:
            task_id (int): ID of the task.
            user_id (int): ID of the user making the comment.
            comment (str): The comment text.
            timestamp (datetime): The timestamp of the comment.
        """
        self.task_id = task_id
        self.user_id = user_id
        self.comment = comment
        self.timestamp = timestamp

    def to_dict(self):
        """
        Converts the TaskComment to a dictionary.

        Returns:
            dict: A dictionary representation of the TaskComment.
        """
        return {
            "task_id": self.task_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        """
        Returns a string representation of the TaskComment.
        """
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] User {self.user_id}: {self.comment}"
