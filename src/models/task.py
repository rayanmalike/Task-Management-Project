from datetime import datetime
from enum import Enum
import uuid

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
class TaskPriority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    UNDEFINED = 4

class Task:
    def __init__(self, title, description='', due_date=None, assigned_user=None, creator = None):
        self._id = str(uuid.uuid4())
        self._title = title
        self._description = description
        self._due_date = due_date  # datetime object
        self._priority = TaskPriority.UNDEFINED # default Undefined
        self._status = TaskStatus.PENDING # default 
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._assigned_user = assigned_user # Expected to be a User object
        self._creator = creator

    # --- Getters ---
    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_due_date(self):
        return self._due_date

    def get_priority(self):
        return self._priority.name

    def get_status(self):
        return self._status.name

    def get_created_at(self):
        return self._created_at

    def get_updated_at(self):
        return self._updated_at

    def get_assigned_user(self):
        return self._assigned_user
    
    def get_creator_id(self):
        return self._creator.get_user_id()
    
    # --- Setters ---
    def set_title(self, title):
        self._title = title
        self._updated_at = datetime.now()

    def set_description(self, description):
        self._description = description
        self._updated_at = datetime.now()

    def set_due_date(self, due_date):
        self._due_date = due_date
        self._updated_at = datetime.now()

    def set_priority(self, priority : TaskPriority):
        self._priority = priority
        self._updated_at = datetime.now()

    def set_status(self, status: TaskStatus):
        self._status = status
        self._updated_at = datetime.now()

    def set_assigned_user(self, user):
        self._assigned_user = user
        self._updated_at = datetime.now()

    def __str__(self):
        return f"[{self._status.name}] {self._title} | Priority: {self._priority.name} | Due: {self._due_date} | Assigned to: {self._assigned_user.get_username() if self._assigned_user else 'Unassigned'}"
