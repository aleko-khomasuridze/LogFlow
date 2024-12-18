from enums import LogColor, LogLevel, LogType
from datetime import datetime

class Log:
    def __init__(self, type: LogType, message: str, date_time: datetime):
        self.__color: LogColor = type.log_color
        self.__level: LogLevel = type.log_level
        self.__message: str = message
        self.__date_time: datetime = date_time
        
    def get_color(self) -> LogColor:
        return self.__color
        
    def get_level(self) -> LogLevel:
        return self.__level
    
    def get_message(self) -> str:
        return self.__message
    
    def get_date_tiem(self) -> datetime:
        return self.__date_time

    def set_date_time(self, date_time: datetime) -> None:
        self.__date_time = date_time
        
            
    # def __str__(self) -> str:
    #     return f'{{color: {self.__color}, level: {self.__level}, message: {self.__message}}}'
