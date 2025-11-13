#include "Lecturer.h"
#include "Schedule.h"
#include <iostream>


using namespace std;

void Lecturer::EnterGrades(string classID, string studentID, float score) {
    
}

vector<Schedule> Lecturer::ViewSchedule() {
	vector<Schedule> mySchedule = this->schedules;
    for(Schedule s : mySchedule) {
        cout << "Class ID: " << s.classID << ", Day: " << s.dayOfWeek 
             << ", Time: " << s.startTime << " - " << s.endTime 
             << ", Room: " << s.room << endl;
	}
}