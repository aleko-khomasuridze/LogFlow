from abc import ABC, abstractmethod
from models import Log

class Handler(ABC):
    @abstractmethod
    def handle(self, log: Log) -> None:
        pass