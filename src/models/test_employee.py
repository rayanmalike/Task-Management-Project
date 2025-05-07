import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from employee import Employee
from task import Task


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee(1, "Alice", "alice@example.com", "password", "employee")

    @patch('task_controller.TaskManager.get_instance')
    def test_get_assigned_tasks_returns_tasks(self, mock_get_instance):
        # Create a mock Task object
        mock_task = Task(
            title="Test Task",
            description="Do something",
            due_date=datetime(2025, 5, 10),
            assigned_user=1,
            creator=2
        )
        mock_task.set_id(101)
        mock_task.set_status("PENDING")
        mock_task.set_priority("HIGH")

        mock_manager = MagicMock()
        mock_manager.get_user_assigned_tasks.return_value = [mock_task]
        mock_get_instance.return_value = mock_manager

        tasks = self.employee.get_assigned_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].get_title(), "Test Task")
        self.assertEqual(tasks[0].get_assigned_user(), 1)

    @patch('task_controller.TaskManager.get_instance')
    def test_get_assigned_tasks_returns_empty_list(self, mock_get_instance):
        mock_manager = MagicMock()
        mock_manager.get_user_assigned_tasks.return_value = None
        mock_get_instance.return_value = mock_manager

        tasks = self.employee.get_assigned_tasks()

        self.assertEqual(tasks, [])

    @patch('task_controller.TaskManager.get_instance')
    def test_display_tasks_with_tasks(self, mock_get_instance):
        task = Task(
            title="Finish Report",
            description="Complete the financial report",
            due_date=datetime(2025, 6, 1),
            assigned_user=1,
            creator=99
        )
        task.set_id(102)
        task.set_status("IN PROGRESS")
        task.set_priority("MEDIUM")

        mock_manager = MagicMock()
        mock_manager.get_user_assigned_tasks.return_value = [task]
        mock_get_instance.return_value = mock_manager

        with patch('builtins.print') as mock_print:
            self.employee.display_tasks()

        mock_print.assert_any_call(f"\nTasks assigned to {self.employee.username}:")
        mock_print.assert_any_call(f"\nTask 102: Finish Report")

    @patch('task_controller.TaskManager.get_instance')
    def test_display_tasks_no_tasks(self, mock_get_instance):
        mock_manager = MagicMock()
        mock_manager.get_user_assigned_tasks.return_value = []
        mock_get_instance.return_value = mock_manager

        with patch('builtins.print') as mock_print:
            self.employee.display_tasks()

        mock_print.assert_called_with(f"No tasks assigned to {self.employee.username}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
