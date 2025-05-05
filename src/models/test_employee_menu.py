import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
from employee import Employee
from task import Task

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.test_task_id = "1"  # match Task_ID in CSV
    
    @patch("builtins.open", new_callable=mock_open, read_data="Task_ID,Title,Description,Due_Date,Assigned_User_ID,Creator_ID,Status,Priority\n1,Test Task,This is a test task,2025-05-01T12:00:00,1,1,PENDING,UNDEFINED")
    @patch("builtins.print")  # Mock print function to capture printed output
    def test_display_tasks(self, mock_print, mock_file):
        employee = Employee(1, "John Doe", "john@example.com", "password", "employee")
        employee.display_tasks()

        print_calls = [call[0][0] for call in mock_print.call_args_list]

        self.assertIn("\nTask 1: Test Task", print_calls)
        self.assertIn("Description: This is a test task", print_calls)
        self.assertIn("Due Date: 2025-05-01 12:00:00", print_calls)
        self.assertIn("Status: PENDING", print_calls)
        self.assertIn("Priority: UNDEFINED", print_calls)

        # Cleanup
        if self.test_task_id in employee.assigned_tasks:
            del employee.assigned_tasks[self.test_task_id]

    @patch("builtins.open", new_callable=mock_open, read_data="Task_ID,Title,Description,Due_Date,Assigned_User_ID,Creator_ID,Status,Priority\n1,Test Task,This is a test task,2025-05-01T12:00:00,1,1,PENDING,UNDEFINED")
    def test_initialize_employee_with_tasks(self, mock_file):
        employee = Employee(1, "John Doe", "john@example.com", "password", "employee")
        tasks = employee.get_assigned_tasks()

        task = tasks[self.test_task_id]
        self.assertEqual(task.get_title(), "Test Task")
        self.assertEqual(task.get_description(), "This is a test task")
        self.assertEqual(task.get_due_date(), datetime(2025, 5, 1, 12, 0, 0))
        self.assertEqual(task.get_status(), "PENDING")
        self.assertEqual(task.get_priority(), "UNDEFINED")

        # Cleanup
        if self.test_task_id in tasks:
            del tasks[self.test_task_id]

# if __name__ == "__main__":
#     unittest.main()


# cd src/models
# python -m unittest -v test_employee_menu