import unittest
from unittest.mock import patch, MagicMock
from employee_menu import show_employee_menu
from task_controller import TaskManager
from project_controller import ProjectManager
from employee import Employee
from task import Task
from project import Project

class TestShowEmployeeMenu(unittest.TestCase):

    def setUp(self):
        # Create a mock employee
        self.mock_employee = MagicMock(spec=Employee)
        self.mock_employee.get_username.return_value = "johndoe"
        self.mock_employee.get_user_id.return_value = "E001"
        self.mock_employee.display_tasks.return_value = None

        # Set up TaskManager singleton with mocked methods
        self.task_manager = TaskManager.get_instance()
        self.task_manager.get_task_by_id = MagicMock()
        self.task_manager.add_comment = MagicMock(return_value=True)
        self.task_manager.mark_task_as_completed = MagicMock()
        self.task_manager.get_task_comments = MagicMock()
        self.task_manager.get_user_assigned_tasks = MagicMock()

        # Set up ProjectManager singleton
        self.project_manager = ProjectManager.get_instance()
        self.project_manager.get_project_by_id = MagicMock()

    @patch('builtins.input', side_effect=['1', '7'])  # View My Tasks, then Logout
    def test_view_tasks_and_logout(self, mock_input):
        result = show_employee_menu(self.mock_employee)
        self.assertFalse(result)
        self.mock_employee.display_tasks.assert_called_once()

    @patch('builtins.input', side_effect=['2', 'T001', '7'])  # Track Task Status
    def test_track_task_status(self, mock_input):
        mock_task = MagicMock(spec=Task)
        mock_task.get_status.return_value = "In Progress"
        self.task_manager.get_task_by_id.return_value = mock_task

        result = show_employee_menu(self.mock_employee)
        self.task_manager.get_task_by_id.assert_called_with('T001')
        mock_task.get_status.assert_called_once()
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['3', 'T002', '7'])  # Submit task
    def test_submit_task_completion(self, mock_input):
        mock_task = MagicMock(spec=Task)
        self.task_manager.get_task_by_id.return_value = mock_task

        result = show_employee_menu(self.mock_employee)
        self.task_manager.mark_task_as_completed.assert_called_with(mock_task)
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['4', 'T003', 'Great job!', '7'])  # Add comment
    def test_add_comment_to_task(self, mock_input):
        result = show_employee_menu(self.mock_employee)
        self.task_manager.add_comment.assert_called_with('T003', 'E001', 'Great job!')
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['5', '7'])  # View task comments
    def test_view_task_comments(self, mock_input):
        mock_task = MagicMock(spec=Task)
        mock_task.get_id.return_value = "T004"
        self.task_manager.get_user_assigned_tasks.return_value = [mock_task]

        result = show_employee_menu(self.mock_employee)
        self.task_manager.get_task_comments.assert_called_with("T004")
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['6', 'P001', '7'])  # View project details
    def test_view_project_details(self, mock_input):
        mock_project = MagicMock(spec=Project)
        mock_project.get_id.return_value = 'P001'
        mock_project.get_title.return_value = 'Test Project'
        mock_project.get_description.return_value = 'Sample'
        mock_project.get_due_date.return_value = '2024-12-31'
        mock_project.get_assigned_tasks.return_value = {}

        self.project_manager.get_project_by_id.return_value = mock_project

        result = show_employee_menu(self.mock_employee)
        self.project_manager.get_project_by_id.assert_called_with('P001')
        self.assertFalse(result)


# if __name__ == '__main__':
#     unittest.main()
