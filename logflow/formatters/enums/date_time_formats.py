from enum import Enum

class DateTimeFormat(Enum):
    """Enum for standard datetime formats."""
    ISO = "%Y-%m-%dT%H:%M:%S"
    US = "%m/%d/%Y %I:%M %p"
    EU = "%d/%m/%Y %H:%M"
    SIMPLE = "%Y-%m-%d"
    FULL = "%A, %B %d, %Y %H:%M:%S"
    SHORT_TIME = "%H:%M"
