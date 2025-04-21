from datetime import datetime
import uuid

class Project:
    def __init__(self, title, description = '', due_date = None, assigned_tasks = None, creator = None):
        self._id = str(uuid.uuid4())
        self._title = title
        self._description = description
        self._due_date = due_date
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._assigned_tasks = assigned_tasks # list of Task objects
        self._creator = creator # Manager object

    # Getters and setters
    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_created_at(self):
        return self._created_at

    def get_updated_at(self):
        return self._updated_at

    def get_assigned_tasks(self):
        return self._assigned_tasks

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_due_date(self, due_date):
        self._due_date = due_date
        self._updated_at = datetime.now()

    def __str__(self):
        [print(task) for task in self._assigned_tasks]