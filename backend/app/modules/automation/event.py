import time
import uuid


class AutomationEvent:
    def __init__(
        self,
        name,
        data=None,
        source=None,
        event_id=None,
        timestamp=None,
    ):
        self.event_id = (
            str(event_id)
            if event_id is not None
            else str(uuid.uuid4())
        )

        self.name = str(name)

        self.data = dict(
            data or {}
        )

        self.source = source

        self.timestamp = (
            float(timestamp)
            if timestamp is not None
            else time.time()
        )

    def to_dict(self):
        return {
            "id": self.event_id,
            "name": self.name,
            "data": dict(self.data),
            "source": self.source,
            "timestamp": self.timestamp,
        }


class AutomationEventBus:
    def __init__(self):
        self.listeners = {}
        self.history = []

    def subscribe(
        self,
        event_name,
        callback,
    ):
        if not callable(callback):
            raise TypeError(
                "Callback precisa "
                "ser executável."
            )

        event_name = str(
            event_name
        )

        listeners = (
            self.listeners.setdefault(
                event_name,
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
        event_name,
        callback,
    ):
        listeners = (
            self.listeners.get(
                str(event_name),
                [],
            )
        )

        try:
            listeners.remove(
                callback
            )
            return True

        except ValueError:
            return False

    def emit(
        self,
        event,
    ):
        if isinstance(event, str):
            event = AutomationEvent(
                event
            )

        if not isinstance(
            event,
            AutomationEvent,
        ):
            raise TypeError(
                "Evento inválido."
            )

        self.history.append(
            event
        )

        callbacks = list(
            self.listeners.get(
                event.name,
                [],
            )
        )

        callbacks.extend(
            self.listeners.get(
                "*",
                [],
            )
        )

        results = []

        for callback in callbacks:
            results.append(
                callback(event)
            )

        return results

    def clear(
        self,
        event_name=None,
    ):
        if event_name is None:
            self.listeners.clear()
            return

        self.listeners.pop(
            str(event_name),
            None,
        )

    def clear_history(self):
        self.history.clear()

    def listener_count(
        self,
        event_name=None,
    ):
        if event_name is not None:
            return len(
                self.listeners.get(
                    str(event_name),
                    [],
                )
            )

        return sum(
            len(items)
            for items
            in self.listeners.values()
        )


event_bus = AutomationEventBus()
