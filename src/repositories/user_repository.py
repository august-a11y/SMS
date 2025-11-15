from typing import Optional
from src.models.user import User, UserRole
from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    def find_by_username(self, username: str) -> Optional[User]:
        for user in self.get_all():
            if user.username.lower() == username.lower():
                return user
        return None
    
    def find_by_user_id(self, user_id: str) -> Optional[User]:
        for user in self.get_all():
            if user.user_id == user_id:
                return user
        return None
    
    def find_by_role(self, role: UserRole) -> list[User]:
        return [user for user in self.get_all() if user.role == role]
