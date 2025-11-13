#pragma once
#include <string>
#include <vector>
#include "Schedule.h"
#include "Student.h"
#include "Lecturer.h"
#include "Course.h"

using namespace std;

class Student;
class Lecturer;

class CourseClass {
private:
    string classID;
    string className;
    string semester;
    string academicYear;
    int capacity;
    string status;

    
    Course* course;
    Lecturer* lecturer; 
    vector<Student*> students; 
    Schedule schedule; 

public:
    CourseClass(string id, Course* course);
    
    bool AddStudent(Student* student);
    vector<Student*> GetStudentList();
    void SetLecturer(Lecturer* lec);
    void SetSchedule(const Schedule& sched);
};