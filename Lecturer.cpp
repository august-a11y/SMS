#include "Lecturer.h"
#include "Schedule.h"
#include <iostream>


using namespace std;

void Lecturer::EnterGrades(string classID, string studentID, float score) {
    // Logic thực tế:
    // 1. Tìm SchoolClass dựa trên classID
    // 2. Tìm Student trong lớp đó dựa trên studentID
    // 3. Cập nhật đối tượng Grade của sinh viên đó
    cout << "-> " << this->getID() << " dang thuc hien chuc nang [Nhap diem]..." << endl;
    cout << "(Chuc nang chua duoc implement)" << endl;
}

vector<Schedule> Lecturer::ViewSchedule() {
    // Logic thực tế:
    // 1. Lấy danh sách các SchoolClass mà giảng viên này dạy
    // 2. Trả về vector Schedule của các lớp đó
    cout << "-> " << this->getID() << " dang thuc hien chuc nang [Xem lich day]..." << endl;
    cout << "(Chuc nang chua duoc implement)" << endl;
    
    vector<Schedule> mySchedule;
    // ... them logic o day
    return mySchedule;
}