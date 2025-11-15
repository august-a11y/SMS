"""
Book model - Single Responsibility Principle
Chỉ chịu trách nhiệm lưu trữ thông tin về sách
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Book:
    """Book entity - chỉ chứa dữ liệu, không có logic nghiệp vụ"""
    id: int
    title: str
    author: str
    isbn: str
    is_available: bool = True
    borrowed_by: Optional[int] = None  # User ID
    borrowed_date: Optional[datetime] = None
    
    def __str__(self) -> str:
        status = "Available" if self.is_available else f"Borrowed by user {self.borrowed_by}"
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', {status})"

