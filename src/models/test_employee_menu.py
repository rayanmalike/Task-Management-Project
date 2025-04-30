import unittest
from datetime import datetime
from employee import Employee
from task import Task
from project import Project
from task_controller import TaskManager
from project_controller import ProjectManager

class TestEmployeeMenu(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(1, "Test User", "test@email.com", "password123", "employee")
        self.task_manager = TaskManager.get_instance()
        self.project_manager = ProjectManager.get_instance()
        
        # Create a test task
        self.test_task = Task("Test Task", "Test Description", 
                            datetime(2025, 5, 1), 1, 2)
        self.test_task.set_id("T123")
        
    def test_display_tasks(self):
        # Add task to employee's assigned tasks
        self.employee.assigned_tasks[self.test_task.get_id()] = self.test_task
        
        # Test that employee has the assigned task
        self.assertIn(self.test_task.get_id(), self.employee.get_assigned_tasks())
        
    def test_track_task_status(self):
        # Add task and test status
        self.task_manager.tasks[self.test_task.get_id()] = self.test_task
        task = self.task_manager.get_task_by_id(self.test_task.get_id())
        self.assertEqual(task.get_status(), "PENDING")
        
    def test_submit_task(self):
        # Test task completion
        self.task_manager.tasks[self.test_task.get_id()] = self.test_task
        self.task_manager.mark_task_as_completed(self.test_task)
        self.assertEqual(self.test_task.get_status(), "COMPLETED")

if __name__ == '__main__':
    unittest.main()

# cd src / models
# python -m unittest -v test_employee_menu