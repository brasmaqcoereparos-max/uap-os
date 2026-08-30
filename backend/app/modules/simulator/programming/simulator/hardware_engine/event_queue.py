"""
Fila de eventos do simulador UAP.
"""

from collections import deque


class EventQueue:

    def __init__(
        self,
        max_size=None,
    ):
        self._queue = deque()

        self.max_size = (
            int(max_size)
            if max_size is not None
            else None
        )

        self.total_pushed = 0
        self.total_popped = 0
        self.total_dropped = 0

    def push(
        self,
        event,
    ):
        if event is None:
            return False

        if (
            self.max_size is not None
            and len(self._queue)
            >= self.max_size
        ):
            self.total_dropped += 1

            return False

        self._queue.append(
            event
        )

        self.total_pushed += 1

        return True

    def push_front(
        self,
        event,
    ):
        if event is None:
            return False

        if (
            self.max_size is not None
            and len(self._queue)
            >= self.max_size
        ):
            self.total_dropped += 1

            return False

        self._queue.appendleft(
            event
        )

        self.total_pushed += 1

        return True

    def pop(self):
        if not self._queue:
            return None

        self.total_popped += 1

        return self._queue.popleft()

    def peek(self):
        if not self._queue:
            return None

        return self._queue[0]

    def clear(self):
        count = len(
            self._queue
        )

        self._queue.clear()

        return count

    def empty(self):
        return (
            len(self._queue)
            == 0
        )

    def size(self):
        return len(
            self._queue
        )

    def full(self):
        if self.max_size is None:
            return False

        return (
            len(self._queue)
            >= self.max_size
        )

    def all(self):
        return list(
            self._queue
        )

    def status(self):
        return {
            "size": self.size(),
            "empty": self.empty(),
            "full": self.full(),
            "max_size": (
                self.max_size
            ),
            "total_pushed": (
                self.total_pushed
            ),
            "total_popped": (
                self.total_popped
            ),
            "total_dropped": (
                self.total_dropped
            ),
        }
