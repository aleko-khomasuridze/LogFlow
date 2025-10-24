from logflow import *


class CustomFormatter(Formatter):
    def __init__(self):
        pass
    
    def format(self, log: Log) -> str:
        timestamp = log.get_date_time().strftime(LogConfig.LOG_DATE_TIME_FORMAT)
        return f"{log.get_color()}<{log.get_level().name}> {timestamp} :: {LogColors.RESET}{log.get_message()}"
    
class CustomHandler(Handler):
    def __init__(self, formatter: Formatter = None):
        self.__formatter = formatter
    
    def handle(self, log: Log) -> None:
        ''' You can implement any custom handling logic here. 
            For demonstration, we'll just print the formatted log.
        '''
        print(f"CustomHandler Output: {self.__formatter.format(log)}")


LogConfig.FILE_LOGGING_ENABLED = False
LogConfig.CONSOLE_LOGGING_ENABLED = False

logger: Logger = Logger()
logger.add_handler(CustomHandler(CustomFormatter()))

def main() -> None:
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    
if __name__ == "__main__":
    main()