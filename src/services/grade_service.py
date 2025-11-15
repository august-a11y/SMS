from typing import List, Optional
from src.models.grade import Grade
from src.interfaces.repository_interface import IRepository


class GradeService:
    def __init__(self, grade_repository: IRepository[Grade]):
        self._grade_repository = grade_repository
    
    def input_grade(
        self,
        student_username: str,
        class_code: str,
        midterm_score: Optional[float] = None,
        final_score: Optional[float] = None
    ) -> Grade:
        if hasattr(self._grade_repository, 'find_by_student_and_class'):
            grade = self._grade_repository.find_by_student_and_class(student_username, class_code)
        else:
            grade = None
            for g in self._grade_repository.get_all():
                if g.student_username == student_username and g.class_code == class_code:
                    grade = g
                    break
        
        if grade:
            if midterm_score is not None:
                grade.midterm_score = midterm_score
            if final_score is not None:
                grade.final_score = final_score
            return self._grade_repository.update(grade)
        else:
            grade = Grade(
                id=None,
                student_username=student_username,
                class_code=class_code,
                midterm_score=midterm_score,
                final_score=final_score
            )
            return self._grade_repository.create(grade)
    
    def get_grades_by_student(self, student_username: str) -> List[Grade]:
        if hasattr(self._grade_repository, 'find_by_student'):
            return self._grade_repository.find_by_student(student_username)
        return []
    
    def get_grades_by_class(self, class_code: str) -> List[Grade]:
        if hasattr(self._grade_repository, 'find_by_class'):
            return self._grade_repository.find_by_class(class_code)
        return []

