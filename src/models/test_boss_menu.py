import unittest
import os
import sys
import io
from user_manager_dict import UserManager
from user_controller import UserController

class TestBossMenuFull(unittest.TestCase):
    def setUp(self):
        self.test_csv = "test_boss_menu_users.csv"
        self.uc = UserController.get_instance()
        self.manager = UserManager(self.test_csv)

        # Clean and prepare test file
        with open(self.test_csv, 'w') as f:
            f.write("")

        # Capture stdout
        self._stdout = sys.stdout
        sys.stdout = self._log_output = io.StringIO()

        # Setup test users
        self.manager.register_user("boss", "pw", "boss", "boss@email.com", "IDB1")
        self.manager.register_user("manager", "pw", "manager", "mgr@email.com", "IDM1")
        self.manager.register_user("employee", "pw", "employee", "emp@email.com", "IDE1")

    def tearDown(self):
        sys.stdout = self._stdout
        print(self._log_output.getvalue())

        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_display_users(self):
        self.manager.display_users()
        output = self._log_output.getvalue()
        self.assertIn("boss", output)
        self.assertIn("manager", output)
        self.assertIn("employee", output)

    def test_register_and_promote_demote_user(self):
        self.manager.register_user("testuser", "pw", "employee", "test@email.com", "IDT1")
        self.assertEqual(self.manager.get_user_role("testuser"), "employee")
        self.manager.update_role("testuser", "manager")
        self.assertEqual(self.manager.get_user_role("testuser"), "manager")
        self.manager.update_role("testuser", "employee")
        self.assertEqual(self.manager.get_user_role("testuser"), "employee")

    def test_reset_password_for_roles(self):
        self.assertTrue(self.manager.reset_password("manager", "newpw1"))
        hashed1 = self.manager.hash_password("newpw1")
        self.assertEqual(self.manager.users_dict["manager"]["password"], hashed1)

        self.assertTrue(self.manager.reset_password("employee", "newpw2"))
        hashed2 = self.manager.hash_password("newpw2")
        self.assertEqual(self.manager.users_dict["employee"]["password"], hashed2)

        self.assertTrue(self.manager.reset_password("boss", "newpw3"))
        hashed3 = self.manager.hash_password("newpw3")
        self.assertEqual(self.manager.users_dict["boss"]["password"], hashed3)

    def test_delete_user(self):
        self.assertIn("employee", self.manager.users_dict)
        self.manager.delete_user("employee")
        self.assertNotIn("employee", self.manager.users_dict)

    def test_fail_invalid_promote(self):
        result = self.manager.update_role("nonexistent", "manager")
        self.assertFalse(result)

    def test_fail_reset_wrong_user(self):
        result = self.manager.reset_password("ghost", "pw")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()