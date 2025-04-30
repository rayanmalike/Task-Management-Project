import unittest
import os
from unittest.mock import patch, MagicMock
from user_manager_dict import UserManager
import boss_menu  
class TestBossMenuIntegration(unittest.TestCase):
    
    def setUp(self):
        self.test_csv = 'test_users.csv'
        # Ensure the test file is clean before each test
        with open(self.test_csv, 'w') as f:
            f.write('')
        self.manager = UserManager(self.test_csv)

        # Create a dummy boss account to allow boss_menu to function
        self.manager.register_user('boss_user', 'boss_pass', 'boss', 'boss@example.com', 'BOSS001')

        # Replace UserController with a mock (to prevent errors from other parts of the app)
        self.user_controller_patch = patch('boss_menu.UserController')
        self.mock_user_controller_class = self.user_controller_patch.start()
        self.mock_user_controller_instance = MagicMock()
        self.mock_user_controller_class.get_instance.return_value = self.mock_user_controller_instance

    # def tearDown(self):
    #     # Clean up the test file
    #     if os.path.exists(self.test_csv):
    #         os.remove(self.test_csv)
    #     self.user_controller_patch.stop()

    @patch('boss_menu.input', side_effect=[
        '2',  # Add new account
        'new_user', 'new_pass', 'new@example.com', 'manager', 'MGR001',
        '8'  # Logout
    ])
    def test_add_user_writes_to_csv(self, mock_input):
        boss_menu.show_boss_menu('boss_user', self.manager)

        # Reload the manager to verify file change
        new_manager = UserManager(self.test_csv)
        self.assertTrue('new_user' in new_manager.users_dict)
        self.assertEqual(new_manager.users_dict['new_user']['role'], 'manager')

    @patch('boss_menu.input', side_effect=[
        '6',  # Delete user
        'delete_user', 'EMP001', 'yes',
        '8'
    ])
    def test_delete_user_removes_from_csv(self, mock_input):
        # Pre-add a user to delete
        self.manager.register_user('delete_user', 'pass123', 'employee', 'del@example.com', 'EMP001')

        # Simulate role checking and controller delete calls
        self.manager.get_user_role = lambda username: 'employee'

        boss_menu.show_boss_menu('boss_user', self.manager)

        # Reload and assert user is deleted
        new_manager = UserManager(self.test_csv)
        self.assertNotIn('delete_user', new_manager.users_dict)

    @patch('boss_menu.input', side_effect=[
        '5',  # Update user info
        'update_user', 'updated_user', 'updated@example.com',
        '8'
    ])
    def test_update_user_info_in_csv(self, mock_input):
        self.manager.register_user('update_user', 'pass', 'employee', 'old@example.com', 'EMP123')
        self.manager.user_exists = lambda username: username == 'update_user'

        boss_menu.show_boss_menu('boss_user', self.manager)

        # Reload and verify updated data
        new_manager = UserManager(self.test_csv)
        self.assertIn('updated_user', new_manager.users_dict)
        self.assertEqual(new_manager.users_dict['updated_user']['email'], 'updated@example.com')

# if __name__ == '__main__':
#     unittest.main()

# cd src/models
# python -m unittest -v test_boss_menu