from src.models.log import Log
from src.logger import Logger
<<<<<<< Updated upstream
from src.models.enums.logtype import LogTypes
from src.formaters import JsonFormatter
=======
from src.models import LogTypes
from src.config import LogConfig
from src.formatters import DateTimeFormat
from src.formatters import JsonFormatter
from src.formatters import DictFormater
>>>>>>> Stashed changes

jsonFormatter: JsonFormatter = JsonFormatter(indent=4)
jsonLog = jsonFormatter.format(Log(LogTypes.ERROR, "This is an error log message."))
print(jsonLog)

dictFormatter: DictFormater = DictFormater()
dictLog = dictFormatter.format(Log(LogTypes.INFO, "This is an info log message."))
print(dictLog["message"])

LogConfig.DATETIME_FORMAT = DateTimeFormat.FULL

logger = Logger()
logger.log(Log(LogTypes.SUCCESS, 'test log message'))
logger.log(Log(LogTypes.INFO, 'test log message'))
logger.log(Log(LogTypes.DEBUG, 'test log message'))
logger.log(Log(LogTypes.WARNING, 'test log message'))
logger.log(Log(LogTypes.ERROR, 'test log message'))
logger.log(Log(LogTypes.FATAL, 'test log message'))
