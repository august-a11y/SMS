from typing import Optional, List
from src.models.class_model import Class
from src.repositories.base_repository import BaseRepository


class ClassRepository(BaseRepository[Class]):
    def find_by_code(self, code: str) -> Optional[Class]:
        for class_obj in self.get_all():
            if class_obj.code.upper() == code.upper():
                return class_obj
        return None
    
    def find_by_subject_code(self, subject_code: str) -> List[Class]:
        return [cls for cls in self.get_all() if cls.subject_code.upper() == subject_code.upper()]
    
    def find_by_lecturer(self, lecturer_username: str) -> List[Class]:
        return [cls for cls in self.get_all() if cls.lecturer_username == lecturer_username]
    
    def find_by_student(self, student_username: str) -> List[Class]:
        return [cls for cls in self.get_all() if student_username in cls.enrolled_students]
    
    def find_conflicting_schedule(self, room: str, schedule: str, exclude_class_id: Optional[int] = None) -> Optional[Class]:
        for cls in self.get_all():
            if exclude_class_id and cls.id == exclude_class_id:
                continue
            if cls.room == room and cls.schedule == schedule:
                return cls
        return None

