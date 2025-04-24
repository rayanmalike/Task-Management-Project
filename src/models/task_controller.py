from datetime import datetime
from task import *
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
    
    def check_manager(self, task: Task):
        if (task._creator.get_role() != "Manager".lower()):
            raise Exception ("Only Manager can create/update/delete tasks.")
        

    def create_task(self, task : Task):
        self.check_manager(task)
        self.tasks[task.get_id()] = task
        self._assign_task_to_user(task.get_assigned_user(), task)
        print(f"Created task {task.get_id()} successfully.")
        

    def update_task(self, existing_task: Task):
        self.check_manager(existing_task)
        
        if existing_task:
            existing_task.set_title(input("Enter new title for task: "))
            existing_task.set_description(input("Enter new description for task: "))
            existing_task.set_due_date(datetime(int(input("Enter year: ")), int(input("Enter month: ")), int(input("Enter date: "))))
            existing_task._updated_at = datetime.now()
            previous_user = existing_task._assigned_user.get_user_id()
            new_user = input("Enter assigned user ID: ")
            if previous_user != new_user:
                self._unassign_task_from_user(previous_user, existing_task)
                self._assign_task_to_user(new_user, existing_task)
            print(f"Updated task {existing_task.get_id()} successfully.")
        
        else:
            print(f"Task must be existed")

    def delete_task(self, task: Task):
        self.check_manager(task)
        task = self.tasks.pop(task.get_id(), None)
        if task:
            self._unassign_task_from_user(task.get_assigned_user(), task)
        print(f"Deleted task {task.get_id()} successfully")

    def mark_task_as_completed(self, task: Task):
        self.check_manager(task)
        if task:
            task.set_status(TaskStatus.COMPLETED)
        print(f"Marked task {task.get_id()} status to [COMPLETED].")

    def change_task_priority(self, task: Task, priority: TaskPriority):
        self.check_manager(task)
        if task:
            task.set_priority(priority)
        print(f"Changed task {task.get_id()} priority to [{priority.name}]")

    def add_comment_to_task(self, task: Task, user, comment_text: str):
        if task and (self._is_manager(user) or user == task.get_assigned_user()):
            task.add_comment(user, comment_text)
            print(f"Comment added to task {task.get_id()} successfully.")
        else:
            print("Only managers or assigned users can add comments to tasks.")

    def view_task_comments(self, task: Task):
        if task:
            print(f"Comments for task {task.get_id()} - {task.get_title()}:")
            print(task.display_comments())
        else:
            print("Task not found.")

    def _assign_task_to_user(self, user, task: Task):
        if user not in self.user_tasks:
            self.user_tasks[user] = []
        self.user_tasks[user].append(task)

    def _unassign_task_from_user(self, user, task: Task):
        if user in self.user_tasks:
            if task in self.user_tasks[user]:
                self.user_tasks[user].remove(task)
                # If user has no more tasks, remove the user entry
                if not self.user_tasks[user]:
                    del self.user_tasks[user]

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
                    task.get_status(),
                    task.get_assigned_user().get_user_id() if task.get_assigned_user() else "",
                    task.get_creator_id() 
                    # if hasattr(task, "creator_id") else ""
                ])
        file.close()
    

# tm = TaskManager.get_instance()
# user1 =User(1, 'Bob', 'bob@gmail.com', 'pw123', 'staff')
# user2 = User(2, 'Alice', 'alice@gmail.com', 'pw456','manager')

# task1 = Task('analyze data', 'create excel sheet', datetime(2025,4,5), user1, user2)
# task2 = Task('analyze sheet', 'create chart', datetime(2025,4,5), user1, user2)
# task3 = Task('lala', 'lili', datetime(2025, 6, 4), user1, user2)


# tm.create_task(task1)
# tm.create_task(task2)
# tm.update_task(task1)
# tm._save_tasks_to_csv()
