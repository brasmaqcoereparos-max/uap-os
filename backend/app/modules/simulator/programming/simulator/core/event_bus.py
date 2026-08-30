"""
Barramento central de eventos do Core UAP.

Mantém:
    listeners
    subscribe()
    emit()
    event_bus
"""


class EventBus:

    def __init__(self):
        self.listeners = {}

        self.emit_count = 0
        self.callback_count = 0

        self.last_event = None
        self.last_error = None

    def subscribe(
        self,
        event,
        callback,
    ):
        if not callable(callback):
            raise TypeError(
                "O callback do evento "
                "precisa ser executável."
            )

        listeners = (
            self.listeners.setdefault(
                event,
                [],
            )
        )

        if callback not in listeners:
            listeners.append(
                callback
            )

        return callback

    def unsubscribe(
        self,
        event,
        callback=None,
    ):
        if event not in self.listeners:
            return False

        if callback is None:
            self.listeners.pop(
                event,
                None,
            )

            return True

        listeners = (
            self.listeners[event]
        )

        if callback not in listeners:
            return False

        listeners.remove(
            callback
        )

        if not listeners:
            self.listeners.pop(
                event,
                None,
            )

        return True

    def emit(
        self,
        event,
        data=None,
    ):
        self.emit_count += 1
        self.last_event = event

        if event not in self.listeners:
            return None

        results = []

        try:
            for callback in list(
                self.listeners[event]
            ):
                results.append(
                    callback(data)
                )

                self.callback_count += 1

            self.last_error = None

            return results

        except Exception as exc:
            self.last_error = str(exc)

            raise

    def has_listeners(
        self,
        event,
    ):
        return bool(
            self.listeners.get(
                event
            )
        )

    def listener_count(
        self,
        event=None,
    ):
        if event is not None:
            return len(
                self.listeners.get(
                    event,
                    [],
                )
            )

        return sum(
            len(callbacks)
            for callbacks
            in self.listeners.values()
        )

    def events(self):
        return list(
            self.listeners.keys()
        )

    def clear(
        self,
        event=None,
    ):
        if event is not None:
            return self.unsubscribe(
                event
            )

        count = (
            self.listener_count()
        )

        self.listeners.clear()

        return count

    def status(self):
        return {
            "events": len(
                self.listeners
            ),
            "listeners": (
                self.listener_count()
            ),
            "emit_count": (
                self.emit_count
            ),
            "callback_count": (
                self.callback_count
            ),
            "last_event": (
                self.last_event
            ),
            "last_error": (
                self.last_error
            ),
        }


event_bus = EventBus()
