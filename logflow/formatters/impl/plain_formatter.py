from formatter import Formatter
from logflow.config import LogConfig
from logflow.models import Log
from logflow.formatters import DateTimeFormat

class PlainFormatter(Formatter):
    def __init__(self):
        pass
    
    def format(self, log: Log) -> str:
        timestamp = log.get_date_time().strftime(LogConfig.LOG_DATE_TIME_FORMAT)
        return f"[{timestamp}] [{log.get_level().name}] {log.get_message()}" 