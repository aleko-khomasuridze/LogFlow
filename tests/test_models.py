from datetime import datetime

from logFlow.models import Log, LogColors, LogLevel, LogTypes


def test_log_exposes_expected_properties() -> None:
    moment = datetime(2024, 1, 1, 12, 0, 0)
    log = Log(LogTypes.SUCCESS, "payload", moment)

    assert log.get_level() is LogLevel.SUCCESS
    assert log.get_color() is LogColors.SUCCESS
    assert log.get_message() == "payload"
    assert log.get_date_time() is moment


def test_log_to_dict_is_serialisable() -> None:
    log = Log(LogTypes.WARNING, "dict payload", datetime(2024, 2, 3, 4, 5, 6))

    data = log.to_dict()

    assert data["level"] == "Warning"
    assert data["message"] == "dict payload"
    assert data["date_time"].startswith("2024-02-03T04:05:06")