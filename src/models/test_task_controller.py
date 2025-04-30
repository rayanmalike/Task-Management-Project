import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
from task import Task
from task_controller import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager.get_instance()

    @patch("builtins.open", new_callable=mock_open)
    def test_add_comment(self, mock_file):
        # Simulate an empty task_comments.csv file
        mock_file.return_value.read.side_effect = [
            "",  # Empty content for task_comments.csv
        ]
        
        # Create a task and add it
        task = Task("Commented Task", due_date=datetime.now())
        task.set_id("5")  # Set a task ID
        task.set_assigned_user("1")
        task.set_creator("1")
        
        # Create the task through the manager
        self.manager.create_task(task)
        
        # Verify that the task was created
        self.assertIn("5", self.manager.tasks)
        
        # Log the current state of the task_manager's tasks and comments
        print(f"Tasks in manager: {self.manager.tasks}")
        
        # Add a comment to the task
        success = self.manager.add_comment("5", 1, "This is a test comment")
        
        # Log the success status and comment addition
        print(f"Success: {success}")
        
        # Now, let's print the actual comments (instead of TaskComment object reference)
        comments = self.manager.task_comments.get("5", [])
        for comment in comments:
            print(f"Comment: {comment.comment}, Timestamp: {comment.timestamp}")

        # Assert that the comment was successfully added
        self.assertTrue(success)
        
        # Check if the comment has been added to the task
        self.assertEqual(len(self.manager.task_comments["5"]), 1)
        self.assertEqual(self.manager.task_comments["5"][0].comment, "This is a test comment")

        # Verify that the CSV file was opened for writing the comments
        mock_file.assert_called_with("task_comments.csv", "w", newline="")
        handle = mock_file()
        handle.write.assert_called()  # Ensure that write was called to save the comments

# if __name__ == "__main__":
#     unittest.main()

# cd src -> models
# python -m unittest -v  test_task_controller 