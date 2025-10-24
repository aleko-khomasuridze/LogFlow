# from logflow.logger import Logger
# from logflow.models import LogTypes, Log
# from logflow.config import LogConfig
from logflow import Logger, LogConfig, LogTypes, Log

LogConfig.LOG_DATE_TIME_FORMAT

def main() -> None:
    logger = Logger()
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
if __name__ == "__main__":
    main()