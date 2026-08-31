"""
Sistema de eventos da automação UAP.
"""

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

        self.name = str(
            name
        )

        self.data = dict(
            data or {}
        )

        self.source = source

        self.timestamp = (
            float(timestamp)
            if timestamp is not None
            else time.time()
        )

        self.metadata = {}

    def set_metadata(
        self,
        key,
        value,
    ):
        self.metadata[
            str(key)
        ] = value

        return value

    def to_dict(self):
        return {
            "id": self.event_id,
            "name": self.name,
            "data": dict(
                self.data
            ),
            "source": self.source,
            "timestamp": (
                self.timestamp
            ),
            "metadata": dict(
                self.metadata
            ),
        }


class AutomationEventBus:

    def __init__(self):
        self.listeners = {}

        self.history = []

        self.emit_count = 0
        self.callback_count = 0

        self.last_event = None
        self.last_error = None

    def subscribe(
        self,
        event_name,
        callback,
    ):
        if not callable(
            callback
        ):
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

            if not listeners:
                self.listeners.pop(
                    str(event_name),
                    None,
                )

            return True

        except ValueError:
            return False

    def emit(
        self,
        event,
    ):
        if isinstance(
            event,
            str,
        ):
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

        self.last_event = event
        self.last_error = None

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

        try:
            for callback in callbacks:
                results.append(
                    callback(
                        event
                    )
                )

                self.callback_count += 1

            self.emit_count += 1

            return results

        except Exception as exc:
            self.last_error = str(
                exc
            )

            raise

    def clear(
        self,
        event_name=None,
    ):
        if event_name is None:
            count = (
                self.listener_count()
            )

            self.listeners.clear()

            return count

        event_name = str(
            event_name
        )

        count = len(
            self.listeners.get(
                event_name,
                [],
            )
        )

        self.listeners.pop(
            event_name,
            None,
        )

        return count

    def clear_history(self):
        count = len(
            self.history
        )

        self.history.clear()

        return count

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

    def history_count(self):
        return len(
            self.history
        )

    def status(self):
        return {
            "listener_count": (
                self.listener_count()
            ),
            "history_count": (
                self.history_count()
            ),
            "emit_count": (
                self.emit_count
            ),
            "callback_count": (
                self.callback_count
            ),
            "last_event": (
                self.last_event.to_dict()
                if self.last_event
                is not None
                else None
            ),
            "last_error": (
                self.last_error
            ),
        }


event_bus = (
    AutomationEventBus()
        )
