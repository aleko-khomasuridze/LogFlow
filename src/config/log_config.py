from src.formatters import DateTimeFormat

class LogConfig:
    LOG_TO_CONSOLE = True
    LOG_TO_FILE = True
    LOG_FILE_PATH = 'logs/app.log'
    DATETIME_FORMAT = DateTimeFormat.ISO
