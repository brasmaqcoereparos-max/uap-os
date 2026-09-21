from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from datetime import timezone
from typing import Any


def utc_now():
    return datetime.now(
        timezone.utc
    )


class MetricsHistoryService:

    def __init__(self):

        self._history: dict[
            str,
            list[dict[str, Any]],
        ] = defaultdict(
            list
        )

    def record(
        self,
        category: str,
        data: dict[str, Any],
        *,
        source: str | None = None,
    ):

        normalized = str(
            category
        ).strip()

        if not normalized:
            raise ValueError(
                "History category "
                "is required"
            )

        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "History data "
                "must be a dict"
            )

        item = {
            "category": normalized,
            "source": source,
            "timestamp": (
                utc_now().isoformat()
            ),
            "data": dict(
                data
            ),
        }

        self._history[
            normalized
        ].append(
            item
        )

        return item

    def list(
        self,
        category: str,
        *,
        limit: int | None = None,
        source: str | None = None,
    ):

        result = list(
            self._history.get(
                category,
                [],
            )
        )

        if source is not None:
            result = [
                item
                for item in result
                if item.get(
                    "source"
                )
                == source
            ]

        if limit is not None:
            result = result[
                -max(
                    0,
                    int(limit),
                ):
            ]

        return result

    def latest(
        self,
        category: str,
        *,
        source: str | None = None,
    ):

        items = self.list(
            category,
            source=source,
        )

        if not items:
            return None

        return items[-1]

    def categories(self):

        return sorted(
            self._history.keys()
        )

    def count(
        self,
        category: str,
    ):

        return len(
            self._history.get(
                category,
                [],
            )
        )

    def clear(
        self,
        category: str | None = None,
    ):

        if category is None:
            self._history.clear()

        else:
            self._history.pop(
                category,
                None,
            )


metrics_history_service = (
    MetricsHistoryService()
      )
