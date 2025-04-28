from datetime import datetime
from enum import Enum

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
        self._id = None
        self._title = title
        self._description = description
        self._due_date = due_date  # datetime object
        self._priority = TaskPriority.UNDEFINED # default Undefined
        self._status = TaskStatus.PENDING # default 
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._assigned_user = assigned_user 
        self._creator = creator
        # self._comments = []

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
        return self._creator
    
    def get_task(self, task_id):
        return self.tasks.get(task_id)
    
    # --- Setters ---
    def set_id (self, task_id: int):
        self._id = task_id
        
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
        if priority == 'LOW' : self._priority= TaskPriority.LOW
        elif priority == 'MEDIUM': self._priority= TaskPriority.MEDIUM
        elif priority == 'HIGH' : self._priority=TaskPriority.HIGH
        self._updated_at = datetime.now()

    def set_status(self, status):
        if status == 'COMPLETED' : self._status= TaskStatus.COMPLETED
        elif status == 'PENDING': self._status=TaskStatus.PENDING
        elif status == 'IN PROGRESS' : self._status=TaskStatus.IN_PROGRESS
        self._updated_at = datetime.now()

    def set_assigned_user(self, user_id):
        self._assigned_user =  user_id
        self._updated_at = datetime.now()

    def set_creator(self, creator_id):
        self._creator = creator_id
        self._updated_at = datetime.now()
        
    def __str__(self):
        base_str = f"ID: {self._id} | Title: {self._title} | Status: [{self._status.name}]  | Priority: {self._priority.name} | Due: {self._due_date} | Assigned to user ID: {self._assigned_user if self._assigned_user else 'Unassigned'}"
        # comments = self.display_comments()
        return base_str
    
class TaskComment:
    def __init__(self, task_id: int, user_id: int, comment: str, timestamp: datetime):
        self.task_id = task_id
        self.user_id = user_id
        self.comment = comment
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] User {self.user_id}: {self.comment}"