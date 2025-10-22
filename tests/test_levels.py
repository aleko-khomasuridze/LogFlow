from logflow.models import LogColors, LogLevel, LogTypes


def test_log_levels_are_strings() -> None:
    assert LogLevel.ERROR.value == "Error"
    assert LogLevel.SUCCESS.value == "Success"


def test_log_types_bind_level_and_color() -> None:
    assert LogTypes.ERROR.log_level is LogLevel.ERROR
    assert LogTypes.ERROR.log_color is LogColors.ERROR
    assert LogTypes.SUCCESS.log_level is LogLevel.SUCCESS