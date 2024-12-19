from format_enums import DateTimeFormat
from models import Log

class LogFormater:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LogFormater, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, date_time_format: DateTimeFormat = DateTimeFormat.FULL):
        if not hasattr(self, '__date_time_format'):
            self.__date_time_format = date_time_format
    
    def fromat(self, log: Log) -> str:
        return (
            f'[{log.get_level()}]-
            [{log.get_date_time()}]: 
            {log.get_message()}'
        )
        
logFormater: LogFormater = LogFormater(DateTimeFormat.EU)
        