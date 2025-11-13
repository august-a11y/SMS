#include "Student.h"
#include "Schedule.h" 
#include "Grade.h"
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

void Student::ViewSchedule() {
	vector<Schedule> mySchedule = this->schedules;
    for(Schedule s : mySchedule) {
        cout << "Class ID: " << s.classID << ", Day: " << s.dayOfWeek 
             << ", Time: " << s.startTime << " - " << s.endTime 
             << ", Room: " << s.room << endl;
	}
}

void Student::ViewGrades() {
	
}