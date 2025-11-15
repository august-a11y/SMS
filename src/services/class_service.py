from typing import List, Optional
from src.models.class_model import Class
from src.interfaces.repository_interface import IRepository


class ClassService:
    def __init__(self, class_repository: IRepository[Class]):
        self._class_repository = class_repository
    
    def create_class(
        self,
        code: str,
        subject_code: str,
        lecturer_username: str,
        room: str,
        schedule: str,
        max_students: int = 50
    ) -> Class:
        if hasattr(self._class_repository, 'find_by_code'):
            existing = self._class_repository.find_by_code(code)
            if existing:
                raise ValueError(f"Lỗi: Mã lớp học '{code}' đã tồn tại.")
        
        if hasattr(self._class_repository, 'find_conflicting_schedule'):
            conflicting = self._class_repository.find_conflicting_schedule(room, schedule)
            if conflicting:
                raise ValueError(f"Lỗi: Trùng lịch phòng '{room}'.")
        
        class_obj = Class(
            id=None,
            code=code,
            subject_code=subject_code,
            lecturer_username=lecturer_username,
            room=room,
            schedule=schedule,
            max_students=max_students
        )
        return self._class_repository.create(class_obj)
    
    def get_all_classes(self) -> List[Class]:
        return self._class_repository.get_all()
    
    def update_class(
        self,
        class_obj: Class,
        room: Optional[str] = None,
        schedule: Optional[str] = None
    ) -> Class:
        if room is not None:
            if hasattr(self._class_repository, 'find_conflicting_schedule'):
                conflicting = self._class_repository.find_conflicting_schedule(
                    room,
                    schedule if schedule else class_obj.schedule,
                    exclude_class_id=class_obj.id
                )
                if conflicting:
                    raise ValueError(f"Lỗi: Phòng học '{room}' đã bận.")
            class_obj.room = room
        
        if schedule is not None:
            if hasattr(self._class_repository, 'find_conflicting_schedule'):
                conflicting = self._class_repository.find_conflicting_schedule(
                    room if room else class_obj.room,
                    schedule,
                    exclude_class_id=class_obj.id
                )
                if conflicting:
                    raise ValueError(f"Lỗi: Trùng lịch phòng '{class_obj.room}'.")
            class_obj.schedule = schedule
        
        return self._class_repository.update(class_obj)
    
    def delete_class(self, class_id: int) -> bool:
        return self._class_repository.delete(class_id)
    
    def get_class_by_code(self, code: str) -> Optional[Class]:
        if hasattr(self._class_repository, 'find_by_code'):
            return self._class_repository.find_by_code(code)
        return None

