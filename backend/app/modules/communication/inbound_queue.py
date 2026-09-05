from collections import deque

from app.modules.communication.inbound_message import (
    CommunicationInboundMessage,
)


class CommunicationInboundQueue:

    def __init__(
        self,
        max_size: int = 1000,
    ):
        self.max_size = max(
            1,
            int(max_size),
        )

        self._queue = deque(
            maxlen=self.max_size
        )

    def push(
        self,
        message: CommunicationInboundMessage,
    ):
        self._queue.append(
            message
        )

        return message

    def pop(self):
        if not self._queue:
            return None

        return self._queue.popleft()

    def peek(self):
        if not self._queue:
            return None

        return self._queue[0]

    def size(self):
        return len(
            self._queue
        )

    def clear(self):
        self._queue.clear()

    def snapshot(self):
        return {
            "size": self.size(),
            "max_size": self.max_size,
        }


communication_inbound_queue = (
    CommunicationInboundQueue()
      )
