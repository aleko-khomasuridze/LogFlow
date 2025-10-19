from __future__ import annotations

from typing import Optional

from .format_enums import DateTimeFormat
from ..models import Log, LogColors


class LogFormatter:
    """Pretty printer used by the built-in handlers."""

    _instance: Optional["LogFormatter"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, date_time_format: DateTimeFormat = DateTimeFormat.FULL):
        if getattr(self, "__initialized", False):
            return

        self.__date_time_format = date_time_format
        self.__initialized = True

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


# Backwards compatibility with the previous public name
LogFormater = LogFormatter


logFormater: LogFormatter = LogFormatter(DateTimeFormat.EU)


__all__ = ["LogFormatter", "LogFormater", "logFormater"]