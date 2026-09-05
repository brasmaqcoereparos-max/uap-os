from collections import deque

from app.modules.communication.dead_letter import (
    CommunicationDeadLetter,
)


class CommunicationDeadLetterQueue:

    def __init__(
        self,
        max_size: int = 1000,
    ):
        self._queue = deque(
            maxlen=max_size
        )

    def push(
        self,
        letter: CommunicationDeadLetter,
    ):
        self._queue.append(
            letter
        )

        return letter

    def pop(self):
        if not self._queue:
            return None

        return self._queue.popleft()

    def list_all(self):
        return [
            item.to_dict()
            for item
            in self._queue
        ]

    def size(self):
        return len(
            self._queue
        )

    def clear(self):
        self._queue.clear()


communication_dead_letter_queue = (
    CommunicationDeadLetterQueue()
)
