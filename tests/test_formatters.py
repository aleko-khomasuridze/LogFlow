from datetime import datetime
import json

from src.formaters import DateTimeFormat, JsonFormatter, LogFormatter, logFormater
from src.models import Log, LogColors, LogTypes


def test_log_formatter_is_singleton() -> None:
    instance_one = LogFormatter(DateTimeFormat.ISO)
    instance_two = LogFormatter()

    assert instance_one is instance_two


def test_log_formatter_uses_color_level_and_reset() -> None:
    formatter = LogFormatter()
    formatter.set_date_time_format(DateTimeFormat.US)
    log = Log(LogTypes.INFO, "formatted message", datetime(2024, 5, 6, 9, 30))

    formatted = formatter.format(log)

    assert formatted.startswith(f"{LogColors.INFO.value}[Info]-[")
    assert "]" + LogColors.RESET.value + ": formatted message" in formatted
    assert "05/06/2024" in formatted


def test_log_formatter_module_instance_respects_configuration() -> None:
    log = Log(LogTypes.ERROR, "module instance")
    formatted = logFormater.format(log)

    assert formatted.endswith(f"{LogColors.RESET.value}: module instance")


def test_json_formatter_serialises_expected_fields() -> None:
    log = Log(LogTypes.SUCCESS, "json message", datetime(2023, 1, 2, 3, 4, 5))
    formatter = JsonFormatter(date_time_format=DateTimeFormat.SIMPLE, indent=0)

    payload = json.loads(formatter.format(log))

    assert payload == {
        "level": "Success",
        "message": "json message",
        "date_time": "2023-01-02",
    }