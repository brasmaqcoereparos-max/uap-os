from collections.abc import Callable

from app.modules.ui.event import (
    UIEvent,
)


class UIEventBus:

    def __init__(self):
        self._listeners: dict[
            str,
            list[Callable],
        ] = {}

    def subscribe(
        self,
        event_name: str,
        callback: Callable,
    ):
        listeners = (
            self._listeners.setdefault(
                event_name,
                [],
            )
        )

        if callback not in listeners:
            listeners.append(callback)

        return callback

    def unsubscribe(
        self,
        event_name: str,
        callback: Callable,
    ):
        listeners = self._listeners.get(
            event_name,
            [],
        )

        if callback not in listeners:
            return False

        listeners.remove(callback)

        return True

    def publish(
        self,
        event: UIEvent,
    ):
        results = []

        listeners = self._listeners.get(
            event.name,
            [],
        )

        for callback in list(listeners):
            results.append(
                callback(event)
            )

        return results

    def clear(self):
        self._listeners.clear()


ui_event_bus = UIEventBus()
