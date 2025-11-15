from dataclasses import dataclass
from typing import Optional


@dataclass
class Subject:
    id: Optional[int]
    code: str
    name: str
    credits: int
    
    def __str__(self) -> str:
        return f"Subject(id={self.id}, code='{self.code}', name='{self.name}', credits={self.credits})"

