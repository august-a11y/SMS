#include "User.h"
#include <iostream>


using namespace std;


bool User::Login(const string& enteredID, const string& enteredPass) {
    if (this->password == enteredPass) {
        return true;
    }
    return false;
}

void User::ChangePassword(const string& newPassword) {
    this->password = newPassword;
    cout << "Da thay doi mat khau cho user: " << this->userID << endl;
}

void User::Logout() {
    
    cout << "User " << this->userID << " da dang xuat." << endl;
}