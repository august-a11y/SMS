#include "Student.h"
#include "Schedule.h" 
#include <iostream>

using namespace std;
void Student::RegisterCourses() {
    // Logic thực tế:
    // 1. Hiển thị các môn học (từ DataManager)
    // 2. Cho sinh viên chọn
    // 3. Thêm sinh viên vào SchoolClass tương ứng
    cout << "-> " << this->getID() << " dang thuc hien chuc nang [Dang ky mon hoc]..." << endl;
    cout << "(Chuc nang chua duoc implement)" << endl;
}

vector<Schedule> Student::ViewSchedule() {
    // Logic thực tế:
    // 1. Lấy danh sách các SchoolClass mà sinh viên này đã đăng ký
    // 2. Lặp qua các class đó, lấy Schedule của chúng
    // 3. Trả về một vector chứa các Schedule
    cout << "-> " << this->getID() << " dang thuc hien chuc nang [Xem thoi khoa bieu]..." << endl;
    cout << "(Chuc nang chua duoc implement)" << endl;
    
    vector<Schedule> mySchedule;
    // ... them logic o day
    return mySchedule;
}

vector<Grade> Student::ViewGrades() {
    // Logic thực tế:
    // 1. Lấy danh sách các Grade từ vector<Grade*>
    // 2. Trả về một vector<Grade> (không phải con trỏ)
    cout << "-> " << this->getID() << " dang thuc hien chuc nang [Xem diem]..." << endl;
    cout << "(Chuc nang chua duoc implement)" << endl;
    
    vector<Grade> myGrades;
    // ... them logic o day
    return myGrades;
}