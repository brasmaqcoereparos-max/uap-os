"""
Fila de eventos do simulador UAP.
"""

from collections import deque


class EventQueue:

    def __init__(self):

        self._queue = deque()

    def push(
        self,
        event,
    ):

        if event is not None:
            self._queue.append(event)

    def pop(self):

        if not self._queue:
            return None

        return self._queue.popleft()

    def peek(self):

        if not self._queue:
            return None

        return self._queue[0]

    def clear(self):

        self._queue.clear()

    def empty(self):

        return len(self._queue) == 0

    def size(self):

        return len(self._queue)
