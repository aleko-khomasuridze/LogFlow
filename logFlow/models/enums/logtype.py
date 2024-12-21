from . import LogColors
from . import LogLevel

class LogType:
    def __init__(self, log_level: LogLevel, log_color: LogColors):
        self._log_level = log_level
        self._log_color = log_color

    @property
    def log_color(self) -> LogColors:
        return self._log_color

    @property
    def log_level(self) -> LogLevel:
        return self._log_level

class LogTypes:
    ERROR = LogType(LogLevel.ERROR, LogColors.ERROR)
    WARNING = LogType(LogLevel.WARNING, LogColors.WARNING)
    INFO = LogType(LogLevel.INFO, LogColors.INFO)
    FATAL = LogType(LogLevel.FATAL, LogColors.FATAL)
    SUCCESS = LogType(LogLevel.SUCCESS, LogColors.SUCCESS)
