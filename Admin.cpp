#include "Admin.h"
#include <iostream>
#include "Student.h"
#include "Lecturer.h"


using namespace std;


void Admin::ManageStudents() {
    while (true)
    {
        cout << "menu:" << endl;
        cout << "1. View all" << endl;
        cout << "2. Edit " << endl;
        cout << "3. Delete" << endl;
        cout << "4. Add " << endl;
        cout << "5. Exit" << endl;
        string choice;
        getline(cin, choice);
        switch (stoi(choice)) {
            case 1:
                // View all students
                break;
            case 2:
                // Edit student
                break;
            case 3:
                // Delete student
                break;
            case 4:
                // Add student
                break;
            case 5:
                return;
            default:
                cout << "Invalid choice. Please try again." << endl;
		}

    }
}

void Admin::ManageLecturers() {
    while (true)
    {
        cout << "menu:" << endl;
        cout << "1. View all" << endl;
        cout << "2. Edit " << endl;
        cout << "3. Delete" << endl;
        cout << "4. Add " << endl;
        cout << "5. Exit" << endl;
        string choice;
        getline(cin, choice);
        switch (stoi(choice)) {
        case 1:
            // View all lecturers
            break;
        case 2:
            // Edit lecturer
            break;
        case 3:
            // Delete lecturer
            break;
        case 4:
            // Add lecturer
            break;
        case 5:
            return;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }

    }
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
    while (true)
    {
        cout << "menu:" << endl;
        cout << "1. View all" << endl;
        cout << "2. Edit " << endl;
        cout << "3. Delete" << endl;
        cout << "4. Add " << endl;
        cout << "5. Exit" << endl;
        string choice;
        getline(cin, choice);
        switch (stoi(choice)) {
        case 1:
            // View all courses
            break;
        case 2:
            // Edit course
            break;
        case 3:
            // Delete course
            break;
        case 4:
            // Add course
            break;
        case 5:
            return;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }

    }
}

void Admin::ManageSchedule() {
    while (true)
    {
        cout << "menu:" << endl;
        cout << "1. View all" << endl;
        cout << "2. Edit " << endl;
        cout << "3. Delete" << endl;
        cout << "4. Add " << endl;
        cout << "5. Exit" << endl;
        string choice;
        getline(cin, choice);
        switch (stoi(choice)) {
        case 1:
            // View all schedules
            break;
        case 2:
            // Edit schedule
            break;
        case 3:
            // Delete schedule
            break;
        case 4:
            // Add schedule
            break;
        case 5:
            return;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }

    }
}