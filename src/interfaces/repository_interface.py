from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')


class IRepository(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity: T) -> T:
        pass
    
    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[T]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[T]:
        pass
    
    @abstractmethod
    def update(self, entity: T) -> T:
        pass
    
    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        pass

