import unittest
from Permissions import Permissions

class TestPermissions(unittest.TestCase):

    def test_enforce_create_project_manager(self):
        """Test that a Manager can create a project."""
        permissions = Permissions("Manager")
        try:
            permissions.enforce_create_project()  # This should not raise an exception
        except PermissionError:
            self.fail("PermissionError raised unexpectedly!")

    def test_enforce_create_project_employee(self):
        """Test that an Employee cannot create a project."""
        permissions = Permissions("Employee")
        with self.assertRaises(PermissionError):
            permissions.enforce_create_project()

    def test_enforce_update_project_manager(self):
        """Test that a Manager can update a project."""
        permissions = Permissions("Manager")
        try:
            permissions.enforce_update_project()  # This should not raise an exception
        except PermissionError:
            self.fail("PermissionError raised unexpectedly!")

    def test_enforce_update_project_employee(self):
        """Test that an Employee cannot update a project."""
        permissions = Permissions("Employee")
        with self.assertRaises(PermissionError):
            permissions.enforce_update_project()

    def test_enforce_view_project_manager(self):
        """Test that a Manager can view a project."""
        permissions = Permissions("Manager")
        try:
            permissions.enforce_view_project()  # This should not raise an exception
        except PermissionError:
            self.fail("PermissionError raised unexpectedly!")

    def test_enforce_view_project_employee(self):
        """Test that an Employee can view a project."""
        permissions = Permissions("Employee")
        try:
            permissions.enforce_view_project()  # This should not raise an exception
        except PermissionError:
            self.fail("PermissionError raised unexpectedly!")

    def test_enforce_view_project_guest(self):
        """Test that a Guest cannot view a project."""
        permissions = Permissions("Guest")
        with self.assertRaises(PermissionError):
            permissions.enforce_view_project()

if __name__ == "__main__":
    unittest.main()
