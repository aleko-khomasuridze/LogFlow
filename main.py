from logflow.models import Log
from logflow.logger import Logger
from logflow.models.enums.log_type import LogTypes
from logflow.formatters.impl import *

dictFormatter: DictFormatter = DictFormatter()
formattedLog = dictFormatter.format(Log(LogTypes.INFO, "This is an info log message."))
print(formattedLog["message"])

jsonFormatter: JsonFormatter = JsonFormatter(indent=4)
jsonLog = jsonFormatter.format(Log(LogTypes.ERROR, "This is an error log message."))
print(jsonLog)

logger = Logger()
logger.log(Log(LogTypes.SUCCESS, 'test log message'))
logger.log(Log(LogTypes.INFO, 'test log message'))
logger.log(Log(LogTypes.DEBUG, 'test log message'))
logger.log(Log(LogTypes.WARNING, 'test log message'))
logger.log(Log(LogTypes.ERROR, 'test log message'))
logger.log(Log(LogTypes.FATAL, 'test log message'))
