# Logflow - Python

[<img src="https://img.shields.io/badge/Version-1.0.0-blue">](#)
[<img src="https://img.shields.io/badge/Status-Stable-brightgreen">](#)
[<img src="https://img.shields.io/badge/Python-3.11-brightgreen">](#)

A simple yet elegant logging library for your `python` apps.

## Specs

### Logging

* **`console`** – colorful and elegant log format for the terminal.
* **`file`** – stashing and persistence of logs on your system with organization by date.
* **`database`** – custom logging that allows you to save your logs in a database for remote access and optimized search.

### Configuration

* **`datetime mask`** – you have a variety of standard datetime/timestamp masks to choose from.
* **`custom handlers`** – you can implement and add your own custom handlers to the logger’s handler list using our `Handler` interface/abstract class.
* **`logging file path config`** – configurable logging file path in `LogConfig`.

## Setup

Setting up Logflow on your device.

### Installation

```bash
pip install logflow-python
```

> Works on any system — no specific download required!

### Check (optional)

```bash
pip list
```

After running the following command, check for `logflow` in the list. If not found, install again.

## Simple Example

A quick demo of `logflow`.

### Basic setup

##### Code

```python
from logflow import *

logger: Logger = Logger()

def main() -> None:
    logger.log(Log(LogType.DEBUG), 'some test message')

if __name__ == '__main__':
    main()
```

##### Output

```bash
[Debug]-[YYYY-MM-DDTHH:mm:SS]: some test message
```
Sure — here’s the same section rewritten cleanly and professionally, without emojis:

---

## Logger Configuration

### DateTime Format Configuration

With **LogFlow**, you can fully customize the **date and time format** of your log messages.
You can choose from the built-in standard formats (`ISO`, `US`, `EU`, `SIMPLE`, `FULL`, `SHORT_TIME`)
or define a custom format to match your preferred logging style.
This flexibility allows consistent timestamp formatting across regions, systems, and user interfaces.

---

#### Example Code

```python
from logflow import *

logger: Logger = Logger()

def main() -> None:
    # Default: ISO format -> "%Y-%m-%dT%H:%M:%S"
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
```

---

#### Example Output

```bash
[Debug]-[2025-10-24T10:22:43]: LogFlow is running smoothly!
[Debug]-[10/24/2025 10:22 AM]: LogFlow is running smoothly!
[Debug]-[24/10/2025 10:22]: LogFlow is running smoothly!
[Debug]-[2025-10-24]: LogFlow is running smoothly!
[Debug]-[Friday, October 24, 2025 10:22:43]: LogFlow is running smoothly!
[Debug]-[10:22]: LogFlow is running smoothly!
[Debug]-[24-10-2025 10:22:43]: LogFlow is running smoothly!
```

---

### Summary

| Format Type    | Mask Example             | Description                                         |
| -------------- | ------------------------ | --------------------------------------------------- |
| **ISO**        | `%Y-%m-%dT%H:%M:%S`      | Standard ISO 8601 timestamp (default)               |
| **US**         | `%m/%d/%Y %I:%M %p`      | U.S. date format with AM/PM                         |
| **EU**         | `%d/%m/%Y %H:%M`         | European date format                                |
| **SIMPLE**     | `%Y-%m-%d`               | Date-only representation                            |
| **FULL**       | `%A, %B %d, %Y %H:%M:%S` | Full date and time                                  |
| **SHORT_TIME** | `%H:%M`                  | Time-only (hours and minutes)                       |
| **CUSTOM**     | *User-defined*           | Fully customizable using Python’s `strftime` syntax |

---

> **Tip**:
You can dynamically change `LogConfig.LOG_DATE_TIME_FORMAT` at runtime.
This makes it easy to adjust log output for localization, system integration, or debugging needs.


### Custom handler implementation and integration

### 

