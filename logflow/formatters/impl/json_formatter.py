from __future__ import annotations

import json
from typing import Any, Dict, Optional

from ..enums import DateTimeFormat
from ..formatter import Formatter
from ...models import Log
from ...config import LogConfig


class JsonFormatter(Formatter):
    def __init__(
        self,
        date_time_format: DateTimeFormat = LogConfig.LOG_DATE_TIME_FORMAT,
        indent: Optional[int] = None
    ):
        self._date_time_format = date_time_format
        self._indent = indent

    def format(self, log: Log) -> str:
        payload: Dict[str, Any] = {
            "level": log.get_level().value if hasattr(log.get_level(), "value") else str(log.get_level()),
            "message": log.get_message(),
            "date_time": log.get_date_time().strftime(self._date_time_format.value),
        }

        return json.dumps(payload, indent=self._indent)

