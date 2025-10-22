from ..formatter import Formatter
from ...models import Log
from ...formatters import DateTimeFormat

class FileFormatter(Formatter):
    def __init__(self, date_time_format: DateTimeFormat = DateTimeFormat.ISO):
        self.__date_time_format = date_time_format

    def format(self, log: Log) -> str:
        timestamp = log.get_date_time()
        timestamp_str = timestamp.strftime(self.__date_time_format.value)
        return f"[{timestamp_str}] [{log.get_level().name}] {log.get_message()}"
