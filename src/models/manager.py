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
        if task.id not in self.tasks:
            raise ValueError("Task not found.")
        task = [self.tasks[task.id]
        if title is not None:
            task.set_title(title)
        if description is not None:
            task.set_description(description)
        if due_date is not None:
            task.set_due_date(due_date)
        if priority is not None:
            task.set_priority(priority)
        if status is not None:
            task.set_status(status)
        if assigned_user is not None:
            task.set_assigned_user(assigned_user)
        return task

    def delete_task():
        if task_id in self.tasks:
            del sel.tasks[task.id]
        else:
            raise ValueError("Task not found.")

    def assign_task():
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        task = self.tasks[task.id]
        task.set_assigned_user(user)
        return task

    def track_task_status():
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        return self.tasks[task_id].get_status()

    def create_project():
        pass

    def update_project():
        pass
