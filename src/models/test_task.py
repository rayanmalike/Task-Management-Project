import unittest
from datetime import datetime
from task import Task, TaskComment

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task(
            title="Test Task",
            description="Initial description",
            due_date=datetime(2025, 5, 1),
            assigned_user=101,
            creator=201
        )

    def test_initial_values(self):
        self.assertEqual(self.task.get_title(), "Test Task")
        self.assertEqual(self.task.get_description(), "Initial description")
        self.assertEqual(self.task.get_due_date(), datetime(2025, 5, 1))
        self.assertEqual(self.task.get_priority(), "UNDEFINED")
        self.assertEqual(self.task.get_status(), "PENDING")
        self.assertEqual(self.task.get_assigned_user(), 101)
        self.assertEqual(self.task.get_creator_id(), 201)

    def test_setters_and_timestamps(self):
        old_update = self.task.get_updated_at()

        # Wait a little to ensure timestamp difference
        self.task.set_title("Updated Task")
        self.assertEqual(self.task.get_title(), "Updated Task")
        self.assertGreater(self.task.get_updated_at(), old_update)

        self.task.set_description("New Description")
        self.assertEqual(self.task.get_description(), "New Description")

        new_due = datetime(2025, 6, 1)
        self.task.set_due_date(new_due)
        self.assertEqual(self.task.get_due_date(), new_due)

        self.task.set_priority("HIGH")
        self.assertEqual(self.task.get_priority(), "HIGH")

        self.task.set_status("COMPLETED")
        self.assertEqual(self.task.get_status(), "COMPLETED")

        self.task.set_assigned_user(202)
        self.assertEqual(self.task.get_assigned_user(), 202)

        self.task.set_creator(303)
        self.assertEqual(self.task.get_creator_id(), 303)

    def test_set_invalid_priority_or_status(self):
        self.task.set_priority("INVALID")  # Should stay UNDEFINED
        self.assertNotEqual(self.task.get_priority(), "INVALID")

        self.task.set_status("UNKNOWN")  # Should stay as last valid
        self.assertNotEqual(self.task.get_status(), "UNKNOWN")

    def test_string_representation(self):
        self.task.set_id(42)
        expected_substring = "ID: 42 | Title: Test Task | Status: [PENDING]"
        self.assertIn(expected_substring, str(self.task))

class TestTaskComment(unittest.TestCase):

    def test_comment_to_dict_and_str(self):
        timestamp = datetime(2025, 4, 30, 14, 30)
        comment = TaskComment(1, 999, "Looks good!", timestamp)

        comment_dict = comment.to_dict()
        self.assertEqual(comment_dict["task_id"], 1)
        self.assertEqual(comment_dict["user_id"], 999)
        self.assertEqual(comment_dict["comment"], "Looks good!")
        self.assertEqual(comment_dict["timestamp"], "2025-04-30 14:30:00")

        expected_str = "[2025-04-30 14:30:00] User 999: Looks good!"
        self.assertEqual(str(comment), expected_str)

if __name__ == '__main__':
    unittest.main(verbosity=2)

# cd src/models
# python -m unittest -v test_task