import unittest
from services.auth_service import AuthService

class TestAuthService(unittest.TestCase):
    def test_login_success(self):
        result = AuthService.login("test_user", "password")
        self.assertTrue(result["success"])
        self.assertIn("token", result)

    def test_login_failure(self):
        result = AuthService.login(None, None)
        self.assertFalse(result["success"])

    def test_validate_token(self):
        self.assertTrue(AuthService.validate_token("dummy_token_test"))
        self.assertFalse(AuthService.validate_token("invalid_token"))