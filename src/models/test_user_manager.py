import unittest
import os
from user_manager_dict import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.test_csv = "test_users_temp.csv"
        with open(self.test_csv, 'w') as f:
            f.write("")
        self.manager = UserManager(self.test_csv)

    def tearDown(self):
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_register_and_get_role(self):
        self.manager.register_user("Alice", "pw", "employee", "alice@example.com", "A001")
        self.assertIn("Alice", self.manager.users_dict)
        self.assertEqual(self.manager.get_user_role("Alice"), "employee")

    def test_delete_user(self):
        self.manager.register_user("Frank", "pw", "manager", "frank@example.com", "F001")
        self.assertIn("Frank", self.manager.users_dict)
        deleted = self.manager.delete_user("Frank")
        self.assertTrue(deleted)
        self.assertNotIn("Frank", self.manager.users_dict)

    def test_password_is_hashed(self):
        self.manager.register_user("Bob", "plainpw", "manager", "bob@example.com", "B001")
        stored = self.manager.users_dict["Bob"]["password"]
        self.assertNotEqual(stored, "plainpw")  # Should be hashed
        self.assertEqual(stored, self.manager.hash_password("plainpw"))

    def test_reset_password(self):
        self.manager.register_user("Dave", "pw", "employee", "dave@example.com", "D001")
        new_password = "newpw"
        self.manager.reset_password("Dave", new_password)
        expected_hash = self.manager.hash_password(new_password)
        self.assertEqual(self.manager.users_dict["Dave"]["password"], expected_hash)

    def test_update_role(self):
        self.manager.register_user("Eve", "pw", "employee", "eve@example.com", "E001")
        updated = self.manager.update_role("Eve", "manager")
        self.assertTrue(updated)
        self.assertEqual(self.manager.get_user_role("Eve"), "manager")

    def test_get_user_role_not_found(self):
        self.assertIsNone(self.manager.get_user_role("Ghost"))

    def test_delete_nonexistent_user(self):
        self.assertFalse(self.manager.delete_user("No_one"))

# if __name__ == '__main__':
#     unittest.main()

# cd src/models
# python -m unittest -v test_user_manager