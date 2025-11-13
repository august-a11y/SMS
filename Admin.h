#pragma once
#include "User.h"
#include <string>

using namespace std;

class Student ;
class Lecturer ;

class Admin : public User {
private:
    string department;
    string position;

public:
    Admin(string id, string pass);

   
    void ManageStudents();
    void ManageLecturers();
    void CreateAccount();
    void ManageCourses();
    void ManageSchedule();
};