from typing import List
from src.models.user import Lecturer, UserRole
from src.interfaces.repository_interface import IRepository


class LecturerService:
    def __init__(self, user_repository: IRepository):
        self._user_repository = user_repository
    
    def create_lecturer(self, user_id: str, username: str, password: str, name: str, department: str = "") -> Lecturer:
        if hasattr(self._user_repository, 'find_by_username'):
            existing = self._user_repository.find_by_username(username)
            if existing:
                raise ValueError(f"Lỗi: Tên đăng nhập '{username}' đã tồn tại.")
        
        lecturer = Lecturer(
            id=None,
            username=username,
            password=password,
            role=UserRole.LECTURER,
            user_id=user_id,
            name=name,
            department=department
        )
        return self._user_repository.create(lecturer)
    
    def get_all_lecturers(self) -> List[Lecturer]:
        if hasattr(self._user_repository, 'find_by_role'):
            users = self._user_repository.find_by_role(UserRole.LECTURER)
            return [u for u in users if isinstance(u, Lecturer)]
        return []
    
    def update_lecturer(self, lecturer: Lecturer) -> Lecturer:
        return self._user_repository.update(lecturer)
    
    def delete_lecturer(self, lecturer_id: int) -> bool:
        return self._user_repository.delete(lecturer_id)

