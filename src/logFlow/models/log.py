from enums import LogColors
from ..levels.loglevel import LogLevel

class Log:
    def __init__(self, color: LogColors, level: LogLevel, message: str):
        self.__color = color
        self.__level = level
        self.__message = message
        
    def get_color(self) -> LogColors:
        return self.__color
        
    def get_level(self) -> LogLevel:
        return self.__level
    
    def get_message(self) -> str:
        return self.__message
    
    def __str__(self) -> str:
        return f'{{color: {self.__color}, level: {self.__level}, message: {self.__message}}}'
