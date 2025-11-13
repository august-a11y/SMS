#pragma once
#include "User.h"
#include "Address.h"
#include "Grade.h" 
#include "Schedule.h" 
#include <vector>

using namespace std;

class Grade; 
class Schedule;

class Student : public User {
private:
    string faculty;
    string gender;
    int creditCompleted;
    string major;
    string dateOfBirth;
    float gpa;
    Address address;
    int enrollmentYear;
    string academicStatus;
    vector<Grade*> grades; 
    
public:
    
    Student(string id, string pass);
    string getMajor();
    string getDateOfBirth();
    float getGPA();
    string getAcademicStatus();
    int getEnrollmentYear();
    Address getAddress();
    string getFaculty();
    string getGender();
    void setFaculty(const string& faculty);
    void setGender(const string& gender);
    void setAddress(const Address& addr);
    void setMajor(const string& major);
    void setDateOfBirth(const string& dob);
    void setGPA(float gpa);
    void setAcademicStatus(const string& status);
    void setEnrollmentYear(int year);
    void RegisterCourses();
    vector<Schedule> ViewSchedule();
    vector<Grade> ViewGrades();
};