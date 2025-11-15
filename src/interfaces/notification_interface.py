from abc import ABC, abstractmethod


class INotification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

