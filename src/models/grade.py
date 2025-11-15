from dataclasses import dataclass
from typing import Optional


@dataclass
class Grade:
    id: Optional[int]
    student_username: str
    class_code: str
    midterm_score: Optional[float] = None
    final_score: Optional[float] = None
    
    @property
    def total_score(self) -> Optional[float]:
        if self.midterm_score is None or self.final_score is None:
            return None
        return round(self.midterm_score * 0.3 + self.final_score * 0.7, 1)
    
    def __str__(self) -> str:
        mid = self.midterm_score if self.midterm_score is not None else "N/A"
        final = self.final_score if self.final_score is not None else "N/A"
        total = self.total_score if self.total_score is not None else "N/A"
        return f"Grade(student='{self.student_username}', class='{self.class_code}', Giữa kỳ: {mid}, Cuối kỳ: {final}, Tổng: {total})"

