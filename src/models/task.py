from datetime import datetime
from enum import Enum
import uuid

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4

class Task:
    def __init__(self, title, description='', due_date=None, priority=1, assigned_user=None):
        self._id = str(uuid.uuid4())
        self._title = title
        self._description = description
        self._due_date = due_date  # datetime object
        self._priority = priority  # int from 1-3
        self._status = TaskStatus.PENDING
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._assigned_user = assigned_user  # Expected to be a User object

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
        return self._priority

    def get_status(self):
        return self._status

    def get_created_at(self):
        return self._created_at

    def get_updated_at(self):
        return self._updated_at

    def get_assigned_user(self):
        return self._assigned_user

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

    def set_priority(self, priority):
        self._priority = priority
        self._updated_at = datetime.now()

    def set_status(self, status: TaskStatus):
        self._status = status
        self._updated_at = datetime.now()

    def set_assigned_user(self, user):
        self._assigned_user = user
        self._updated_at = datetime.now()

    def __str__(self):
        return f"[{self._status.name}] {self._title} | Due: {self._due_date} | Assigned to: {self._assigned_user.get_name() if self._assigned_user else 'Unassigned'}"
