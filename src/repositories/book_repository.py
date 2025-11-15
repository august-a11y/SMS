"""
Book Repository - Single Responsibility Principle
Chỉ chịu trách nhiệm về thao tác dữ liệu sách
"""
from typing import List, Optional
from src.models.book import Book
from src.repositories.base_repository import BaseRepository


class BookRepository(BaseRepository[Book]):
    """
    Book repository implementation
    Single Responsibility Principle - chỉ quản lý dữ liệu sách
    Liskov Substitution Principle - có thể thay thế BaseRepository
    """
    
    def find_by_title(self, title: str) -> Optional[Book]:
        """Find book by exact title match"""
        for book in self.get_all():
            if book.title.lower() == title.lower():
                return book
        return None
    
    def search_by_title(self, title: str) -> List[Book]:
        """Search books by title (partial match)"""
        return [book for book in self.get_all() 
                if title.lower() in book.title.lower()]
    
    def find_by_author(self, author: str) -> List[Book]:
        """Find books by author"""
        return [book for book in self.get_all() if book.author.lower() == author.lower()]
    
    def find_available_books(self) -> List[Book]:
        """Find all available books"""
        return [book for book in self.get_all() if book.is_available]
    
    def find_borrowed_books(self) -> List[Book]:
        """Find all borrowed books"""
        return [book for book in self.get_all() if not book.is_available]

