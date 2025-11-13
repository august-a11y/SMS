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
	string fullName;
    string academicStatus;
	vector<Schedule> schedules;
    vector<Grade> grades; 
    
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
	string getFullName();
	void setFullName(const string& name);
    void setFaculty(const string& faculty);
    void setGender(const string& gender);
    void setAddress(const Address& addr);
    void setMajor(const string& major);
    void setDateOfBirth(const string& dob);
    void setGPA(float gpa);
    void setAcademicStatus(const string& status);
    void setEnrollmentYear(int year);
    void RegisterCourses();
    void ViewSchedule();
    void ViewGrades();
};