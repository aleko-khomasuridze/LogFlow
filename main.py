from logflow import *

logger: Logger = Logger()

def main() -> None:
    # Set custom DateTimeFormat and log a message
    # ISO (default) -> "%Y-%m-%dT%H:%M:%S"
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    # US -> "%m/%d/%Y %I:%M %p"
    LogConfig.LOG_DATE_TIME_FORMAT = DateTimeFormat.US    
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    # EU -> "%d/%m/%Y %H:%M"
    LogConfig.LOG_DATE_TIME_FORMAT = DateTimeFormat.EU    
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    # SIMPLE -> "%Y-%m-%d"
    LogConfig.LOG_DATE_TIME_FORMAT = DateTimeFormat.SIMPLE    
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    # FULL -> "%A, %B %d, %Y %H:%M:%S"
    LogConfig.LOG_DATE_TIME_FORMAT = DateTimeFormat.FULL    
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    # SHORT_TIME -> "%H:%M"
    LogConfig.LOG_DATE_TIME_FORMAT = DateTimeFormat.SHORT_TIME    
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    # CUSTOM -> User-defined format
    DateTimeFormat.CUSTOM = "%d-%m-%Y %H:%M:%S"  # Example of setting a custom format   
    LogConfig.LOG_DATE_TIME_FORMAT = DateTimeFormat.CUSTOM
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    
if __name__ == "__main__":
    main()