from __future__ import annotations

import sys
from typing import Callable, Protocol, TextIO, Union

from ..handler import Handler
from ...formatters import logFormater
from ...models import Log


class _FormatterProtocol(Protocol):
    def format(self, log: Log) -> str: ...


FormatterType = Union[_FormatterProtocol, Callable[[Log], str]]


class ConsoleHandler(Handler):
    """Handler that prints logs to a text stream (stdout by default)."""

    def __init__(self, *, formatter: FormatterType | None = None, stream: TextIO | None = None) -> None:
        self._formatter: FormatterType = formatter or logFormater
        self._stream: TextIO = stream or sys.stdout

    def handle(self, log: Log) -> None:
        if hasattr(self._formatter, "format"):
            message = self._formatter.format(log)  # type: ignore[attr-defined]
        else:
            message = self._formatter(log)  # type: ignore[operator]

        print(message, file=self._stream, flush=True)