from collections import deque

from app.modules.security.security_event import (
    SecurityEvent,
)


class SecurityEventLog:

    def __init__(
        self,
        max_size: int = 5000,
    ):
        self._events = deque(
            maxlen=max_size
        )

    def add(
        self,
        event: SecurityEvent,
    ):
        self._events.append(
            event
        )

        return event

    def list_all(self):
        return [
            event.to_dict()
            for event
            in self._events
        ]

    def clear(self):
        self._events.clear()

    def size(self):
        return len(
            self._events
        )


security_event_log = (
    SecurityEventLog()
          )
