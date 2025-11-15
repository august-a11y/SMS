from typing import Generic, TypeVar, Optional, List, Dict
from src.interfaces.repository_interface import IRepository

T = TypeVar('T')


class BaseRepository(IRepository[T], Generic[T]):
    def __init__(self):
        self._storage: Dict[int, T] = {}
        self._next_id = 1
    
    def create(self, entity: T) -> T:
        if not hasattr(entity, 'id') or getattr(entity, 'id') is None:
            entity.id = self._next_id
            self._next_id += 1
        
        entity_id = getattr(entity, 'id')
        self._storage[entity_id] = entity
        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[T]:
        """Get entity by ID"""
        return self._storage.get(entity_id)
    
    def get_all(self) -> List[T]:
        """Get all entities"""
        return list(self._storage.values())
    
    def update(self, entity: T) -> T:
        """Update an existing entity"""
        entity_id = getattr(entity, 'id')
        if entity_id not in self._storage:
            raise ValueError(f"Entity with id {entity_id} not found")
        self._storage[entity_id] = entity
        return entity
    
    def delete(self, entity_id: int) -> bool:
        """Delete an entity by ID"""
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False

