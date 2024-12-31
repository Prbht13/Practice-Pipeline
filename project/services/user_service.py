from .config import Config
from .logger import Logger

class UserService:
    _service_name = Config.USER_SERVICE_NAME
    _config = Config.get_service_config(_service_name)
    
    # Simulated database
    _users = [
        {"id": 1, "username": "john_doe", "email": "john@example.com"},
        {"id": 2, "username": "jane_doe", "email": "jane@example.com"}
    ]

    @classmethod
    def get_users(cls):
        Logger.log(cls._service_name, "Fetching all users")
        return cls._users

    @classmethod
    def get_user_by_id(cls, user_id):
        Logger.log(cls._service_name, f"Fetching user with id {user_id}")
        return next((user for user in cls._users if user["id"] == user_id), None)

    @classmethod
    def create_user(cls, username, email):
        new_user = {
            "id": len(cls._users) + 1,
            "username": username,
            "email": email
        }
        cls._users.append(new_user)
        Logger.log(cls._service_name, f"Created new user: {username}")
        return new_user