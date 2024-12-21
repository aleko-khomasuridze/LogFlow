from models import Log
from handlers import Handler
from datetime import datetime
from handlers.impl import ConsoleHandler

class Logger:
    def __init__(self):
        self.__handlers = [
            ConsoleHandler()
        ]
        # self.__datetime = datetime.now()
        
    def add_handler(self, handler: Handler) -> None:
        self.__handlers.append(handler)
        
    def add_handlers_all(self, handlers: list) -> None:
        for handler in handlers:
            self.__handlers.append(handler)
            
    def remove_handler(self, target_handler: Handler) -> None:
        self.__handlers.remove(target_handler)
        
    def log(self, log: Log) -> None:
        for handler in self.__handlers:
            handler.handle(log)
            
