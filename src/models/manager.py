from user import User
from task import Task, TaskStatus
from project import Project
from datetime import datetime

class Manager(User):
    def __init__(self, id, name, email, password,  role):
        super().__init__(id, name, email, password, role)
        self.tasks = {}
        self.projects = {}

    def create_task(self, task_id, title, description, due_date, priority, assigned_user=None):
        new_task = Task(title, description, due_date, priority, assigned_user)
        new_task._id = task_id
        self.tasks[task_id] = new_task
        return new_task

    def update_task(self, task_id, title=None, description=None, due_date=None, priority=None, status=None, assigned_user=None):
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        task = self.tasks[task_id]
        if title:
            task.set_title(title)
        if description:
            task.set_description(description)
        if due_date:
            task.set_due_date(due_date)
        if priority:
            task.set_priority(priority)
        if status:
            task.set_status(status)
        if assigned_user:
            task.set_assigned_user(assigned_user)
        return task

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError("Task not found.")

    def assign_task(self, task_id, user):
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        task = self.tasks[task_id]
        task.set_assigned_user(user)
        return task

    def track_task_status(self, task_id):
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        return self.tasks[task_id].get_status()

    def create_project(self, project_id, project_name, description, start_date, end_date):
        new_project = Project(project_id, project_name, description, self.get_id(), start_date, end_date)
        self.projects[project_id] = new_project
        return new_project

    def update_project(self, project_id, project_name=None, description=None, start_date=None, end_date=None):
        if project_id not in self.projects:
            raise ValueError("Project not found.")
        project = self.projects[project_id]
        if project_name:
            project.set_project_title(project_name)
        if description:
            project.set_project_description(description)
        if start_date:
            project.set_start_date(start_date)
        if end_date:
            project.set_end_date(end_date)
        return project
