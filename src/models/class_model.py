from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Class:
    id: Optional[int]
    code: str
    subject_code: str
    lecturer_username: str
    room: str
    schedule: str
    max_students: int
    enrolled_students: List[str] = None
    
    def __post_init__(self):
        if self.enrolled_students is None:
            self.enrolled_students = []
    
    @property
    def current_count(self) -> int:
        return len(self.enrolled_students)
    
    @property
    def is_full(self) -> bool:
        return self.current_count >= self.max_students
    
    def __str__(self) -> str:
        return f"Class(id={self.id}, code='{self.code}', subject='{self.subject_code}', room='{self.room}', schedule='{self.schedule}', {self.current_count}/{self.max_students})"

