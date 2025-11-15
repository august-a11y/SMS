"""Interfaces package - Interface Segregation Principle"""

from .repository_interface import IRepository
from .notification_interface import INotification

__all__ = ["IRepository", "INotification"]

