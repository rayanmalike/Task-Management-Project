import unittest
from unittest.mock import patch, mock_open
from project import Project
from task import Task
from project_controller import ProjectManager
from datetime import datetime

class TestProjectManager(unittest.TestCase):

    def setUp(self):
        self.manager = ProjectManager.get_instance()

    @patch("builtins.open", new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        mock_file.return_value.read.side_effect = ["",]

        task = Task(title="Test Title",description="Initial Description",due_date=datetime(2025, 5, 1),assigned_user=101,creator=201)
        task.set_id(1)
        project = Project(title = "Test Title", description = "Test Description", due_date = datetime(2025, 11, 12), creator_id = 201)
        project.set_id(12)

        self.manager.create_project(project)

        self.manager.add_task_to_project(project, task)

        self.manager.delete_task_from_project(project, task)

        self.manager.delete_project(project)

        mock_file.assert_called_with("projects.csv", "w", newline="")
        handle = mock_file()
        handle.write.assert_called()

# if __name__ == "__main__":
#     unittest.main()