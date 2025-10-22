from src.models.log import Log
from src.logger import Logger
from src.models.enums.log_type import LogTypes
from src.formaters import JsonFormatter

jsonFormatter: JsonFormatter = JsonFormatter(indent=4)
jsonLog = jsonFormatter.format(Log(LogTypes.ERROR, "This is an error log message."))
print(jsonLog["message"])

logger = Logger()
logger.log(Log(LogTypes.SUCCESS, 'test log message'))
logger.log(Log(LogTypes.INFO, 'test log message'))
logger.log(Log(LogTypes.DEBUG, 'test log message'))
logger.log(Log(LogTypes.WARNING, 'test log message'))
logger.log(Log(LogTypes.ERROR, 'test log message'))
logger.log(Log(LogTypes.FATAL, 'test log message'))
