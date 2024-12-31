import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def test_get_users(self):
        users = UserService.get_users()
        self.assertTrue(len(users) > 0)
        self.assertTrue(all(isinstance(user, dict) for user in users))

    def test_get_user_by_id(self):
        user = UserService.get_user_by_id(1)
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "john_doe")

    def test_create_user(self):
        new_user = UserService.create_user("test_user", "test@example.com")
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user["username"], "test_user")
        self.assertEqual(new_user["email"], "test@example.com")