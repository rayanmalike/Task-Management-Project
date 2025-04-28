from datetime import datetime
from task import Task, TaskComment
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
            self.task_comments = {}
            self.load_tasks_from_csv()
            self._load_comments_from_csv()

    @staticmethod
    def get_instance():
        if TaskManager._instance is None:
            TaskManager()
        return TaskManager._instance
    
    def create_task(self, task : Task):
        self.tasks[task.get_id()] = task
        self._assign_task_to_user(task.get_assigned_user(), task)
        self._save_tasks_to_csv()
        print(f"Created task {task.get_id()} successfully.")
        
    def update_task(self, existing_task: Task):
        if existing_task:
            existing_task.set_title(input("Enter new title for task: "))
            existing_task.set_description(input("Enter new description for task: "))
            existing_task.set_due_date(datetime(int(input("Enter year: ")), int(input("Enter month: ")), int(input("Enter date: "))))
            existing_task._updated_at = datetime.now()
            previous_user = existing_task.get_assigned_user()
            new_user = input("Enter new assigned user ID: ")
            if previous_user != new_user:
                self._unassign_task_from_user(previous_user, existing_task)
                self._assign_task_to_user(new_user, existing_task)
            existing_task.set_assigned_user(new_user)
            existing_task.set_creator(existing_task.get_creator_id())
            print(f"Updated task {existing_task.get_id()} successfully.")
            self._save_tasks_to_csv()
        
        else:
            print(f"Task must be existed")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        self._unassign_task_from_user(task.get_assigned_user(), task)
        self.tasks.pop(task_id)
        print(f"Deleted task {task_id} successfully")
        self._save_tasks_to_csv()

    def mark_task_as_completed(self, task: Task):
        if task:
            task.set_status('COMPLETED')
            self._save_tasks_to_csv()  # Save changes to CSV
            print(f"Marked task {task.get_id()} status to [COMPLETED].")
            return True
        else:
            return False

    def change_task_priority(self, task_id , priority):
        if task_id in self.tasks:
            task = self.tasks.get(task_id)
            task.set_priority(priority)
            print(f"Changed task {task_id} priority to {priority} successfully")
            self._save_tasks_to_csv()
        else:
            print(f"Task must be existed")

    def _assign_task_to_user(self, user_id, task: Task):
        if user_id not in self.user_tasks:
            self.user_tasks[user_id] = []
        self.user_tasks[user_id].append(task)

    def _unassign_task_from_user(self, user_id, task: Task):
        if user_id in self.user_tasks:
            if task in self.user_tasks[user_id]:
                self.user_tasks[user_id].remove(task)
                # If user has no more tasks, remove the user entry
                if not self.user_tasks[user_id]:
                    del self.user_tasks[user_id]

    def list_tasks(self):
        for task in self.tasks.values():
            print(task)
    
    def _save_tasks_to_csv(self):
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Task_ID", "Title", "Description", "Due_Date",
                "Priority", "Status", "Assigned_User_ID", "Creator_ID"
            ])
            for task_id, task in self.tasks.items():
                writer.writerow([
                    task.get_id(), task.get_title(), task.get_description(),
                    task.get_due_date().isoformat(), task.get_priority(),
                    task.get_status(), task.get_assigned_user(),
                    task.get_creator_id()
                ])
            

    def get_task_by_id(self, task_id):
        try:
            if task_id in self.tasks:
                return self.tasks.get(task_id)
        except:
            print("Task not found")

    def load_tasks_from_csv(self):
        try:
            with open("tasks.csv", "r", newline="") as file:
                reader = csv.DictReader(file)  # Use DictReader instead of reader
                for row in reader:
                    # Skip rows that are just comments
                    if not row['Task_ID'] or row['Task_ID'] in self.tasks:
                        continue
                        
                    # Convert string date back to datetime
                    due_date = datetime.fromisoformat(row['Due_Date'])
                    
                    # Create new task object
                    task = Task(row['Title'], row['Description'], due_date)
                    
                    # Set additional properties
                    task._id = row['Task_ID']
                    task.set_priority(row['Priority'])
                    task.set_status(row['Status'])
                    task.set_assigned_user(row['Assigned_User_ID'])
                    task.set_creator(row['Creator_ID'])
                    
                    # Store in tasks dictionary
                    self.tasks[row['Task_ID']] = task
                    
        except FileNotFoundError:
            print("No tasks.csv file found.")
        except Exception as e:
            print(f"Error loading tasks: {str(e)}")

    def _load_comments_from_csv(self):
        try:
            self.task_comments.clear()
            with open("task_comments.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task_id = int(row["TaskID"])
                    if task_id not in self.task_comments:
                        self.task_comments[task_id] = []
                        
                    comment = TaskComment(
                        task_id=task_id,
                        user_id=int(row["UserID"]),
                        comment=row["Comment"],
                        timestamp=datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S")
                    )
                    self.task_comments[task_id].append(comment)

                #Displaying the comments
                if self.task_comments:
                    [print(comment) for comment in self.task_comments[task_id]]
                else: 
                    print("No comments to display")
                return True
        except FileNotFoundError:
            print("Comments CSV file not found. Starting with empty comments.")
            return False

    def _save_comments_to_csv(self):
        try:
            with open("task_comments.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["TaskID", "UserID", "Comment", "Timestamp"])
                for task_id, comments in self.task_comments.items():
                    for comment in comments:
                        writer.writerow([
                            comment.task_id,
                            comment.user_id,
                            comment.comment,
                            comment.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        ])
            print("Successfully saved comments to CSV")
        except Exception as e:
            print(f"Error saving comments to CSV: {str(e)}")

    def get_user_assigned_tasks(self, user_id):
        if user_id in self.user_tasks:
            return self.user_tasks.get(user_id)
    
    def get_task_comments(self, task_id):
        """Get comments for a specific task with safe dictionary access."""
        try:
            self._load_comments_from_csv()
            return self.task_comments.get(task_id, [])
                
        except Exception as e:
            print(f"Error retrieving comments for task {task_id}: {str(e)}")
            return []

    def add_comment(self, task_id, user_id, comment: str) -> bool:
        try:
            if task_id not in self.tasks:
                return False
                
            if task_id not in self.task_comments:
                self.task_comments[task_id] = []
                
            comment_obj = TaskComment(task_id, user_id, comment, datetime.now())
            self.task_comments[task_id].append(comment_obj)
            self._save_comments_to_csv()
            return True
        except Exception as e:
            print(f"Failed to add comment: {str(e)}")
            return False
    
 
    