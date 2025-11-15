from typing import Optional
from src.models.user import User, UserRole, Student, Lecturer
from src.models.subject import Subject
from src.models.class_model import Class
from src.models.grade import Grade
from src.services.auth_service import AuthService
from src.services.student_service import StudentService
from src.services.lecturer_service import LecturerService
from src.services.subject_service import SubjectService
from src.services.class_service import ClassService
from src.services.grade_service import GradeService
from src.ui.menu import Menu, AdminMenu, StudentMenu, LecturerMenu


class AppController:
    def __init__(
        self,
        auth_service: AuthService,
        student_service: StudentService,
        lecturer_service: LecturerService,
        subject_service: SubjectService,
        class_service: ClassService,
        grade_service: GradeService
    ):
        self.auth_service = auth_service
        self.student_service = student_service
        self.lecturer_service = lecturer_service
        self.subject_service = subject_service
        self.class_service = class_service
        self.grade_service = grade_service
        
        self.admin_menu = AdminMenu()
        self.student_menu = StudentMenu()
        self.lecturer_menu = LecturerMenu()
        
        self._setup_menus()
    
    def _setup_menus(self):
        self._setup_admin_menu()
        self._setup_student_menu()
        self._setup_lecturer_menu()
    
    def _setup_admin_menu(self):
        self.admin_menu.add_option("1", "Quản lý Sinh viên", self._admin_student_menu)
        self.admin_menu.add_option("2", "Quản lý Giảng viên", self._admin_lecturer_menu)
        self.admin_menu.add_option("3", "Quản lý Môn học", self._admin_subject_menu)
        self.admin_menu.add_option("4", "Quản lý Lịch học", self._admin_class_menu)
        self.admin_menu.add_option("5", "Đổi mật khẩu", self._change_password)
        self.admin_menu.add_option("0", "Đăng xuất", lambda: False)
    
    def _setup_student_menu(self):
        self.student_menu.add_option("1", "Xem Lịch học", self._view_schedule)
        self.student_menu.add_option("2", "Xem Điểm", self._view_grades)
        self.student_menu.add_option("3", "Đăng ký Môn học", self._register_class)
        self.student_menu.add_option("4", "Đổi mật khẩu", self._change_password)
        self.student_menu.add_option("0", "Đăng xuất", lambda: False)
    
    def _setup_lecturer_menu(self):
        self.lecturer_menu.add_option("1", "Nhập Điểm", self._input_grades)
        self.lecturer_menu.add_option("2", "Đổi mật khẩu", self._change_password)
        self.lecturer_menu.add_option("0", "Đăng xuất", lambda: False)
    
    def login(self) -> bool:
        print("\n" + "=" * 60)
        print("ĐĂNG NHẬP HỆ THỐNG".center(60))
        print("=" * 60)
        
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        try:
            user = self.auth_service.login(username, password)
            print(f"\n✓ Đăng nhập thành công!")
            print(f"Chào mừng {user.name} ({user.role.value})")
            input("\nNhấn Enter để tiếp tục...")
            return True
        except ValueError as e:
            print(f"\n{e}")
            input("\nNhấn Enter để tiếp tục...")
            return False
    
    def run(self):
        while True:
            if not self.auth_service.is_authenticated():
                if not self.login():
                    continue
            
            user = self.auth_service.get_current_user()
            if not user:
                continue
            
            if user.role == UserRole.ADMIN:
                self.admin_menu.run()
            elif user.role == UserRole.STUDENT:
                self.student_menu.run()
            elif user.role == UserRole.LECTURER:
                self.lecturer_menu.run()
            
            self.auth_service.logout()
    
    def _admin_student_menu(self):
        menu = Menu("QUẢN LÝ SINH VIÊN")
        menu.add_option("1", "Xem tất cả Sinh viên", self._list_all_students)
        menu.add_option("2", "Thêm Sinh viên", self._add_student)
        menu.add_option("3", "Sửa Sinh viên", self._edit_student)
        menu.add_option("4", "Xóa Sinh viên", self._delete_student)
        menu.add_option("0", "Quay lại", lambda: False)
        menu.run()
    
    def _admin_lecturer_menu(self):
        menu = Menu("QUẢN LÝ GIẢNG VIÊN")
        menu.add_option("1", "Xem tất cả Giảng viên", self._list_all_lecturers)
        menu.add_option("2", "Thêm Giảng viên", self._add_lecturer)
        menu.add_option("3", "Sửa Giảng viên", self._edit_lecturer)
        menu.add_option("4", "Xóa Giảng viên", self._delete_lecturer)
        menu.add_option("0", "Quay lại", lambda: False)
        menu.run()
    
    def _admin_subject_menu(self):
        menu = Menu("QUẢN LÝ MÔN HỌC")
        menu.add_option("1", "Xem tất cả Môn học", self._list_all_subjects)
        menu.add_option("2", "Thêm Môn học mới", self._add_subject)
        menu.add_option("3", "Sửa Môn học", self._edit_subject)
        menu.add_option("4", "Xóa Môn học", self._delete_subject)
        menu.add_option("0", "Quay lại", lambda: False)
        menu.run()
    
    def _admin_class_menu(self):
        menu = Menu("QUẢN LÝ LỊCH HỌC")
        menu.add_option("1", "Xem tất cả Lớp học", self._list_all_classes)
        menu.add_option("2", "Thêm Lớp học mới", self._add_class)
        menu.add_option("3", "Sửa Lớp học", self._edit_class)
        menu.add_option("4", "Xóa Lớp học", self._delete_class)
        menu.add_option("0", "Quay lại", lambda: False)
        menu.run()
    
    def _view_schedule(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Student):
            print("✗ Lỗi: Không tìm thấy thông tin sinh viên.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        classes = self.student_service.get_student_schedule(user.username)
        if not classes:
            print("\nBạn chưa đăng ký lớp học nào.")
        else:
            print("\n" + "=" * 60)
            print("LỊCH HỌC CỦA BẠN".center(60))
            print("=" * 60)
            schedule_dict = {}
            for cls in classes:
                day = cls.schedule.split()[0] if cls.schedule else "Chưa có"
                if day not in schedule_dict:
                    schedule_dict[day] = []
                schedule_dict[day].append(cls)
            
            for day, cls_list in sorted(schedule_dict.items()):
                print(f"\n{day}:")
                for cls in cls_list:
                    subject = self.subject_service.get_subject_by_code(cls.subject_code)
                    subject_name = subject.name if subject else cls.subject_code
                    print(f"  {cls.schedule}: {subject_name} tại {cls.room}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _view_grades(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Student):
            print("✗ Lỗi: Không tìm thấy thông tin sinh viên.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        grades = self.student_service.get_student_grades(user.username)
        if not grades:
            print("\nBạn chưa có điểm số nào.")
        else:
            print("\n" + "=" * 60)
            print("ĐIỂM SỐ CỦA BẠN".center(60))
            print("=" * 60)
            for grade in grades:
                subject = self.subject_service.get_subject_by_code(
                    self.class_service.get_class_by_code(grade.class_code).subject_code
                    if self.class_service.get_class_by_code(grade.class_code) else ""
                )
                subject_name = subject.name if subject else grade.class_code
                mid = grade.midterm_score if grade.midterm_score is not None else "N/A"
                final = grade.final_score if grade.final_score is not None else "N/A"
                total = grade.total_score if grade.total_score is not None else "N/A"
                print(f"\n{subject_name} ({grade.class_code}):")
                print(f"  Giữa kỳ: {mid}, Cuối kỳ: {final}, Tổng: {total}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _register_class(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Student):
            print("✗ Lỗi: Không tìm thấy thông tin sinh viên.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        all_classes = self.class_service.get_all_classes()
        available_classes = [cls for cls in all_classes if not cls.is_full]
        
        if not available_classes:
            print("\nKhông có lớp học nào có sẵn để đăng ký.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH LỚP HỌC".center(60))
        print("=" * 60)
        for idx, cls in enumerate(available_classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name} - {cls.schedule} tại {cls.room} ({cls.current_count}/{cls.max_students})")
        
        try:
            choice = int(input("\nChọn STT lớp để đăng ký: ").strip())
            if 1 <= choice <= len(available_classes):
                selected_class = available_classes[choice - 1]
                self.student_service.register_class(user.username, selected_class.code)
                print(f"\n✓ Thành công: Đã đăng ký '{selected_class.code}'.")
            else:
                print("\n✗ STT không hợp lệ.")
        except ValueError:
            print("\n✗ Vui lòng nhập số hợp lệ.")
        except Exception as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _input_grades(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Lecturer):
            print("✗ Lỗi: Không tìm thấy thông tin giảng viên.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        if hasattr(self.class_service._class_repository, 'find_by_lecturer'):
            classes = self.class_service._class_repository.find_by_lecturer(user.username)
        else:
            classes = [cls for cls in self.class_service.get_all_classes() if cls.lecturer_username == user.username]
        
        if not classes:
            print("\nBạn không có lớp học nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH LỚP HỌC CỦA BẠN".center(60))
        print("=" * 60)
        for idx, cls in enumerate(classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name}")
        
        try:
            class_choice = int(input("\nChọn STT lớp: ").strip())
            if not (1 <= class_choice <= len(classes)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            selected_class = classes[class_choice - 1]
            
            print("\n" + "=" * 60)
            print("DANH SÁCH SINH VIÊN".center(60))
            print("=" * 60)
            for idx, student_username in enumerate(selected_class.enrolled_students, 1):
                print(f"{idx}. [{student_username}]")
            
            student_choice = int(input("\nChọn STT sinh viên: ").strip())
            if not (1 <= student_choice <= len(selected_class.enrolled_students)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            student_username = selected_class.enrolled_students[student_choice - 1]
            
            midterm = input("Nhập Điểm Giữa kỳ: ").strip()
            final = input("Nhập Điểm Cuối kỳ: ").strip()
            
            midterm_score = float(midterm) if midterm else None
            final_score = float(final) if final else None
            
            self.grade_service.input_grade(
                student_username,
                selected_class.code,
                midterm_score,
                final_score
            )
            print(f"\n✓ Thành công: Đã lưu điểm cho '{student_username}'.")
        except ValueError as e:
            print(f"\n✗ Lỗi: {e}")
        except Exception as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _change_password(self):
        old_password = input("Nhập Mật khẩu cũ: ").strip()
        new_password = input("Nhập Mật khẩu mới: ").strip()
        
        try:
            self.auth_service.change_password(old_password, new_password)
            print("\n✓ Thành công: Đã đổi mật khẩu.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _list_all_students(self):
        students = self.student_service.get_all_students()
        print("\n" + "=" * 60)
        print("DANH SÁCH SINH VIÊN".center(60))
        print("=" * 60)
        if not students:
            print("Không có sinh viên nào.")
        else:
            for idx, student in enumerate(students, 1):
                print(f"{idx}. [{student.username}] {student.name} - {student.user_id} - {student.status}")
        input("\nNhấn Enter để tiếp tục...")
    
    def _add_student(self):
        user_id = input("UserID: ").strip()
        username = input("Nhập Username: ").strip()
        password = input("Password: ").strip()
        name = input("Tên sinh viên: ").strip()
        
        try:
            student = self.student_service.create_student(user_id, username, password, name)
            print(f"\n✓ Thành công: Đã tạo sinh viên '{username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _edit_student(self):
        students = self.student_service.get_all_students()
        if not students:
            print("\nKhông có sinh viên nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH SINH VIÊN".center(60))
        print("=" * 60)
        for idx, student in enumerate(students, 1):
            print(f"{idx}. [{student.username}] {student.name}")
        
        try:
            choice = int(input("\nChọn STT sinh viên cần sửa: ").strip())
            if not (1 <= choice <= len(students)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            student = students[choice - 1]
            status = input("Trạng thái học tập: ").strip()
            
            if status:
                student.status = status
                self.student_service.update_student(student)
                print(f"\n✓ Thành công: Đã cập nhật sinh viên '{student.username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _delete_student(self):
        students = self.student_service.get_all_students()
        if not students:
            print("\nKhông có sinh viên nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH SINH VIÊN".center(60))
        print("=" * 60)
        for idx, student in enumerate(students, 1):
            print(f"{idx}. [{student.username}] {student.name}")
        
        try:
            choice = int(input("\nChọn STT sinh viên cần xóa: ").strip())
            if not (1 <= choice <= len(students)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            student = students[choice - 1]
            confirm = input(f"Xóa '{student.name}'? (C/K): ").strip().upper()
            
            if confirm == "C":
                self.student_service.delete_student(student.id)
                print("\n✓ Đã xóa")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _list_all_lecturers(self):
        lecturers = self.lecturer_service.get_all_lecturers()
        print("\n" + "=" * 60)
        print("DANH SÁCH GIẢNG VIÊN".center(60))
        print("=" * 60)
        if not lecturers:
            print("Không có giảng viên nào.")
        else:
            for idx, lecturer in enumerate(lecturers, 1):
                print(f"{idx}. [{lecturer.username}] {lecturer.name} - {lecturer.department}")
        input("\nNhấn Enter để tiếp tục...")
    
    def _add_lecturer(self):
        user_id = input("UserID: ").strip()
        username = input("Nhập Username: ").strip()
        password = input("Password: ").strip()
        name = input("Tên giảng viên: ").strip()
        department = input("Khoa: ").strip()
        
        try:
            lecturer = self.lecturer_service.create_lecturer(user_id, username, password, name, department)
            print(f"\n✓ Thành công: Đã tạo giảng viên '{username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _edit_lecturer(self):
        lecturers = self.lecturer_service.get_all_lecturers()
        if not lecturers:
            print("\nKhông có giảng viên nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH GIẢNG VIÊN".center(60))
        print("=" * 60)
        for idx, lecturer in enumerate(lecturers, 1):
            print(f"{idx}. [{lecturer.username}] {lecturer.name}")
        
        try:
            choice = int(input("\nChọn STT giảng viên cần sửa: ").strip())
            if not (1 <= choice <= len(lecturers)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            lecturer = lecturers[choice - 1]
            department = input("Nhập Khoa MỚI...: ").strip()
            
            if department:
                lecturer.department = department
                self.lecturer_service.update_lecturer(lecturer)
                print(f"\n✓ Thành công: Đã cập nhật giảng viên '{lecturer.username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _delete_lecturer(self):
        lecturers = self.lecturer_service.get_all_lecturers()
        if not lecturers:
            print("\nKhông có giảng viên nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH GIẢNG VIÊN".center(60))
        print("=" * 60)
        for idx, lecturer in enumerate(lecturers, 1):
            print(f"{idx}. [{lecturer.username}] {lecturer.name}")
        
        try:
            choice = int(input("\nChọn STT giảng viên cần xóa: ").strip())
            if not (1 <= choice <= len(lecturers)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            lecturer = lecturers[choice - 1]
            confirm = input(f"Xóa '{lecturer.name}'? (C/K): ").strip().upper()
            
            if confirm == "C":
                self.lecturer_service.delete_lecturer(lecturer.id)
                print("\n✓ Đã xóa")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _list_all_subjects(self):
        subjects = self.subject_service.get_all_subjects()
        print("\n" + "=" * 60)
        print("DANH SÁCH MÔN HỌC".center(60))
        print("=" * 60)
        if not subjects:
            print("Không có môn học nào.")
        else:
            for idx, subject in enumerate(subjects, 1):
                print(f"{idx}. [{subject.code}] {subject.name} - {subject.credits} tín chỉ")
        input("\nNhấn Enter để tiếp tục...")
    
    def _add_subject(self):
        code = input("Nhập Mã Môn học: ").strip()
        name = input("Nhập Tên Môn học: ").strip()
        credits = input("Nhập Số tín chỉ: ").strip()
        
        try:
            credits_int = int(credits) if credits else 0
            subject = self.subject_service.create_subject(code, name, credits_int)
            print(f"\n✓ Thành công: Đã thêm môn học '{code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _edit_subject(self):
        subjects = self.subject_service.get_all_subjects()
        if not subjects:
            print("\nKhông có môn học nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH MÔN HỌC".center(60))
        print("=" * 60)
        for idx, subject in enumerate(subjects, 1):
            print(f"{idx}. [{subject.code}] {subject.name}")
        
        try:
            choice = int(input("\nChọn STT môn học cần sửa: ").strip())
            if not (1 <= choice <= len(subjects)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            subject = subjects[choice - 1]
            name = input("Nhập TÊN MỚI...: ").strip()
            credits = input("Nhập SỐ TÍN CHỈ MỚI...: ").strip()
            
            name_new = name if name else None
            credits_new = int(credits) if credits else None
            
            self.subject_service.update_subject(subject, name_new, credits_new)
            print(f"\n✓ Thành công: Đã cập nhật môn học '{subject.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _delete_subject(self):
        subjects = self.subject_service.get_all_subjects()
        if not subjects:
            print("\nKhông có môn học nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH MÔN HỌC".center(60))
        print("=" * 60)
        for idx, subject in enumerate(subjects, 1):
            print(f"{idx}. [{subject.code}] {subject.name}")
        
        try:
            choice = int(input("\nChọn STT môn học cần xóa: ").strip())
            if not (1 <= choice <= len(subjects)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            subject = subjects[choice - 1]
            confirm = input(f"Xóa '{subject.name}'? (C/K): ").strip().upper()
            
            if confirm == "C":
                self.subject_service.delete_subject(subject.id)
                print(f"\n✓ Thành công: Đã xóa môn học '{subject.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _list_all_classes(self):
        classes = self.class_service.get_all_classes()
        print("\n" + "=" * 60)
        print("DANH SÁCH LỚP HỌC".center(60))
        print("=" * 60)
        if not classes:
            print("Không có lớp học nào.")
        else:
            for idx, cls in enumerate(classes, 1):
                subject = self.subject_service.get_subject_by_code(cls.subject_code)
                subject_name = subject.name if subject else cls.subject_code
                print(f"{idx}. [{cls.code}] {subject_name} - {cls.schedule} tại {cls.room} ({cls.current_count}/{cls.max_students})")
        input("\nNhấn Enter để tiếp tục...")
    
    def _add_class(self):
        code = input("Nhập Mã Lớp học: ").strip()
        subject_code = input("Nhập Mã môn học: ").strip()
        lecturer_username = input("Nhập Username giảng viên: ").strip()
        room = input("Nhập phòng: ").strip()
        schedule = input("Nhập Lịch (ví dụ: T2 7-9): ").strip()
        max_students = input("Sĩ số tối đa (mặc định 50): ").strip()
        
        try:
            max_students_int = int(max_students) if max_students else 50
            class_obj = self.class_service.create_class(
                code, subject_code, lecturer_username, room, schedule, max_students_int
            )
            print(f"\n✓ Thành công: Đã thêm lớp học mới.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _edit_class(self):
        classes = self.class_service.get_all_classes()
        if not classes:
            print("\nKhông có lớp học nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH LỚP HỌC".center(60))
        print("=" * 60)
        for idx, cls in enumerate(classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name}")
        
        try:
            choice = int(input("\nChọn STT lớp cần sửa: ").strip())
            if not (1 <= choice <= len(classes)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            class_obj = classes[choice - 1]
            room = input("Nhập Phòng mới: ").strip()
            schedule = input("Nhập Lịch mới (Enter để bỏ qua): ").strip()
            
            room_new = room if room else None
            schedule_new = schedule if schedule else None
            
            self.class_service.update_class(class_obj, room_new, schedule_new)
            print(f"\n✓ Thành công: Đã cập nhật lớp '{class_obj.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")
    
    def _delete_class(self):
        classes = self.class_service.get_all_classes()
        if not classes:
            print("\nKhông có lớp học nào.")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH LỚP HỌC".center(60))
        print("=" * 60)
        for idx, cls in enumerate(classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name}")
        
        try:
            choice = int(input("\nChọn STT lớp cần xóa: ").strip())
            if not (1 <= choice <= len(classes)):
                print("\n✗ STT không hợp lệ.")
                input("\nNhấn Enter để tiếp tục...")
                return
            
            class_obj = classes[choice - 1]
            subject = self.subject_service.get_subject_by_code(class_obj.subject_code)
            subject_name = subject.name if subject else class_obj.code
            confirm = input(f"Xóa '{subject_name}'? (C/K): ").strip().upper()
            
            if confirm == "C":
                self.class_service.delete_class(class_obj.id)
                print(f"\n✓ Thành công: Đã xóa lớp học '{class_obj.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nNhấn Enter để tiếp tục...")

