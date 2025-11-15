from typing import Optional
from src.models.subject import Subject
from src.repositories.base_repository import BaseRepository


class SubjectRepository(BaseRepository[Subject]):
    def find_by_code(self, code: str) -> Optional[Subject]:
        for subject in self.get_all():
            if subject.code.upper() == code.upper():
                return subject
        return None

