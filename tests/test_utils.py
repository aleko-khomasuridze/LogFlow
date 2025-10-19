from logFlow.handlers import ConsoleHandler
from logFlow.logger import Logger


def test_logger_clear_handlers_removes_all() -> None:
    logger = Logger()
    assert any(isinstance(handler, ConsoleHandler) for handler in logger.get_handlers())

    logger.clear_handlers()

    assert list(logger.get_handlers()) == []