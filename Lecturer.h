#pragma once
#include "User.h"
#include "Address.h"
#include "Schedule.h"
#include <vector>
#include <string>

using namespace std;

class Schedule; 

class Lecturer : public User {
private:
    string faculty;
    string specialization;
    string gender;
    string dateOfBirth;
    Address address; 
	vector<Schedule> schedules;
  
    
public:
    Lecturer(string id, string pass);
    string getFaculty();
    string getSpecialization();
    void setFaculty(const string& faculty);
    void setSpecialization(const string& specialization);
    string getGender();
    void setGender(const string& gender);
    string getDateOfBirth();
    void setDateOfBirth(const string& dob);
    Address getAddress();
    void setAddress(const Address& addr);
    
    void EnterGrades(string classID, string studentID, float score);
    vector<Schedule> ViewSchedule();
};