from .config import Config
from .logger import Logger

class AuthService:
    _service_name = Config.AUTH_SERVICE_NAME
    _config = Config.get_service_config(_service_name)

    @classmethod
    def login(cls, username, password):
        Logger.log(cls._service_name, f"Login attempt for user: {username}")
        if username and password:
            return {
                "success": True,
                "token": f"dummy_token_{username}",
                "message": "Login successful"
            }
        Logger.log(cls._service_name, "Login failed - invalid credentials", "ERROR")
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    @classmethod
    def validate_token(cls, token):
        is_valid = token and token.startswith("dummy_token_")
        Logger.log(
            cls._service_name, 
            f"Token validation {'successful' if is_valid else 'failed'}"
        )
        return is_valid