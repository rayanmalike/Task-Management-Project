import unittest
import os
from user_manager_dict import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'test_users.csv'
        self.manager = UserManager(self.test_filename)


        with open(self.test_filename, 'w') as f:
            f.write('')

    def tearDown(self):

        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_register_user_success(self):
        result = self.manager.register_user("an123", "pass123", "employee", "an@example.com", "001")
        self.assertTrue(result)
        self.assertIn("an123", self.manager.users_dict)

    def test_register_user_duplicate(self):
        self.manager.register_user("an123", "pass123", "employee", "an@example.com", "001")
        result = self.manager.register_user("an123", "pass456", "manager", "an2@example.com", "002")
        self.assertFalse(result)

    def test_verify_login(self):
        self.manager.register_user("an123", "pass123", "employee", "an@example.com", "001")
        self.assertTrue(self.manager.verify_login("an123", "pass123"))
        self.assertFalse(self.manager.verify_login("an123", "wrongpass"))

    def test_reset_password(self):
        self.manager.register_user("an123", "oldpass", "employee", "an@example.com", "001")
        self.assertTrue(self.manager.reset_password("an123", "newpass"))
        self.assertTrue(self.manager.verify_login("an123", "newpass"))

    def test_delete_user(self):
        self.manager.register_user("an123", "pass123", "employee", "an@example.com", "001")
        self.assertTrue(self.manager.delete_user("an123"))
        self.assertFalse(self.manager.user_exists("an123"))

    def test_update_role(self):
        self.manager.register_user("an123", "pass123", "employee", "an@example.com", "001")
        self.assertTrue(self.manager.update_role("an123", "manager"))
        self.assertEqual(self.manager.get_user_role("an123"), "manager")

# if __name__ == '__main__':
#     unittest.main()