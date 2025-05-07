import unittest
from unittest.mock import patch, MagicMock
from task_controller import TaskManager
from project_controller import ProjectManager
from task import Task
from employee import Employee  # Assuming you have an Employee class
from employee_menu import show_employee_menu  # Adjust path if needed

class TestEmployeeMenu(unittest.TestCase):

    def setUp(self):
        # Setup mock employee
        self.employee = MagicMock()
        self.employee.get_username.return_value = "Employee1"
        self.employee.get_user_id.return_value = "3"
        self.employee.display_tasks = MagicMock()

        # Mock singletons
        self.task_manager = TaskManager.get_instance()
        self.project_manager = ProjectManager.get_instance()

        # Patch task_manager and project_manager methods
        self.task_manager.get_task_by_id = MagicMock()
        self.task_manager.get_user_assigned_tasks = MagicMock()
        self.task_manager.get_task_comments = MagicMock()
        self.task_manager.mark_task_as_completed = MagicMock()
        self.task_manager.add_comment = MagicMock()

        self.project_manager.get_project_by_id = MagicMock()

    @patch('builtins.input', side_effect=['1', '7'])
    def test_view_tasks_and_logout(self, mock_input):
        show_employee_menu(self.employee)
        self.employee.display_tasks.assert_called_once()

    @patch('builtins.input', side_effect=['2', '123', '7'])
    def test_track_task_status(self, mock_input):
        task = MagicMock()
        task.get_status.return_value = 'IN_PROGRESS'
        task.get_assigned_user.return_value = '3'  # Ensure the task is assigned to employee '3'
        self.task_manager.get_task_by_id.return_value = task

        show_employee_menu(self.employee)

        print(f"Called get_task_by_id: {self.task_manager.get_task_by_id.called}")  # Debugging line
        print(f"Called get_status: {task.get_status.called}")  # Debugging line

        self.task_manager.get_task_by_id.assert_called_with('123')
        task.get_status.assert_called_once()

    @patch('builtins.input', side_effect=['3', '123', '7'])
    def test_submit_task_completion(self, mock_input):
        task = MagicMock()
        self.task_manager.get_task_by_id.return_value = task
        show_employee_menu(self.employee)
        self.task_manager.mark_task_as_completed.assert_called_with(task)

    @patch('builtins.input', side_effect=['4', '101', 'This is a comment', '7'])
    def test_add_comment_to_task(self, mock_input):
        self.task_manager.add_comment.return_value = True
        show_employee_menu(self.employee)
        self.task_manager.add_comment.assert_called_with('101', '3', 'This is a comment')

    @patch('builtins.input', side_effect=['5', '7'])
    def test_view_task_comments(self, mock_input):
        task1 = MagicMock()
        task1.get_id.return_value = 1
        self.task_manager.get_user_assigned_tasks.return_value = [task1]
        mock_comment = MagicMock()
        mock_comment.timestamp = "2025-05-05 10:00:00"
        mock_comment.user_id = 2
        mock_comment.comment = "Please submit"
        self.task_manager.get_task_comments.return_value = [mock_comment]

        show_employee_menu(self.employee)
        self.task_manager.get_user_assigned_tasks.assert_called_with("3")

    @patch('builtins.input', side_effect=['6', 'P123', '7'])
    def test_view_project_details(self, mock_input):
        project = MagicMock()
        project.get_id.return_value = "P123"
        project.get_title.return_value = "Project Alpha"
        project.get_description.return_value = "A test project"
        project.get_due_date.return_value = "2025-06-01"
        task = MagicMock()
        task.get_id.return_value = "T001"
        task.get_title.return_value = "Sample Task"
        task.get_status.return_value = "NEW"
        task.get_due_date.return_value = "2025-06-01"
        project.get_assigned_tasks.return_value = {"T001": task}
        self.project_manager.get_project_by_id.return_value = project

        show_employee_menu(self.employee)
        self.project_manager.get_project_by_id.assert_called_with("P123")

if __name__ == '__main__':
    unittest.main()
