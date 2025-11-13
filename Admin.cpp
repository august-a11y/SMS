#include "Admin.h"
#include <iostream>
#include "Student.h"
#include "Lecturer.h"


using namespace std;


void Admin::ManageStudents() {
    cout << "menu:" << endl;
    cout << "1. View all" << endl;
    cout << "2. Delete" << endl;
    cout << "3. Update " << endl;
    cout << "4. Exit" << endl;
}

void Admin::ManageLecturers() {
    cout << "menu:" << endl;
    cout << "1. View all" << endl;
    cout << "2. Delete" << endl;
    cout << "3. Update " << endl;
    cout << "4. Exit" << endl;
}

void Admin::CreateAccount() {
    string id, pass, major, dateOfBirth, faculty, specialization;
    cout << "Who do you want to create an account for? (1. Student  2. Lecturer  ): ";
    string choice;
    getline(cin, choice);
    cout<<"UserID: ";
    getline(cin, id);
    cout<<"Password: ";
    getline(cin, pass);
    if(choice == "1") {
        cout<<"Major: ";
        getline(cin, major);
        cout<<"Faculty: ";
        getline(cin, faculty);
        cout<<"dateOfBirth: ";
        getline(cin, dateOfBirth);
        Student newStudent(id, pass);
        newStudent.setMajor(major);
        newStudent.setFaculty(faculty);
        newStudent.setDateOfBirth(dateOfBirth);
        cout<<"completed"<<endl;
    } else if(choice == "2") {
        cout<<"faculty: ";
        getline(cin, faculty);
        cout<<"specialization: ";
        getline(cin, specialization);
        Lecturer newLecturer(id, pass);
        newLecturer.setFaculty(faculty);
        newLecturer.setSpecialization(specialization);
        cout<<"completed"<<endl;
    } else {
        cout << "Lua chon khong hop le." << endl;
        return;
    }
}

void Admin::ManageCourses() {
    cout << "menu:" << endl;
    cout << "1. View all" << endl;
    cout << "2. Edit " << endl;
    cout << "3. Delete" << endl;
    cout << "4. Add " << endl;
    cout << "5. Exit" << endl;
}

void Admin::ManageSchedule() {
    cout << "menu:" << endl;
    cout << "1. View all" << endl;
    cout << "2. Edit " << endl;
    cout << "3. Delete" << endl;
    cout << "4. Add " << endl;
    cout << "5. Exit" << endl;
}