from datetime import datetime
from task import *
from employee import Employee
from manager import Manager
import csv

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
        # self._assign_task_to_user(task.get_assigned_user(), task)
        print(f"Created task {task.get_id()} successfully.")

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

    def delete_task(self, task: Task):
        task = self.tasks.pop(task.get_id(), None)
        if task:
            self._unassign_task_from_user(task.get_assigned_user(), task)
        print(f"Deleted task {task.get_id()} successfully")

    def mark_task_as_completed(self, task: Task):
        if task:
            task.set_status(TaskStatus.COMPLETED)
        print(f"Marked task {task.get_id()} status to [COMPLETED].")

    def change_task_priority(seld, task: Task, priority: TaskPriority):
        if task:
            task.set_priority(priority)
        print(f"Changed task {task.get_id()} priority to [{priority.name}]")


    def _assign_task_to_user(self, user: Employee, task: Task):
        self.user_tasks.setdefault(user.get_user_id(), []).append(task)

    def _unassign_task_from_user(self, user: Employee, task: Task):
        tasks = self.user_tasks.get(user.get_user_id())
        if tasks:
            tasks.remove(task)

    def list_tasks(self):
        for task in self.tasks.values():
            print(task)
    
    def _save_tasks_to_csv(self):
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID", "Title", "Description", "Due Date",
                "Priority", "Status", "Assigned User ID", "Creator ID"
            ])
            for task in self.tasks.values():
                writer.writerow([
                    task.get_id(),
                    task.get_title(),
                    task.get_description(),
                    task.get_due_date().isoformat(),
                    task.get_priority(),
                    task.get_status().name,
                    task.get_assigned_user().get_user_id() if task.get_assigned_user() else "",
                    task.get_creator_id() 
                    # if hasattr(task, "creator_id") else ""
                ])
        file.close()
    

# tm = TaskManager.get_instance()
# user1 = Employee(1, 'Bob', 'bob@gmail.com', 'pw123', 'staff')
# user2 = Manager(2, 'Alice', 'alice@gmail.com', 'pw456','manager')

# task1 = Task('analyze data', 'create excel sheet', datetime(2025,4,5), user1, user2)
# task2 = Task('analyze sheet', 'create chart', datetime(2025,4,5), user1, user2)

# tm.create_task(task1)
# tm.create_task(task2)
# tm._save_tasks_to_csv()
