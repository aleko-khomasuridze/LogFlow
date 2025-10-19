from logFlow.models.log import Log
from logFlow.logger import Logger
from logFlow.models.enums.logtype import LogTypes

logger = Logger()
logger.log(Log(LogTypes.ERROR, 'test log message'))
