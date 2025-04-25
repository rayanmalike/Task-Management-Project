from datetime import datetime
import uuid

class Project:
    def __init__(self, title, description = '', due_date = None, creator = None):
        self._id = None
        self._title = title
        self._description = description
        self._due_date = due_date
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._assigned_tasks = [] # list of Task objects
        # [self._assigned_tasks.append(task) for task in assigned_tasks ]
        self._creator = creator # Manager object

    # Getters and setters
    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description
    
    def get_due_date(self):
        return self._due_date

    def get_created_at(self):
        return self._created_at

    def get_updated_at(self):
        return self._updated_at

    def get_assigned_tasks(self):
        return self._assigned_tasks
    
    def get_due_date(self):
        return self._due_date
    
    def get_creator(self):
        return self._creator.get_user_id()
    
    def set_id(self, id):
        self._id = id

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_due_date(self, due_date):
        self._due_date = due_date
        self._updated_at = datetime.now()
    
    def get_tasks(self):
        return self._assigned_tasks # Where self.tasks is a list of Task objects

    def __str__(self):
        [print(task) for task in self._assigned_tasks]