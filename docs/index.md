# Logify - Python

[<img src="https://img.shields.io/badge/Version-1.0.0-blue">](#)
[<img src="https://img.shields.io/badge/Status-Stable-brightgreen">](#)
[<img src="https://img.shields.io/badge/Python-3.11-brightgreen">](#)

Simple yet elegant logging library for your `python` apps.

## Specs
### Logging
 - **`console`** - colorfull and elegant log format for terminal
 - **`file`** - stashing and persistance of logs on your system with organisation of logs with date.
 - **`database`** - custom logging that allows you to save your logs in database for remote access and optimised search.
### Configuration
 - **`datetime mask`** - you have veriety of standard datetime/timestamp masks to choose from.
 - **`custom handlers`** - you can implement and add your custom handlers in loggers handler list utilizing our `Handler` interface/abstract class
 - **`logging file path config`** - configurable logging file path in `LogCofig`.

## Setup
Setting up logflow on your device 
### Installation
```bash
pip install logflow-python
```
> works on any system no specific download required!

### Check (optional)
```bash
pip list
```
After running the following command check for `logflow` in the list. if not found install again

## Simple Example

Quick demo of `logflow`

#### code

```python
from logflow import *

logger: Logger = Logger()

def main() -> None:
    logger.log(Log(LogType.DEBUG), 'some test message')

if __name__ == '__main__':
    main()

```

#### output

```bash
[Debug]-[YYYY-MM-DDTHH:mm:SS]: some test message
```