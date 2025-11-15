"""
Notification Service - Open/Closed Principle và Liskov Substitution Principle
Có thể mở rộng thêm loại notification mới mà không cần sửa code cũ
"""
from abc import ABC
from src.interfaces.notification_interface import INotification


class NotificationService(INotification, ABC):
    """
    Base notification service
    Open/Closed Principle - mở để mở rộng, đóng để sửa đổi
    """
    
    def send(self, recipient: str, message: str) -> bool:
        """Base implementation - should be overridden"""
        raise NotImplementedError("Subclass must implement send method")


class EmailNotification(NotificationService):
    """
    Email notification implementation
    Liskov Substitution Principle - có thể thay thế NotificationService
    """
    
    def send(self, recipient: str, message: str) -> bool:
        """Send email notification"""
        print(f"[EMAIL] To: {recipient}")
        print(f"[EMAIL] Message: {message}")
        print(f"[EMAIL] ✓ Email sent successfully")
        return True


class SMSNotification(NotificationService):
    """
    SMS notification implementation
    Liskov Substitution Principle - có thể thay thế NotificationService
    """
    
    def send(self, recipient: str, message: str) -> bool:
        """Send SMS notification"""
        print(f"[SMS] To: {recipient}")
        print(f"[SMS] Message: {message}")
        print(f"[SMS] ✓ SMS sent successfully")
        return True

