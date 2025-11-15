from src.models.user import Admin, Student, Lecturer, UserRole
from src.models.subject import Subject
from src.models.class_model import Class
from src.repositories.user_repository import UserRepository
from src.repositories.subject_repository import SubjectRepository
from src.repositories.class_repository import ClassRepository
from src.repositories.grade_repository import GradeRepository
from src.services.auth_service import AuthService
from src.services.student_service import StudentService
from src.services.lecturer_service import LecturerService
from src.services.subject_service import SubjectService
from src.services.class_service import ClassService
from src.services.grade_service import GradeService
from src.controllers.app_controller import AppController


def initialize_data(
    user_repo: UserRepository,
    subject_repo: SubjectRepository,
    class_repo: ClassRepository
):
    admin = Admin(
        id=None,
        username="admin01",
        password="admin123",
        role=UserRole.ADMIN,
        user_id="ADMIN001",
        name="Administrator"
    )
    user_repo.create(admin)
    
    student1 = Student(
        id=None,
        username="student01",
        password="123456",
        role=UserRole.STUDENT,
        user_id="051111",
        name="Nguyễn Văn A"
    )
    user_repo.create(student1)
    
    lecturer1 = Lecturer(
        id=None,
        username="lecturer01",
        password="123456",
        role=UserRole.LECTURER,
        user_id="051211",
        name="Prof. Alan",
        department="Khoa học Máy tính"
    )
    user_repo.create(lecturer1)
    
    subject1 = Subject(id=None, code="CS101", name="Nhập môn Lập trình", credits=3)
    subject_repo.create(subject1)
    
    subject2 = Subject(id=None, code="CS102", name="Cấu trúc Dữ liệu", credits=3)
    subject_repo.create(subject2)
    
    class1 = Class(
        id=None,
        code="CL1001",
        subject_code="CS101",
        lecturer_username="lecturer01",
        room="B101",
        schedule="T2 7-9",
        max_students=50
    )
    class_repo.create(class1)
    
    class2 = Class(
        id=None,
        code="CL1002",
        subject_code="CS101",
        lecturer_username="lecturer01",
        room="B102",
        schedule="T3 9-11",
        max_students=50
    )
    class_repo.create(class2)


def main():
    print("=" * 60)
    print("HỆ THỐNG QUẢN LÝ HỌC TẬP".center(60))
    print("=" * 60)
    
    user_repository = UserRepository()
    subject_repository = SubjectRepository()
    class_repository = ClassRepository()
    grade_repository = GradeRepository()
    
    initialize_data(user_repository, subject_repository, class_repository)
    
    auth_service = AuthService(user_repository)
    student_service = StudentService(user_repository, class_repository, grade_repository)
    lecturer_service = LecturerService(user_repository)
    subject_service = SubjectService(subject_repository)
    class_service = ClassService(class_repository)
    grade_service = GradeService(grade_repository)
    
    controller = AppController(
        auth_service=auth_service,
        student_service=student_service,
        lecturer_service=lecturer_service,
        subject_service=subject_service,
        class_service=class_service,
        grade_service=grade_service
    )
    
    try:
        controller.run()
    except KeyboardInterrupt:
        print("\n\nCảm ơn bạn đã sử dụng hệ thống!")
    except Exception as e:
        print(f"\n✗ Lỗi: {e}")


if __name__ == "__main__":
    main()