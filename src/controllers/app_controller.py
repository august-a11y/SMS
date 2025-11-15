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
        self.admin_menu.add_option("1", "Manage Students", self._admin_student_menu)
        self.admin_menu.add_option("2", "Manage Lecturers", self._admin_lecturer_menu)
        self.admin_menu.add_option("3", "Manage Course", self._admin_subject_menu)
        self.admin_menu.add_option("4", "Manage Schedule", self._admin_class_menu)
        self.admin_menu.add_option("5", "Change Password", self._change_password)
        self.admin_menu.add_option("0", "Logout", lambda: False)
    
    def _setup_student_menu(self):
        self.student_menu.add_option("1", "View Schedule", self._view_schedule)
        self.student_menu.add_option("2", "View Grades", self._view_grades)
        self.student_menu.add_option("3", "Register Courese", self._register_class)
        self.student_menu.add_option("4", "Change Password", self._change_password)
        self.student_menu.add_option("0", "Logout", lambda: False)
    
    def _setup_lecturer_menu(self):
        self.lecturer_menu.add_option("1", "Enter Grades", self._input_grades)
        self.lecturer_menu.add_option("2", "Change Password", self._change_password)
        self.lecturer_menu.add_option("0", "Logout", lambda: False)
    
    def login(self) -> bool:
        print("\n" + "=" * 60)
        print("SYSTEM LOGIN".center(60))
        print("=" * 60)
        
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        try:
            user = self.auth_service.login(username, password)
            print(f"\n✓ Login successful!")
            print(f"Welcome {user.name} ({user.role.value})")
            input("\nPress Enter to continue...")
            return True
        except ValueError as e:
            print(f"\n{e}")
            input("\nPress Enter to continue...")
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
        menu = Menu("STUDENT MANAGEMENT")
        menu.add_option("1", "View All Students", self._list_all_students)
        menu.add_option("2", "Add Student", self._add_student)
        menu.add_option("3", "Edit Student", self._edit_student)
        menu.add_option("4", "Delete Student", self._delete_student)
        menu.add_option("0", "Back", lambda: False)
        menu.run()
    
    def _admin_lecturer_menu(self):
        menu = Menu("LECTURER MANAGEMENT")
        menu.add_option("1", "View All Lecturers", self._list_all_lecturers)
        menu.add_option("2", "Add Lecturer", self._add_lecturer)
        menu.add_option("3", "Edit Lecturer", self._edit_lecturer)
        menu.add_option("4", "Delete Lecturer", self._delete_lecturer)
        menu.add_option("0", "Back", lambda: False)
        menu.run()
    
    def _admin_subject_menu(self):
        menu = Menu("COURSE MANAGEMENT")
        menu.add_option("1", "View All Subjects", self._list_all_subjects)
        menu.add_option("2", "Add New Subject", self._add_subject)
        menu.add_option("3", "Edit Subject", self._edit_subject)
        menu.add_option("4", "Delete Subject", self._delete_subject)
        menu.add_option("0", "Back", lambda: False)
        menu.run()
    
    def _admin_class_menu(self):
        menu = Menu("SCHEDULE MANAGEMENT")
        menu.add_option("1", "View All Schedule", self._list_all_classes)
        menu.add_option("2", "Add New Class", self._add_class)
        menu.add_option("3", "Edit Class", self._edit_class)
        menu.add_option("4", "Delete Class", self._delete_class)
        menu.add_option("0", "Back", lambda: False)
        menu.run()
    
    def _view_schedule(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Student):
            print("✗ Error: Student information not found.")
            input("\nPress Enter to continue...")
            return
        
        classes = self.student_service.get_student_schedule(user.username)
        if not classes:
            print("\nYou are not registered for any classes.")
        else:
            print("\n" + "=" * 60)
            print("YOUR SCHEDULE".center(60))
            print("=" * 60)
            schedule_dict = {}
            for cls in classes:
                day = cls.schedule.split()[0] if cls.schedule else "Not set"
                if day not in schedule_dict:
                    schedule_dict[day] = []
                schedule_dict[day].append(cls)
            
            for day, cls_list in sorted(schedule_dict.items()):
                print(f"\n{day}:")
                for cls in cls_list:
                    subject = self.subject_service.get_subject_by_code(cls.subject_code)
                    subject_name = subject.name if subject else cls.subject_code
                    print(f"  {cls.schedule}: {subject_name} at {cls.room}")
        
        input("\nPress Enter to continue...")
    
    def _view_grades(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Student):
            print("✗ Error: Student information not found.")
            input("\nPress Enter to continue...")
            return
        
        grades = self.student_service.get_student_grades(user.username)
        if not grades:
            print("\nYou do not have any grades yet.")
        else:
            print("\n" + "=" * 60)
            print("YOUR GRADES".center(60))
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
                print(f"  Midterm: {mid}, Final: {final}, Total: {total}")
        
        input("\nPress Enter to continue...")
    
    def _register_class(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Student):
            print("✗ Error: Student information not found.")
            input("\nPress Enter to continue...")
            return
        
        all_classes = self.class_service.get_all_classes()
        available_classes = [cls for cls in all_classes if not cls.is_full]
        
        if not available_classes:
            print("\nThere are no available classes to register for.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("AVAILABLE CLASSES".center(60))
        print("=" * 60)
        for idx, cls in enumerate(available_classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name} - {cls.schedule} at {cls.room} ({cls.current_count}/{cls.max_students})")
        
        try:
            choice = int(input("\nSelect class number to register: ").strip())
            if 1 <= choice <= len(available_classes):
                selected_class = available_classes[choice - 1]
                self.student_service.register_class(user.username, selected_class.code)
                print(f"\n✓ Success: Registered for '{selected_class.code}'.")
            else:
                print("\n✗ Invalid number.")
        except ValueError:
            print("\n✗ Please enter a valid number.")
        except Exception as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _input_grades(self):
        user = self.auth_service.get_current_user()
        if not user or not isinstance(user, Lecturer):
            print("✗ Error: Lecturer information not found.")
            input("\nPress Enter to continue...")
            return
        
        if hasattr(self.class_service._class_repository, 'find_by_lecturer'):
            classes = self.class_service._class_repository.find_by_lecturer(user.username)
        else:
            classes = [cls for cls in self.class_service.get_all_classes() if cls.lecturer_username == user.username]
        
        if not classes:
            print("\nYou are not assigned to any classes.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("YOUR CLASSES".center(60))
        print("=" * 60)
        for idx, cls in enumerate(classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name}")
        
        try:
            class_choice = int(input("\nSelect class number: ").strip())
            if not (1 <= class_choice <= len(classes)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            selected_class = classes[class_choice - 1]
            
            print("\n" + "=" * 60)
            print("STUDENT LIST".center(60))
            print("=" * 60)
            for idx, student_username in enumerate(selected_class.enrolled_students, 1):
                print(f"{idx}. [{student_username}]")
            
            student_choice = int(input("\nSelect student number: ").strip())
            if not (1 <= student_choice <= len(selected_class.enrolled_students)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            student_username = selected_class.enrolled_students[student_choice - 1]
            
            midterm = input("Enter Midterm Grade: ").strip()
            final = input("Enter Final Grade: ").strip()
            
            midterm_score = float(midterm) if midterm else None
            final_score = float(final) if final else None
            
            self.grade_service.input_grade(
                student_username,
                selected_class.code,
                midterm_score,
                final_score
            )
            print(f"\n✓ Success: Saved grade for '{student_username}'.")
        except ValueError as e:
            print(f"\n✗ Error: {e}")
        except Exception as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _change_password(self):
        old_password = input("Enter Old Password: ").strip()
        new_password = input("Enter New Password: ").strip()
        
        try:
            self.auth_service.change_password(old_password, new_password)
            print("\n✓ Success: Password changed.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _list_all_students(self):
        students = self.student_service.get_all_students()
        print("\n" + "=" * 60)
        print("STUDENT LIST".center(60))
        print("=" * 60)
        if not students:
            print("No students found.")
        else:
            for idx, student in enumerate(students, 1):
                print(f"{idx}. [{student.username}] {student.name} - {student.user_id} - {student.status}")
        input("\nPress Enter to continue...")
    
    def _add_student(self):
        user_id = input("UserID: ").strip()
        username = input("Enter Username: ").strip()
        password = input("Password: ").strip()
        name = input("Student Name: ").strip()
        
        try:
            student = self.student_service.create_student(user_id, username, password, name)
            print(f"\n✓ Success: Created student '{username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _edit_student(self):
        students = self.student_service.get_all_students()
        if not students:
            print("\nNo students found.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("STUDENT LIST".center(60))
        print("=" * 60)
        for idx, student in enumerate(students, 1):
            print(f"{idx}. [{student.username}] {student.name}")
        
        try:
            choice = int(input("\nSelect student number to edit: ").strip())
            if not (1 <= choice <= len(students)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            student = students[choice - 1]
            status = input("Academic Status: ").strip()
            
            if status:
                student.status = status
                self.student_service.update_student(student)
                print(f"\n✓ Success: Updated student '{student.username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _delete_student(self):
        students = self.student_service.get_all_students()
        if not students:
            print("\nNo students found.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("STUDENT LIST".center(60))
        print("=" * 60)
        for idx, student in enumerate(students, 1):
            print(f"{idx}. [{student.username}] {student.name}")
        
        try:
            choice = int(input("\nSelect student number to delete: ").strip())
            if not (1 <= choice <= len(students)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            student = students[choice - 1]
            confirm = input(f"Delete '{student.name}'? (Y/N): ").strip().upper()
            
            if confirm == "Y":
                self.student_service.delete_student(student.id)
                print("\n✓ Deleted.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _list_all_lecturers(self):
        lecturers = self.lecturer_service.get_all_lecturers()
        print("\n" + "=" * 60)
        print("LECTURER LIST".center(60))
        print("=" * 60)
        if not lecturers:
            print("No lecturers found.")
        else:
            for idx, lecturer in enumerate(lecturers, 1):
                print(f"{idx}. [{lecturer.username}] {lecturer.name} - {lecturer.department}")
        input("\nPress Enter to continue...")
    
    def _add_lecturer(self):
        user_id = input("UserID: ").strip()
        username = input("Enter Username: ").strip()
        password = input("Password: ").strip()
        name = input("Lecturer Name: ").strip()
        department = input("Department: ").strip()
        
        try:
            lecturer = self.lecturer_service.create_lecturer(user_id, username, password, name, department)
            print(f"\n✓ Success: Created lecturer '{username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _edit_lecturer(self):
        lecturers = self.lecturer_service.get_all_lecturers()
        if not lecturers:
            print("\nNo lecturers found.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("LECTURER LIST".center(60))
        print("=" * 60)
        for idx, lecturer in enumerate(lecturers, 1):
            print(f"{idx}. [{lecturer.username}] {lecturer.name}")
        
        try:
            choice = int(input("\nSelect lecturer number to edit: ").strip())
            if not (1 <= choice <= len(lecturers)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            lecturer = lecturers[choice - 1]
            department = input("Enter NEW Department...: ").strip()
            
            if department:
                lecturer.department = department
                self.lecturer_service.update_lecturer(lecturer)
                print(f"\n✓ Success: Updated lecturer '{lecturer.username}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _delete_lecturer(self):
        lecturers = self.lecturer_service.get_all_lecturers()
        if not lecturers:
            print("\nNo lecturers found.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("LECTURER LIST".center(60))
        print("=" * 60)
        for idx, lecturer in enumerate(lecturers, 1):
            print(f"{idx}. [{lecturer.username}] {lecturer.name}")
        
        try:
            choice = int(input("\nSelect lecturer number to delete: ").strip())
            if not (1 <= choice <= len(lecturers)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            lecturer = lecturers[choice - 1]
            confirm = input(f"Delete '{lecturer.name}'? (Y/N): ").strip().upper()
            
            if confirm == "Y":
                self.lecturer_service.delete_lecturer(lecturer.id)
                print("\n✓ Deleted.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _list_all_subjects(self):
        subjects = self.subject_service.get_all_subjects()
        print("\n" + "=" * 60)
        print("SUBJECT LIST".center(60))
        print("=" * 60)
        if not subjects:
            print("No subjects found.")
        else:
            for idx, subject in enumerate(subjects, 1):
                print(f"{idx}. [{subject.code}] {subject.name} - {subject.credits} credits")
        input("\nPress Enter to continue...")
    
    def _add_subject(self):
        code = input("Enter Subject Code: ").strip()
        name = input("Enter Subject Name: ").strip()
        credits = input("Enter Credits: ").strip()
        
        try:
            credits_int = int(credits) if credits else 0
            subject = self.subject_service.create_subject(code, name, credits_int)
            print(f"\n✓ Success: Added subject '{code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _edit_subject(self):
        subjects = self.subject_service.get_all_subjects()
        if not subjects:
            print("\nNo subjects found.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("SUBJECT LIST".center(60))
        print("=" * 60)
        for idx, subject in enumerate(subjects, 1):
            print(f"{idx}. [{subject.code}] {subject.name}")
        
        try:
            choice = int(input("\nSelect subject number to edit: ").strip())
            if not (1 <= choice <= len(subjects)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            subject = subjects[choice - 1]
            name = input("Enter NEW Name...: ").strip()
            credits = input("Enter NEW Credits...: ").strip()
            
            name_new = name if name else None
            credits_new = int(credits) if credits else None
            
            self.subject_service.update_subject(subject, name_new, credits_new)
            print(f"\n✓ Success: Updated subject '{subject.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _delete_subject(self):
        subjects = self.subject_service.get_all_subjects()
        if not subjects:
            print("\nNo subjects found.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("SUBJECT LIST".center(60))
        print("=" * 60)
        for idx, subject in enumerate(subjects, 1):
            print(f"{idx}. [{subject.code}] {subject.name}")
        
        try:
            choice = int(input("\nSelect subject number to delete: ").strip())
            if not (1 <= choice <= len(subjects)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            subject = subjects[choice - 1]
            confirm = input(f"Delete '{subject.name}'? (Y/N): ").strip().upper()
            
            if confirm == "Y":
                self.subject_service.delete_subject(subject.id)
                print(f"\n✓ Success: Deleted subject '{subject.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _list_all_classes(self):
        classes = self.class_service.get_all_classes()
        print("\n" + "=" * 60)
        print("CLASS LIST".center(60))
        print("=" * 60)
        if not classes:
            print("No classes found.")
        else:
            for idx, cls in enumerate(classes, 1):
                subject = self.subject_service.get_subject_by_code(cls.subject_code)
                subject_name = subject.name if subject else cls.subject_code
                print(f"{idx}. [{cls.code}] {subject_name} - {cls.schedule} at {cls.room} ({cls.current_count}/{cls.max_students})")
        input("\nPress Enter to continue...")
    
    def _add_class(self):
        code = input("Enter Class Code: ").strip()
        subject_code = input("Enter Subject Code: ").strip()
        lecturer_username = input("Enter Lecturer Username: ").strip()
        room = input("Enter Room: ").strip()
        schedule = input("Enter Schedule (e.g., Mon 7-9): ").strip()
        max_students = input("Max Students (default 50): ").strip()
        
        try:
            max_students_int = int(max_students) if max_students else 50
            class_obj = self.class_service.create_class(
                code, subject_code, lecturer_username, room, schedule, max_students_int
            )
            print(f"\n✓ Success: Added new class.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _edit_class(self):
        classes = self.class_service.get_all_classes()
        if not classes:
            print("\nNo classes found.")
            input("\nPress Enter tocontinue...")
            return
        
        print("\n" + "=" * 60)
        print("CLASS LIST".center(60))
        print("=" * 60)
        for idx, cls in enumerate(classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name}")
        
        try:
            choice = int(input("\nSelect class number to edit: ").strip())
            if not (1 <= choice <= len(classes)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            class_obj = classes[choice - 1]
            room = input("Enter new Room: ").strip()
            schedule = input("Enter new Schedule (Enter to skip): ").strip()
            
            room_new = room if room else None
            schedule_new = schedule if schedule else None
            
            self.class_service.update_class(class_obj, room_new, schedule_new)
            print(f"\n✓ Success: Updated class '{class_obj.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")
    
    def _delete_class(self):
        classes = self.class_service.get_all_classes()
        if not classes:
            print("\nNo classes found.")
            input("\nPress Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("CLASS LIST".center(60))
        print("=" * 60)
        for idx, cls in enumerate(classes, 1):
            subject = self.subject_service.get_subject_by_code(cls.subject_code)
            subject_name = subject.name if subject else cls.subject_code
            print(f"{idx}. [{cls.code}] {subject_name}")
        
        try:
            choice = int(input("\nSelect class number to delete: ").strip())
            if not (1 <= choice <= len(classes)):
                print("\n✗ Invalid number.")
                input("\nPress Enter to continue...")
                return
            
            class_obj = classes[choice - 1]
            subject = self.subject_service.get_subject_by_code(class_obj.subject_code)
            subject_name = subject.name if subject else class_obj.code
            confirm = input(f"Delete '{subject_name}'? (Y/N): ").strip().upper()
            
            if confirm == "Y":
                self.class_service.delete_class(class_obj.id)
                print(f"\n✓ Success: Deleted class '{class_obj.code}'.")
        except ValueError as e:
            print(f"\n✗ {e}")
        
        input("\nPress Enter to continue...")