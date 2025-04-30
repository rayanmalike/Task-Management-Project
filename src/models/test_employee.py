import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
from employee import Employee
from task import Task

class TestEmployee(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data="Task_ID,Title,Description,Due_Date,Assigned_User_ID,Creator_ID,Status,Priority\n1,Test Task,This is a test task,2025-05-01T12:00:00,1,1,PENDING,UNDEFINED")
    @patch("builtins.print")  # Mock print function to capture printed output
    def test_display_tasks(self, mock_print, mock_file):
        # Initialize the employee
        employee = Employee(1, "John Doe", "john@example.com", "password", "employee")
        
        # Call the method that should print the task details
        employee.display_tasks()
        
        # Check if print was called with the correct task details
        print_calls = [call[0][0] for call in mock_print.call_args_list]  # Extract all printed arguments
        
        # Check if the expected task details were printed
        self.assertIn("\nTask 1: Test Task", print_calls)  # Including \n at the beginning
        self.assertIn("Description: This is a test task", print_calls)
        self.assertIn("Due Date: 2025-05-01 12:00:00", print_calls)
        self.assertIn("Status: PENDING", print_calls)
        self.assertIn("Priority: UNDEFINED", print_calls)

    @patch("builtins.open", new_callable=mock_open, read_data="Task_ID,Title,Description,Due_Date,Assigned_User_ID,Creator_ID,Status,Priority\n1,Test Task,This is a test task,2025-05-01T12:00:00,1,1,PENDING,UNDEFINED")
    def test_initialize_employee_with_tasks(self, mock_file):
        # Initialize the employee
        employee = Employee(1, "John Doe", "john@example.com", "password", "employee")
        
        # Get the assigned tasks
        tasks = employee.get_assigned_tasks()
        
        # Ensure the task is loaded correctly
        task = tasks[1]  # Now using integer task ID
        self.assertEqual(task.get_title(), "Test Task")
        self.assertEqual(task.get_description(), "This is a test task")
        self.assertEqual(task.get_due_date(), datetime(2025, 5, 1, 12, 0, 0))
        self.assertEqual(task.get_status(), "PENDING")  # Default status
        self.assertEqual(task.get_priority(), "UNDEFINED")  # Default priority

# if __name__ == "__main__":
#     unittest.main()

# cd src/models
# python -m unittest -v  test_employee.py