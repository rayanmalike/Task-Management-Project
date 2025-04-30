import unittest
from unittest.mock import patch, MagicMock
from user_controller import UserController
from employee import Employee
from manager import Manager

class TestUserController(unittest.TestCase):

    def setUp(self):
        """Set up the UserController instance before each test."""
        self.controller = UserController.get_instance()

    @patch("builtins.open", new_callable=MagicMock)
    @patch("csv.writer", new_callable=MagicMock)
    def test_create_employee(self, mock_csv_writer, mock_file):
        """Test creating an employee."""
        # Mock the file write functionality
        mock_file.return_value.write = MagicMock()
        
        # Mock the CSV writer functionality to avoid actual file writing
        mock_writer = MagicMock()
        mock_csv_writer.return_value = mock_writer

        # Create an employee
        employee = self.controller.create_employee(1, "John Doe", "john@example.com", "password123")
        
        # Check if the employee is added to the in-memory dictionary
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.get_user_id(), 1)
        self.assertEqual(employee.get_username(), "John Doe")
        
        # Check if the file was saved
        mock_file.assert_called_with("employees.csv", "w", newline="")
        mock_writer.writerow.assert_called()

    @patch("builtins.open", new_callable=MagicMock)
    @patch("csv.writer", new_callable=MagicMock)
    def test_create_manager(self, mock_csv_writer, mock_file):
        """Test creating a manager."""
        # Mock the file write functionality
        mock_file.return_value.write = MagicMock()
        
        # Mock the CSV writer functionality to avoid actual file writing
        mock_writer = MagicMock()
        mock_csv_writer.return_value = mock_writer

        # Create a manager
        manager = self.controller.create_manager(1, "Jane Smith", "jane@example.com", "password123")
        
        # Check if the manager is added to the in-memory dictionary
        self.assertIsInstance(manager, Manager)
        self.assertEqual(manager.get_user_id(), 1)
        self.assertEqual(manager.get_username(), "Jane Smith")
        
        # Check if the file was saved
        mock_file.assert_called_with("managers.csv", "w", newline="")
        mock_writer.writerow.assert_called()

    @patch("builtins.open", new_callable=MagicMock)
    @patch("csv.writer", new_callable=MagicMock)
    def test_update_employee_password(self, mock_csv_writer, mock_file):
        """Test updating an employee's password."""
        # Mock the file write functionality
        mock_file.return_value.write = MagicMock()
        
        # Mock the CSV writer functionality to avoid actual file writing
        mock_writer = MagicMock()
        mock_csv_writer.return_value = mock_writer

        # Create an employee
        self.controller.create_employee(1, "John Doe", "john@example.com", "password123")
        
        # Update employee password
        success = self.controller.update_password(1, "newpassword123")
        
        # Check if the password was updated
        employee = self.controller.get_employee(1)
        self.assertTrue(success)
        self.assertEqual(employee.get_password(), "newpassword123")
        
        # Check if the file was saved after the update
        mock_file.assert_called_with("employees.csv", "w", newline="")
        mock_writer.writerow.assert_called()

    @patch("builtins.open", new_callable=MagicMock)
    @patch("csv.writer", new_callable=MagicMock)
    def test_update_manager_password(self, mock_csv_writer, mock_file):
        """Test updating a manager's password."""
        # Mock the file write functionality
        mock_file.return_value.write = MagicMock()
        
        # Mock the CSV writer functionality to avoid actual file writing
        mock_writer = MagicMock()
        mock_csv_writer.return_value = mock_writer

        # Create a manager
        self.controller.create_manager(1, "Jane Smith", "jane@example.com", "password123")
        
        # Update manager password
        success = self.controller.update_password(1, "newpassword123", is_manager=True)
        
        # Check if the password was updated
        manager = self.controller.get_manager(1)
        self.assertTrue(success)
        self.assertEqual(manager.get_password(), "newpassword123")
        
        # Check if the file was saved after the update
        mock_file.assert_called_with("managers.csv", "w", newline="")
        mock_writer.writerow.assert_called()

# if __name__ == "__main__":
#     unittest.main()
