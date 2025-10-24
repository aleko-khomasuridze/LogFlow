# Custom Handler Implementation and Integration

LogFlow allows you to extend its functionality by defining **custom formatters** and **handlers**.
This makes it possible to modify how log messages are formatted, processed, or routed — for example, sending logs to a database, cloud service, or custom file format.

In the example below, a custom formatter and handler are implemented to demonstrate how logs can be formatted and handled outside of the default LogFlow configuration.

---

### Example Code

```python
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
        """You can implement any custom handling logic here. 
        For demonstration, we'll just print the formatted log."""
        print(f"CustomHandler Output: {self.__formatter.format(log)}")


# Disable default file and console logging to use only the custom handler
LogConfig.FILE_LOGGING_ENABLED = False
LogConfig.CONSOLE_LOGGING_ENABLED = False

logger: Logger = Logger()
logger.add_handler(CustomHandler(CustomFormatter()))

def main() -> None:
    logger.log(Log(LogTypes.DEBUG, "LogFlow is running smoothly!"))
    
    
if __name__ == "__main__":
    main()
```

---

### Example Output

```bash
CustomHandler Output: <DEBUG> 2025-10-24T10:22:43 :: LogFlow is running smoothly!
```

---

### Explanation

**1. CustomFormatter**
Defines how the log message should be formatted.

* Uses the currently configured `LogConfig.LOG_DATE_TIME_FORMAT` for timestamps.
* Applies color codes from `LogColors` and includes log level, timestamp, and message.
* Returns a string representation of the formatted log.


**2. CustomHandler**
Defines how the log message should be processed or delivered.

* Accepts a `Formatter` instance for flexible formatting.
* Implements the `handle()` method where the log can be printed, saved, or sent elsewhere.
* In this example, it simply prints the formatted log message.

**3. Integration with Logger**

* Default handlers (file and console) are disabled via `LogConfig`.
* The `CustomHandler` is added to the `Logger` using `logger.add_handler()`.
* All logs emitted through this logger are now handled exclusively by the custom handler.

---

### Summary

| Component                | Purpose                                        | Customization                          |
| ------------------------ | ---------------------------------------------- | -------------------------------------- |
| **CustomFormatter**      | Controls the output format of each log message | Modify color, layout, or timestamp     |
| **CustomHandler**        | Controls where and how logs are processed      | Print, store, send to API, etc.        |
| **Logger.add_handler()** | Registers a new handler to process logs        | Attach one or multiple custom handlers |

---

> **Tip**: 
By implementing your own handlers and formatters, you can integrate LogFlow seamlessly into any environment — from simple terminal applications to complex distributed logging infrastructures.
