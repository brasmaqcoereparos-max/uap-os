from collections import deque


class EventBuffer:

    def __init__(
        self,
        max_size: int = 1000,
    ):
        self.max_size = max(
            1,
            int(max_size),
        )

        self._events = deque(
            maxlen=self.max_size
        )

    def add(self, event):

        self._events.append(event)

        return event

    def latest(self):

        if not self._events:
            return None

        return self._events[-1]

    def list(self):

        return list(self._events)

    def count(self):

        return len(self._events)

    def clear(self):

        self._events.clear()


event_buffer = EventBuffer()
