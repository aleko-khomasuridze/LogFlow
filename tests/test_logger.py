from logflow.handlers import Handler
from logflow.logger import Logger
from logflow.models import Log, LogTypes


class DummyHandler(Handler):
    def __init__(self) -> None:
        self.records: list[Log] = []

    def handle(self, log: Log) -> None:
        self.records.append(log)


def test_logger_dispatches_to_handlers() -> None:
    handler = DummyHandler()
    logger = Logger(handlers=[handler])
    log = Log(LogTypes.ERROR, "dispatched")

    logger.log(log)

    assert handler.records == [log]


def test_logger_log_message_creates_log_objects() -> None:
    handler = DummyHandler()
    logger = Logger(handlers=[handler])

    log = logger.log_message(LogTypes.INFO, "message")

    assert handler.records[0] is log
    assert log.get_message() == "message"
