#include "CourseClass.h"
#include "Student.h"    
#include "Lecturer.h"   
#include "Course.h"     
#include <algorithm>    

bool CourseClass::AddStudent(Student* student) {
    if (student == nullptr) return false;

    
    for (Student* s : students) {
        if (s->getID() == student->getID()) {
            return false; 
        }
    }

    students.push_back(student);
    return true;
}



string CourseClass::getCourseCode() const {
    if (course != nullptr) {
        return course->courseCode;
    }
    return ""; // Hoặc "N/A"
}

string CourseClass::getLecturerID() const {
    if (lecturer != nullptr) {
        return lecturer->getID();
    }
    return ""; // Hoặc "N/A"
}

vector<string> CourseClass::getStudentIDs() const {
    vector<string> ids;
    for (Student* s : students) {
        if (s != nullptr) {
            ids.push_back(s->getID());
        }
    }
    return ids;
}