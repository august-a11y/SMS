from typing import Optional
from src.models.user import User
from src.interfaces.repository_interface import IRepository


class AuthService:
    def __init__(self, user_repository: IRepository[User]):
        self._user_repository = user_repository
        self._current_user: Optional[User] = None
    
    def login(self, username: str, password: str) -> User:
        if not username:
            raise ValueError("Username cannot be empty.")
        
        if not password:
            raise ValueError("Password cannot be empty.")
        
        user = None

        if hasattr(self._user_repository, 'find_by_username'):
            user = self._user_repository.find_by_username(username)
        else:
            for u in self._user_repository.get_all():
                if u.username == username:
                    user = u
                    break
        
        if not user:
            raise ValueError("Error: Invalid username or password.")
        
        if user.password != password:
            raise ValueError("Error: Invalid username or password.")
        
        self._current_user = user
        return user
    
    def logout(self) -> None:
        self._current_user = None
        print("You have been logged out successfully.")
    
    def get_current_user(self) -> Optional[User]:
        return self._current_user
    
    def is_authenticated(self) -> bool:
        return self._current_user is not None
    
    def change_password(self, old_password: str, new_password: str) -> None:
        if not self._current_user:
            raise ValueError("You are not logged in.")
        
        if self._current_user.password != old_password:
            raise ValueError("Error: Incorrect old password.")
        
        if not new_password:
            raise ValueError("New password cannot be empty.")
        
        self._current_user.password = new_password
        self._user_repository.update(self._current_user)