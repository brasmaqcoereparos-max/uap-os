from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable


@dataclass
class HardwareEvent:
    event_type: str
    device_id: str | None = None
    source: str | None = None
    value: Any = None
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    metadata: dict[str, Any] = field(default_factory=dict)


class HardwareEventBus:
    def __init__(self) -> None:
        self._handlers: dict[
            str,
            list[Callable[[HardwareEvent], Any]],
        ] = {}

    def subscribe(
        self,
        event_type: str,
        handler: Callable[[HardwareEvent], Any],
    ) -> None:
        self._handlers.setdefault(
            event_type,
            [],
        ).append(handler)

    def unsubscribe(
        self,
        event_type: str,
        handler: Callable[[HardwareEvent], Any],
    ) -> bool:
        handlers = self._handlers.get(event_type)

        if not handlers:
            return False

        if handler not in handlers:
            return False

        handlers.remove(handler)
        return True

    def publish(
        self,
        event: HardwareEvent,
    ) -> None:
        handlers = self._handlers.get(
            event.event_type,
            [],
        )

        for handler in list(handlers):
            handler(event)

    def clear(self) -> None:
        self._handlers.clear()
