# Usage & Example Code

A quick demo of `logflow`.

## Simple Example

### Basic setup

Bare minimum code for setting up and running Logflow

#### Code

```python
from logflow import *

logger: Logger = Logger()

def main() -> None:
    logger.log(Log(LogType.DEBUG), 'some test message')

if __name__ == '__main__':
    main()
```

#### Output

```bash
[Debug]-[2025-10-24T10:22:43]: some test message
```