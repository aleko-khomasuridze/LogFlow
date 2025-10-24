# Logflow Configuration

Configuration is handled by `LogConfig` class/structure below you can see default implementation of it.

```python
class LogConfig:
    CONSOLE_LOGGING_ENABLED = True
    FILE_LOGGING_ENABLED = True
    LOG_FILE_PATH = _filepath
    LOG_DATE_TIME_FORMAT = DateTimeFormat.ISO 
```

> **Note** Logflow allowes you to manage config in runtime
