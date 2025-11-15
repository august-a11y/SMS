from dataclasses import dataclass
from typing import Optional
from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    STUDENT = "student"
    LECTURER = "lecturer"


@dataclass
class User:
    id: Optional[int]
    username: str
    password: str
    role: UserRole
    user_id: str
    name: str
    
    def __str__(self) -> str:
        return f"User(id={self.id}, username='{self.username}', role={self.role.value}, name='{self.name}')"


@dataclass
class Student(User):
    status: str = "Đang học"
    registered_classes: list[str] = None
    
    def __post_init__(self):
        if self.registered_classes is None:
            self.registered_classes = []
        if self.role != UserRole.STUDENT:
            self.role = UserRole.STUDENT
    
    def __str__(self) -> str:
        return f"Student(id={self.id}, username='{self.username}', user_id='{self.user_id}', name='{self.name}', status='{self.status}')"


@dataclass
class Lecturer(User):
    department: str = ""
    
    def __post_init__(self):
        if self.role != UserRole.LECTURER:
            self.role = UserRole.LECTURER
    
    def __str__(self) -> str:
        return f"Lecturer(id={self.id}, username='{self.username}', user_id='{self.user_id}', name='{self.name}', department='{self.department}')"


@dataclass
class Admin(User):
    """Admin entity - kế thừa từ User"""
    
    def __post_init__(self):
        if self.role != UserRole.ADMIN:
            self.role = UserRole.ADMIN
    
    def __str__(self) -> str:
        return f"Admin(id={self.id}, username='{self.username}', name='{self.name}')"
