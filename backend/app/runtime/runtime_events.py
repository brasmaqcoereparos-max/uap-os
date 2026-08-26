from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable


@dataclass
class RuntimeEvent:

    event_type: str
    source: str
    data: Any = None

    timestamp: str = ""

    def __post_init__(self):

        if not self.timestamp:
            self.timestamp = (
                datetime.now(
                    timezone.utc
                ).isoformat()
            )

    def to_dict(self):

        return {
            "event_type": self.event_type,
            "source": self.source,
            "data": self.data,
            "timestamp": self.timestamp,
        }


class RuntimeEventBus:

    def __init__(self):

        self._listeners = {}

    def subscribe(
        self,
        event_type: str,
        callback: Callable,
    ):

        self._listeners.setdefault(
            event_type,
            [],
        ).append(callback)

        return callback

    def unsubscribe(
        self,
        event_type: str,
        callback: Callable,
    ):

        listeners = self._listeners.get(
            event_type,
            [],
        )

        if callback in listeners:
            listeners.remove(callback)

        if not listeners:
            self._listeners.pop(
                event_type,
                None,
            )

    def emit(
        self,
        event_type: str,
        source: str,
        data: Any = None,
    ):

        event = RuntimeEvent(
            event_type=event_type,
            source=source,
            data=data,
        )

        listeners = list(
            self._listeners.get(
                event_type,
                [],
            )
        )

        listeners += list(
            self._listeners.get(
                "*",
                [],
            )
        )

        results = []

        for callback in listeners:

            try:

                results.append(
                    callback(event)
                )

            except Exception as exc:

                results.append(
                    {
                        "success": False,
                        "error": str(exc),
                    }
                )

        return {
            "event": event.to_dict(),
            "results": results,
        }

    def clear(self):

        self._listeners.clear()


runtime_events = RuntimeEventBus()
