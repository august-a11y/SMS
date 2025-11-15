from typing import Optional, List
from src.models.grade import Grade
from src.repositories.base_repository import BaseRepository


class GradeRepository(BaseRepository[Grade]):
    def find_by_student(self, student_username: str) -> List[Grade]:
        return [grade for grade in self.get_all() if grade.student_username == student_username]
    
    def find_by_class(self, class_code: str) -> List[Grade]:
        return [grade for grade in self.get_all() if grade.class_code == class_code]
    
    def find_by_student_and_class(self, student_username: str, class_code: str) -> Optional[Grade]:
        for grade in self.get_all():
            if grade.student_username == student_username and grade.class_code == class_code:
                return grade
        return None

