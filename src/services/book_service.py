"""
Book Service - Single Responsibility Principle và Dependency Inversion Principle
Chỉ chịu trách nhiệm về logic nghiệp vụ sách
Phụ thuộc vào abstraction (IRepository, INotification), không phụ thuộc vào concrete class
"""
from datetime import datetime
from typing import Optional
from src.models.book import Book
from src.models.user import User
from src.interfaces.repository_interface import IRepository
from src.interfaces.notification_interface import INotification


class BookService:
    """
    Book service - business logic for books
    Single Responsibility Principle - chỉ xử lý logic nghiệp vụ sách
    Dependency Inversion Principle - phụ thuộc vào abstraction
    """
    
    def __init__(
        self,
        book_repository: IRepository[Book],
        user_repository: IRepository[User],
        notification_service: INotification
    ):
        """
        Dependency Injection - nhận dependencies qua constructor
        Dependency Inversion Principle - phụ thuộc vào abstraction
        """
        self._book_repository = book_repository
        self._user_repository = user_repository
        self._notification_service = notification_service
    
    def add_book(self, title: str, author: str, isbn: str) -> Book:
        """Add a new book to the library"""
        # Kiểm tra ISBN đã tồn tại chưa
        existing_books = self._book_repository.get_all()
        for book in existing_books:
            if book.isbn == isbn:
                raise ValueError(f"Book with ISBN {isbn} already exists")
        
        book = Book(id=None, title=title, author=author, isbn=isbn)
        return self._book_repository.create(book)
    
    def borrow_book(self, book_id: int, user_id: int) -> Book:
        """Borrow a book"""
        book = self._book_repository.get_by_id(book_id)
        if not book:
            raise ValueError(f"Book with id {book_id} not found")
        
        if not book.is_available:
            raise ValueError(f"Book '{book.title}' is already borrowed")
        
        user = self._user_repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        
        # Update book status
        book.is_available = False
        book.borrowed_by = user_id
        book.borrowed_date = datetime.now()
        self._book_repository.update(book)
        
        # Update user's borrowed books list
        if book_id not in user.borrowed_books:
            user.borrowed_books.append(book_id)
        self._user_repository.update(user)
        
        # Send notification
        message = f"You have successfully borrowed '{book.title}' by {book.author}"
        self._notification_service.send(user.email, message)
        
        return book
    
    def return_book(self, book_id: int, user_id: int) -> Book:
        """Return a borrowed book"""
        book = self._book_repository.get_by_id(book_id)
        if not book:
            raise ValueError(f"Book with id {book_id} not found")
        
        if book.is_available:
            raise ValueError(f"Book '{book.title}' is not borrowed")
        
        if book.borrowed_by != user_id:
            raise ValueError(f"Book '{book.title}' is not borrowed by user {user_id}")
        
        user = self._user_repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        
        # Update book status
        book.is_available = True
        book.borrowed_by = None
        book.borrowed_date = None
        self._book_repository.update(book)
        
        # Update user's borrowed books list
        if book_id in user.borrowed_books:
            user.borrowed_books.remove(book_id)
        self._user_repository.update(user)
        
        # Send notification
        message = f"You have successfully returned '{book.title}' by {book.author}"
        self._notification_service.send(user.email, message)
        
        return book
    
    def get_available_books(self) -> list[Book]:
        """Get all available books"""
        if hasattr(self._book_repository, 'find_available_books'):
            return self._book_repository.find_available_books()
        return [book for book in self._book_repository.get_all() if book.is_available]
    
    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Get book by ID"""
        return self._book_repository.get_by_id(book_id)
    
    def search_books_by_title(self, title: str) -> list[Book]:
        """Search books by title (supports partial matching)"""
        if hasattr(self._book_repository, 'search_by_title'):
            return self._book_repository.search_by_title(title)
        return [book for book in self._book_repository.get_all() 
                if title.lower() in book.title.lower()]

