from __future__ import annotations

import json
from typing import Any, Dict, Optional

from .format_enums import DateTimeFormat
from ..models import Log


class JsonFormatter:
    """Serialises logs to JSON strings."""

    def __init__(
        self,
        *,
        date_time_format: DateTimeFormat = DateTimeFormat.ISO,
        indent: Optional[int] = None,
    ) -> None:
        self._date_time_format = date_time_format
        self._indent = indent

    def format(self, log: Log) -> str:
        payload: Dict[str, Any] = {
            "level": log.get_level().value if hasattr(log.get_level(), "value") else str(log.get_level()),
            "message": log.get_message(),
            "date_time": log.get_date_time().strftime(self._date_time_format.value),
        }

        return json.dumps(payload, indent=self._indent)


__all__ = ["JsonFormatter"]