from datetime import datetime

class Project:
    def __init__(self, title, description = '', due_date = None, creator_id = None):
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

    def get_assigned_tasks_by_id(self, task_id):
        try:
            if task_id in self._assigned_tasks:
                return self._assigned_tasks.get(task_id)
        except:
            print ("Task not found")

    def get_assigned_tasks (self):
        return self._assigned_tasks
    
    def get_due_date(self):
        return self._due_date
    
    def get_creator(self):
        return self._creator
    
    def set_id(self, id):
        self._id = id

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_due_date(self, due_date):
        self._due_date = due_date
        self._updated_at = datetime.now()

    def __str__(self):
        tasks_str = "No tasks added yet." if not self._assigned_tasks else ", ".join(str(task) for task in self._assigned_tasks)
        return f"Project {self._id}: {self._title} | Due: {self._due_date} | Tasks: {tasks_str}"

            