from typing import Optional
from src.models.user import User
from src.interfaces.repository_interface import IRepository


class AuthService:
    def __init__(self, user_repository: IRepository[User]):
        self._user_repository = user_repository
        self._current_user: Optional[User] = None
    
    def login(self, username: str, password: str) -> User:
        if not username:
            raise ValueError("Tên đăng nhập không được để trống.")
        
        if not password:
            raise ValueError("Mật khẩu không được để trống.")
        
        user = None
        if hasattr(self._user_repository, 'find_by_username'):
            user = self._user_repository.find_by_username(username)
        else:
            for u in self._user_repository.get_all():
                if u.username == username:
                    user = u
                    break
        
        if not user:
            raise ValueError("Lỗi: Tên đăng nhập hoặc mật khẩu không hợp lệ.")
        
        if user.password != password:
            raise ValueError("Lỗi: Tên đăng nhập hoặc mật khẩu không hợp lệ.")
        
        self._current_user = user
        return user
    
    def logout(self) -> None:
        self._current_user = None
    
    def get_current_user(self) -> Optional[User]:
        return self._current_user
    
    def is_authenticated(self) -> bool:
        return self._current_user is not None
    
    def change_password(self, old_password: str, new_password: str) -> None:
        if not self._current_user:
            raise ValueError("Bạn chưa đăng nhập.")
        
        if self._current_user.password != old_password:
            raise ValueError("Lỗi: Mật khẩu cũ không chính xác.")
        
        if not new_password:
            raise ValueError("Mật khẩu mới không được để trống.")
        
        self._current_user.password = new_password
        self._user_repository.update(self._current_user)

