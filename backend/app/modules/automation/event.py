class AutomationEvent:

    def __init__(
        self,
        name,
        data=None,
    ):

        self.name = name

        self.data = data or {}


class AutomationEventBus:

    def __init__(self):

        self.listeners = {}

    def subscribe(
        self,
        event_name,
        callback,
    ):

        self.listeners.setdefault(
            event_name,
            [],
        ).append(callback)

    def emit(
        self,
        event,
    ):

        for callback in self.listeners.get(
            event.name,
            [],
        ):

            callback(event)


event_bus = AutomationEventBus()
