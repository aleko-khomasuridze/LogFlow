from __future__ import annotations

from pathlib import Path
from typing import Callable, Optional, Protocol, Union

from ..handler import Handler
from ...formatters import logFormater
from ...models import Log


class _FormatterProtocol(Protocol):
    def format(self, log: Log) -> str: ...


FormatterType = Union[_FormatterProtocol, Callable[[Log], str]]


class FileHandler(Handler):
    """Persists logs to a file on disk."""

    def __init__(
        self,
        path: str | Path,
        *,
        formatter: FormatterType | None = None,
        mode: str = "a",
        encoding: Optional[str] = "utf-8",
    ) -> None:
        self._path = Path(path)
        self._formatter: FormatterType = formatter or logFormater
        self._mode = mode
        self._encoding = encoding

    def handle(self, log: Log) -> None:
        if hasattr(self._formatter, "format"):
            message = self._formatter.format(log)  # type: ignore[attr-defined]
        else:
            message = self._formatter(log)  # type: ignore[operator]

        self._path.parent.mkdir(parents=True, exist_ok=True)
        with self._path.open(self._mode, encoding=self._encoding) as file:
            file.write(f"{message}\n")


__all__ = ["FileHandler"]
