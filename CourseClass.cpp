#include "CourseClass.h"
#include "Student.h"    
#include "Lecturer.h"   
#include "Course.h"     
#include <algorithm>    
#include <iostream>

using namespace std;

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



vector<Student*> CourseClass::GetStudentList() {
	int i = 1;
    for(Student* s : students) {
        cout << i << ": " << s->getFullName() << endl;
		i++;
	}

}