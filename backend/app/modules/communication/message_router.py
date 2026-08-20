from __future__ import annotations

from collections import defaultdict
from typing import Callable

from .message import UAPMessage


class MessageRouter:
    def __init__(self) -> None:
        self._handlers: dict[
            str,
            list[Callable[[UAPMessage], None]],
        ] = defaultdict(list)

    def register(
        self,
        message_type: str,
        handler: Callable[[UAPMessage], None],
    ) -> None:
        self._handlers[message_type].append(handler)

    def unregister(
        self,
        message_type: str,
        handler: Callable[[UAPMessage], None],
    ) -> bool:
        handlers = self._handlers.get(message_type)

        if not handlers or handler not in handlers:
            return False

        handlers.remove(handler)
        return True

    def route(
        self,
        message: UAPMessage,
    ) -> int:
        handlers = list(
            self._handlers.get(
                message.message_type,
                [],
            )
        )

        for handler in handlers:
            handler(message)

        return len(handlers)

    def clear(self) -> None:
        self._handlers.clear()
