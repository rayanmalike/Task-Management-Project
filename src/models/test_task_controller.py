import unittest
from unittest.mock import patch, MagicMock, mock_open
from datetime import datetime
from task_controller import TaskManager
from task import Task, TaskComment

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Reset singleton instance
        TaskManager._instance = None

        # Patch CSV loading to prevent real file I/O
        with patch.object(TaskManager, 'load_tasks_from_csv'), \
             patch.object(TaskManager, '_load_comments_from_csv'):
            self.tm = TaskManager.get_instance()

    def test_create_task(self):
        mock_task = MagicMock(spec=Task)
        mock_task.get_id.return_value = "1"
        mock_task.get_assigned_user.return_value = "user1"

        with patch.object(self.tm, '_save_tasks_to_csv'):
            self.tm.create_task(mock_task)

        self.assertIn("1", self.tm.tasks)
        self.assertIn("user1", self.tm.user_tasks)
        self.assertIn(mock_task, self.tm.user_tasks["user1"])

    def test_mark_task_as_completed(self):
        mock_task = MagicMock(spec=Task)
        mock_task.get_id.return_value = "1"

        with patch.object(self.tm, '_save_tasks_to_csv'):
            result = self.tm.mark_task_as_completed(mock_task)

        mock_task.set_status.assert_called_with("COMPLETED")
        self.assertTrue(result)

    def test_change_task_priority(self):
        mock_task = MagicMock(spec=Task)
        mock_task.get_id.return_value = "1"
        self.tm.tasks["1"] = mock_task

        with patch.object(self.tm, '_save_tasks_to_csv'):
            self.tm.change_task_priority("1", "HIGH")

        mock_task.set_priority.assert_called_with("HIGH")

    def test_delete_task(self):
        mock_task = MagicMock(spec=Task)
        mock_task.get_id.return_value = "1"
        mock_task.get_assigned_user.return_value = "user1"
        self.tm.tasks["1"] = mock_task
        self.tm.user_tasks["user1"] = [mock_task]

        with patch.object(self.tm, '_save_tasks_to_csv'):
            self.tm.delete_task("1")

        self.assertNotIn("1", self.tm.tasks)
        self.assertNotIn("user1", self.tm.user_tasks)

    def test_add_comment(self):
        self.tm.tasks["1"] = MagicMock(spec=Task)

        with patch.object(self.tm, '_save_comments_to_csv'):
            success = self.tm.add_comment("1", "user1", "Test comment")

        self.assertTrue(success)
        self.assertEqual(len(self.tm.task_comments["1"]), 1)
        self.assertEqual(self.tm.task_comments["1"][0].comment, "Test comment")

    def test_get_task_by_id(self):
        mock_task = MagicMock(spec=Task)
        self.tm.tasks["123"] = mock_task

        result = self.tm.get_task_by_id("123")
        self.assertEqual(result, mock_task)

    def test_get_user_assigned_tasks(self):
        task = MagicMock(spec=Task)
        self.tm.user_tasks["user1"] = [task]
        result = self.tm.get_user_assigned_tasks("user1")
        self.assertEqual(result, [task])


if __name__ == "__main__":
    unittest.main()
