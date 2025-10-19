from dataclasses import dataclass

from .logcolors import LogColors
from .loglevel import LogLevel


@dataclass(frozen=True)
class LogType:
    """Mapping between a :class:`LogLevel` and the colour it should be displayed with."""

    log_level: LogLevel
    log_color: LogColors


class LogTypes:
    """Predefined collection of useful log types."""

    ERROR = LogType(LogLevel.ERROR, LogColors.ERROR)
    WARNING = LogType(LogLevel.WARNING, LogColors.WARNING)
    INFO = LogType(LogLevel.INFO, LogColors.INFO)
    FATAL = LogType(LogLevel.FATAL, LogColors.FATAL)
    SUCCESS = LogType(LogLevel.SUCCESS, LogColors.SUCCESS)


__all__ = ["LogType", "LogTypes"]
