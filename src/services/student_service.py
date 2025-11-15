from typing import List
from src.models.user import Student, UserRole
from src.models.class_model import Class
from src.models.grade import Grade
from src.interfaces.repository_interface import IRepository


class StudentService:
    def __init__(
        self,
        user_repository: IRepository,
        class_repository: IRepository[Class],
        grade_repository: IRepository[Grade]
    ):
        self._user_repository = user_repository
        self._class_repository = class_repository
        self._grade_repository = grade_repository
    
    def create_student(self, user_id: str, username: str, password: str, name: str) -> Student:
        if hasattr(self._user_repository, 'find_by_username'):
            existing = self._user_repository.find_by_username(username)
            if existing:
                raise ValueError(f"Lỗi: Tên đăng nhập '{username}' đã tồn tại.")
        
        student = Student(
            id=None,
            username=username,
            password=password,
            role=UserRole.STUDENT,
            user_id=user_id,
            name=name
        )
        return self._user_repository.create(student)
    
    def get_all_students(self) -> List[Student]:
        if hasattr(self._user_repository, 'find_by_role'):
            users = self._user_repository.find_by_role(UserRole.STUDENT)
            return [u for u in users if isinstance(u, Student)]
        return []
    
    def update_student(self, student: Student) -> Student:
        return self._user_repository.update(student)
    
    def delete_student(self, student_id: int) -> bool:
        return self._user_repository.delete(student_id)
    
    def register_class(self, student_username: str, class_code: str) -> Class:
        if hasattr(self._class_repository, 'find_by_code'):
            class_obj = self._class_repository.find_by_code(class_code)
        else:
            class_obj = None
            for cls in self._class_repository.get_all():
                if cls.code == class_code:
                    class_obj = cls
                    break
        
        if not class_obj:
            raise ValueError(f"Lớp học '{class_code}' không tồn tại.")
        
        if class_obj.is_full:
            raise ValueError(f"Lỗi: Không thể đăng ký. Lớp '{class_code}' đã đầy.")
        
        if student_username in class_obj.enrolled_students:
            raise ValueError(f"Sinh viên đã đăng ký lớp '{class_code}'.")
        
        class_obj.enrolled_students.append(student_username)
        self._class_repository.update(class_obj)
        
        if hasattr(self._user_repository, 'find_by_username'):
            student = self._user_repository.find_by_username(student_username)
            if student and isinstance(student, Student):
                if class_code not in student.registered_classes:
                    student.registered_classes.append(class_code)
                self._user_repository.update(student)
        
        return class_obj
    
    def get_student_schedule(self, student_username: str) -> List[Class]:
        if hasattr(self._class_repository, 'find_by_student'):
            return self._class_repository.find_by_student(student_username)
        return []
    
    def get_student_grades(self, student_username: str) -> List[Grade]:
        if hasattr(self._grade_repository, 'find_by_student'):
            return self._grade_repository.find_by_student(student_username)
        return []

