from src.models.log import Log
from src.logger import Logger
from src.models.enums.logtype import LogTypes

logger = Logger()
logger.log(Log(LogTypes.ERROR, 'test log message'))
