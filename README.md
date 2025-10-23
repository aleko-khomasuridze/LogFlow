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

### Logger Configuration

### Custom handler implementation and integration

### 

