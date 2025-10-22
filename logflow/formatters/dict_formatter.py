from logflow.formatters import DateTimeFormat
from logflow.config import LogConfig
from logflow.models import Log

class DictFormater:
    def __init__(self, date_time_format: DateTimeFormat = LogConfig.LOG_DATE_TIME_FORMAT):
        self.__date_time_format = date_time_format

    def get_date_time_format(self) -> DateTimeFormat:
        return self.__date_time_format
    
    def set_date_time_format(self, date_time_format: DateTimeFormat) -> None:
        self.__date_time_format = date_time_format

    def format(self, log: Log) -> dict:
        log_dict: dict = {
            "level": log.get_level().value,
            "message": log.get_message(),
            "timestamp": log.get_date_time()
        }
        return log_dict
