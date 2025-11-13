#pragma once
#include <string>

using namespace std;

class User {
protected: 
    string userID;
    string password;
    string email;
    string phone;
    string role;

public:
    User(string id, string pass, string role);
    virtual ~User() {} 

    bool Login(const string& enteredID, const string& enteredPass);
    void ChangePassword(const string& newPassword);
    void Logout();
    string getRole() const { return role; }
    string getID() const { return userID; }
};