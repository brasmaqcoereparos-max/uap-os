from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from datetime import timezone
from typing import Any


def utc_now():
    return datetime.now(
        timezone.utc
    )


def parse_datetime(
    value,
):
    if value is None:
        return None

    if isinstance(
        value,
        datetime,
    ):
        return value

    return datetime.fromisoformat(
        str(
            value
        )
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
        timestamp: (
            datetime | None
        ) = None,
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
                timestamp
                or utc_now()
            ).isoformat(),
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
        start: (
            datetime | str | None
        ) = None,
        end: (
            datetime | str | None
        ) = None,
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

        start_dt = parse_datetime(
            start
        )

        end_dt = parse_datetime(
            end
        )

        if start_dt is not None:
            result = [
                item
                for item in result
                if parse_datetime(
                    item[
                        "timestamp"
                    ]
                )
                >= start_dt
            ]

        if end_dt is not None:
            result = [
                item
                for item in result
                if parse_datetime(
                    item[
                        "timestamp"
                    ]
                )
                <= end_dt
            ]

        if limit is not None:
            result = result[
                -max(
                    0,
                    int(limit),
                ):
            ]

        return result

    def export_all(self):

        return {
            category: list(
                items
            )
            for (
                category,
                items,
            ) in self._history.items()
        }

    def import_all(
        self,
        data,
        *,
        replace=True,
    ):
        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "History import "
                "must be a dict"
            )

        if replace:
            self.clear()

        for (
            category,
            items,
        ) in data.items():

            if not isinstance(
                items,
                list,
            ):
                continue

            for item in items:

                if not isinstance(
                    item,
                    dict,
                ):
                    continue

                self.record(
                    category,
                    dict(
                        item.get(
                            "data",
                            {},
                        )
                    ),
                    source=item.get(
                        "source"
                    ),
                    timestamp=parse_datetime(
                        item.get(
                            "timestamp"
                        )
                    ),
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
