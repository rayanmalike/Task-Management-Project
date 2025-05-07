import unittest
from datetime import datetime
from project import Project

class TestProject(unittest.TestCase):

    def setUp(self):
        self.project = Project(title = "Test Title", description = "Test Description", due_date = datetime(2025, 11, 12), creator_id = 201)

    def test_initial_values(self):
        self.assertEqual(self.project.get_title(), "Test Title")
        self.assertEqual(self.project.get_description(), "Test Description")
        self.assertEqual(self.project.get_due_date(), datetime(2025, 11, 12))
        self.assertEqual(self.project.get_assigned_tasks(), {})
        self.assertEqual(self.project.get_creator(), 201)
        self.assertEqual(self.project.get_id(), None)

    def test_setters(self):
        self.project.set_description("Updated Description")
        self.assertEqual(self.project.get_description(), "Updated Description")
        
        self.project.set_due_date(datetime(2025, 12, 12))
        self.assertEqual(self.project.get_due_date(), datetime(2025, 12, 12))

        self.project.set_due_date(datetime(2025, 12, 12))
        self.assertEqual(self.project.get_due_date(), datetime(2025, 12, 12))

        self.project.set_due_date(datetime(2025, 12, 12))
        self.assertEqual(self.project.get_due_date(), datetime(2025, 12, 12))

    def test_string_representation(self):
        self.project.set_id(12)
        expected_substring = "Project 12: Test Title | Due: 2025-11-12 00:00:00 | Tasks: No tasks added yet."
        self.assertIn(expected_substring, str(self.project))

if __name__ == '__main__':
     unittest.main()