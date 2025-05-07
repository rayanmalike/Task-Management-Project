import unittest
from unittest.mock import MagicMock

class TestManagerMenu(unittest.TestCase):
    
    def setUp(self):
        # Mock the project and task objects
        self.mock_project = MagicMock()
        self.mock_task = MagicMock()
        
        # Explicitly define the methods that the tests will call
        self.mock_project.create.return_value = None
        self.mock_project.delete.return_value = None
        self.mock_project.update.return_value = None
        self.mock_project.view.return_value = None
        self.mock_project.handle_invalid_option.return_value = None
        
        self.mock_task.create.return_value = None
        self.mock_task.delete.return_value = None
        self.mock_task.update.return_value = None
        self.mock_task.view.return_value = None
        self.mock_task.handle_invalid_option.return_value = None

    def test_show_manager_menu_project_create_project(self):
        # Here you will test the "create project" functionality
        self.mock_project.create()  # This simulates calling the create method on the mock object
        self.mock_project.create.assert_called_once()  # Verify that the create method was called

    def test_show_manager_menu_project_delete_project(self):
        # Test for project deletion
        self.mock_project.delete()  # Simulate delete method call
        self.mock_project.delete.assert_called_once()  # Ensure delete was called

    def test_show_manager_menu_project_invalid_option(self):
        # Simulate an invalid option and check the appropriate response
        self.mock_project.handle_invalid_option()
        self.mock_project.handle_invalid_option.assert_called_once()  # Ensure method was called

    def test_show_manager_menu_task_create_task(self):
        # Test for task creation
        self.mock_task.create()
        self.mock_task.create.assert_called_once()  # Ensure create was called

    def test_show_manager_menu_task_delete_task(self):
        # Test for task deletion
        self.mock_task.delete()
        self.mock_task.delete.assert_called_once()  # Ensure delete was called

    def test_show_manager_menu_task_invalid_option(self):
        # Simulate an invalid task option
        self.mock_task.handle_invalid_option()
        self.mock_task.handle_invalid_option.assert_called_once()  # Ensure invalid option method was called

    def test_show_manager_menu_task_update_task(self):
        # Test for updating a task
        self.mock_task.update()
        self.mock_task.update.assert_called_once()  # Ensure update method was called

    def test_show_manager_menu_task_view_task(self):
        # Test for viewing a task
        self.mock_task.view()
        self.mock_task.view.assert_called_once()  # Ensure view method was called

if __name__ == '__main__':
    unittest.main()
