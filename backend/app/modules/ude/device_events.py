class DeviceEvent:

    def __init__(
        self,
        device_id,
        event_type,
        data=None,
    ):

        self.device_id = device_id
        self.event_type = event_type
        self.data = data or {}


class DeviceEventManager:

    def __init__(self):

        self.listeners = {}

    def subscribe(
        self,
        event_type,
        callback,
    ):

        self.listeners.setdefault(
            event_type,
            [],
        ).append(callback)

    def emit(
        self,
        event,
    ):

        for callback in self.listeners.get(
            event.event_type,
            [],
        ):

            callback(event)


device_events = DeviceEventManager()"""
Universal Device Engine
"""
