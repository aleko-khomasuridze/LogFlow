import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from logFlow.logger import Logger
from logFlow.models.log import Log
from logFlow.models.enums.logtype import LogTypes

logger = Logger()
logger.log(Log(LogTypes.ERROR, 'asafas'))
