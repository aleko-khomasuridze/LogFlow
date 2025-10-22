import platform
from src.formatters import DateTimeFormat

os_name: str = platform.system()

_filepath = os_name.lower() == 'windows' and 'C:\\Logs\\app.log' or '/var/log/app.log'

class LogConfig:
    LOG_TO_CONSOLE = True
    LOG_TO_FILE = True
    LOG_FILE_PATH = _filepath
    LOG_DATE_TIME_FORMAT = DateTimeFormat.ISO 