from typing import List, Optional
from src.models.subject import Subject
from src.interfaces.repository_interface import IRepository


class SubjectService:
    def __init__(self, subject_repository: IRepository[Subject]):
        self._subject_repository = subject_repository
    
    def create_subject(self, code: str, name: str, credits: int) -> Subject:
        if hasattr(self._subject_repository, 'find_by_code'):
            existing = self._subject_repository.find_by_code(code)
            if existing:
                raise ValueError(f"Error: Subject code '{code}' already exists.")
        
        subject = Subject(id=None, code=code, name=name, credits=credits)
        return self._subject_repository.create(subject)
    
    def get_all_subjects(self) -> List[Subject]:
        return self._subject_repository.get_all()
    
    def update_subject(self, subject: Subject, name: Optional[str] = None, credits: Optional[int] = None) -> Subject:
        if name is not None:
            subject.name = name
        if credits is not None:
            subject.credits = credits
        return self._subject_repository.update(subject)
    
    def delete_subject(self, subject_id: int) -> bool:
        return self._subject_repository.delete(subject_id)
    
    def get_subject_by_code(self, code: str) -> Optional[Subject]:
        if hasattr(self._subject_repository, 'find_by_code'):
            return self._subject_repository.find_by_code(code)
        return None