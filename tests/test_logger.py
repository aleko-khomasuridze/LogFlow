from logFlow import Logger, LogTypes, Log
from datetime import datetime

logger: Logger = Logger()

logger.log(Log(LogTypes.ERROR, 'jkj fdasjfj fjla jlaf', datetime.now()))