from user import User
from task import Task
from project import Project

class Manager(User):
    def __init__(self, id, name, email, role):
        super().__init__(id, name, email, role)
        self.tasks = {}
        self.projects = {}

    def create_task(self, title, description, due_date, priority, assigned_user=None):
        new_task = Task(title, description, due_date, priority, assigned_user)
        self.tasks =[new_task.get_id()] = new_task
        return new_task

    def update_task():
        pass

    def delete_task():
        pass

    def assign_task():
        pass

    def track_task_status():
        pass

    def create_project():
        pass

    def update_project():
        pass
