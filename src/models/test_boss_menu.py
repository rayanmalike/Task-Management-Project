import unittest
import os
import sys
import io
from user_manager_dict import UserManager

class TestBossMenuRoleSwap(unittest.TestCase):
    def setUp(self):
        self.test_csv = "test_users_role_swap.csv"
        with open(self.test_csv, 'w') as f:
            f.write("")
        self.manager = UserManager(self.test_csv)

        # Redirect stdout to capture printed logs
        self._stdout = sys.stdout
        sys.stdout = self._log_output = io.StringIO()

        # Initial users
        self.manager.register_user("boss_user", "pw", "boss", "boss@example.com", "B001")
        self.manager.register_user("manager_user", "pw", "manager", "manager@example.com", "M001")
        self.manager.register_user("employee_user", "pw", "employee", "employee@example.com", "E001")
        self.manager.register_user("test_user", "pw123", "employee", "test@example.com", "T001")

    def tearDown(self):
        # Restore stdout and print captured logs
        sys.stdout = self._stdout
        print(self._log_output.getvalue())
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_user_presence(self):
        self.assertIn("test_user", self.manager.users_dict)
        self.assertEqual(self.manager.get_user_role("test_user"), "employee")

    def test_reset_passwords(self):
        self.assertTrue(self.manager.reset_password("employee_user", "newpass1"))
        new_hash = self.manager.hash_password("newpass1")
        self.assertEqual(self.manager.users_dict["employee_user"]["password"], new_hash)

        self.assertTrue(self.manager.reset_password("manager_user", "newpass2"))
        new_hash = self.manager.hash_password("newpass2")
        self.assertEqual(self.manager.users_dict["manager_user"]["password"], new_hash)

    def test_delete_user(self):
        self.assertIn("test_user", self.manager.users_dict)
        deleted = self.manager.delete_user("test_user")
        self.assertTrue(deleted)
        self.assertNotIn("test_user", self.manager.users_dict)

    def test_role_swap_and_revert(self):
        self.assertEqual(self.manager.get_user_role("manager_user"), "manager")
        self.assertEqual(self.manager.get_user_role("employee_user"), "employee")

        # Swap
        self.assertTrue(self.manager.update_role("manager_user", "employee"))
        self.assertEqual(self.manager.get_user_role("manager_user"), "employee")

        self.assertTrue(self.manager.update_role("employee_user", "manager"))
        self.assertEqual(self.manager.get_user_role("employee_user"), "manager")

        # Revert
        self.assertTrue(self.manager.update_role("manager_user", "manager"))
        self.assertEqual(self.manager.get_user_role("manager_user"), "manager")

        self.assertTrue(self.manager.update_role("employee_user", "employee"))
        self.assertEqual(self.manager.get_user_role("employee_user"), "employee")

        print("Logging out...")  # Final logout simulation

# if __name__ == '__main__':
#     unittest.main()

# cd src/models
# python -m unittest -v test_boss_menu