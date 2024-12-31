from services.user_service import UserService
from services.auth_service import AuthService

def main():
    # Demonstrate user service
    print("\n=== User Service Demo ===")
    users = UserService.get_users()
    print("All users:", users)
    
    user = UserService.get_user_by_id(1)
    print("User with ID 1:", user)
    
    new_user = UserService.create_user("alice", "alice@example.com")
    print("New user created:", new_user)
    
    # Demonstrate auth service
    print("\n=== Auth Service Demo ===")
    login_result = AuthService.login("test_user", "password123")
    print("Login attempt:", login_result)
    
    token = login_result.get("token")
    is_valid = AuthService.validate_token(token)
    print("Token validation:", is_valid)

if __name__ == "__main__":
    main()