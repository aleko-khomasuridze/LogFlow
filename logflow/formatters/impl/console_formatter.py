from __future__ import annotations

from typing import Optional

from ..formatter import Formatter
from ..enums import DateTimeFormat
from ...models import Log, LogColors
from ...config import LogConfig


class ConsoleFormatter(Formatter):
    def __init__(self, date_time_format: DateTimeFormat = LogConfig.LOG_DATE_TIME_FORMAT):
        self.__date_time_format = date_time_format

    def set_date_time_format(self, date_time_format: DateTimeFormat) -> None:
        self.__date_time_format = date_time_format

    def get_date_time_format(self) -> DateTimeFormat:
        return self.__date_time_format
    
    def format(self, log: Log) -> str:
        color = log.get_color().value if isinstance(log.get_color(), LogColors) else str(log.get_color())
        reset = LogColors.RESET.value
        level = log.get_level().value if hasattr(log.get_level(), "value") else str(log.get_level())
        date_time = log.get_date_time().strftime(self.__date_time_format.value)
        message = log.get_message()
        return f"{color}[{level}]-[{date_time}]{reset}: {message}"

