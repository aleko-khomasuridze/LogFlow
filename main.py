from logflow import *



logger: Logger = Logger()



def main() -> None:
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    
if __name__ == "__main__":
    main()