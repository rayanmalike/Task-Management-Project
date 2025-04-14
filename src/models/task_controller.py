from datetime import datetime
from task import *
# from user import User

class TaskManager:
    _instance = None

    def __init__(self):
        if TaskManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TaskManager._instance = self
            self.tasks = {}
            self.user_tasks = {}

    @staticmethod
    def get_instance():
        if TaskManager._instance is None:
            TaskManager()
        return TaskManager._instance

    def create_task(self, task : Task):
        self.tasks[task.get_id()] = task
        self._assign_task_to_user(task.get_assigned_user(), task)

    def update_task(self, updated_task):
        existing_task = self.tasks.get(updated_task.get_id())
        if existing_task:
            existing_task.set_title(updated_task.get_title())
            existing_task.set_description(updated_task.get_description())
            existing_task.set_due_date(updated_task.get_due_date())
            existing_task.set_priority(updated_task.get_priority())
            existing_task.set_status(updated_task.get_status())
            previous_user = existing_task.get_assigned_user()
            new_user = updated_task.get_assigned_user()
            if previous_user != new_user:
                self._unassign_task_from_user(previous_user, existing_task)
                self._assign_task_to_user(new_user, existing_task)

    def delete_task(self, task_id):
        task = self.tasks.pop(task_id, None)
        if task:
            self._unassign_task_from_user(task.get_assigned_user(), task)

    def mark_task_as_completed(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            task.set_status(TaskStatus.COMPLETED)

    def _assign_task_to_user(self, user, task):
        self.user_tasks.setdefault(user.get_id(), []).append(task)

    def _unassign_task_from_user(self, user, task):
        tasks = self.user_tasks.get(user.get_id())
        if tasks:
            tasks.remove(task)

    def list_tasks(self):
        for task in self.tasks.values():
            print(task)
        
