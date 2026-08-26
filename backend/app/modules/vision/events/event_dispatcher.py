from typing import Callable


class EventDispatcher:

    def __init__(self):
        self._listeners = {}

    def subscribe(
        self,
        event_type: str,
        listener: Callable,
    ):

        self._listeners.setdefault(
            event_type,
            [],
        ).append(listener)

        return listener

    def unsubscribe(
        self,
        event_type: str,
        listener: Callable,
    ):

        listeners = self._listeners.get(
            event_type,
            [],
        )

        if listener in listeners:
            listeners.remove(listener)

        return listener

    def dispatch(self, event):

        event_type = getattr(
            event,
            "event_type",
            None,
        )

        listeners = self._listeners.get(
            event_type,
            [],
        )

        results = []

        for listener in list(
            listeners
        ):
            results.append(
                listener(event)
            )

        return results

    def clear(self):

        self._listeners.clear()


event_dispatcher = EventDispatcher()
