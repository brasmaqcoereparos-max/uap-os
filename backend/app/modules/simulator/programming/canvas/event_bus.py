class EventBus:

    def __init__(self):

        self.listeners = {}

    def subscribe(
        self,
        event,
        callback,
    ):

        self.listeners.setdefault(
            event,
            [],
        ).append(callback)

    def emit(
        self,
        event,
        payload=None,
    ):

        for callback in self.listeners.get(
            event,
            [],
        ):

            callback(payload)

    def clear(self):

        self.listeners.clear()


event_bus = EventBus()
