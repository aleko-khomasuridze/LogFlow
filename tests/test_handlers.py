from io import StringIO

from logflow.handlers import ConsoleHandler, CustomHandler, FileHandler
from logflow.models import Log, LogTypes


def test_console_handler_writes_to_stream() -> None:
    buffer = StringIO()
    handler = ConsoleHandler(stream=buffer)
    log = Log(LogTypes.WARNING, "console handler")

    handler.handle(log)

    assert buffer.getvalue().rstrip()  # non empty


def test_custom_handler_invokes_callback() -> None:
    received = {}

    def _callback(message: str, log: Log) -> None:
        received["message"] = message
        received["log"] = log

    handler = CustomHandler(_callback)
    log = Log(LogTypes.INFO, "custom handler")

    handler.handle(log)

    assert received["log"] is log
    assert "custom handler" in received["message"]


def test_file_handler_appends_logs(tmp_path) -> None:
    file_path = tmp_path / "log.txt"
    handler = FileHandler(file_path)
    log = Log(LogTypes.ERROR, "file handler")

    handler.handle(log)

    assert "file handler" in file_path.read_text()