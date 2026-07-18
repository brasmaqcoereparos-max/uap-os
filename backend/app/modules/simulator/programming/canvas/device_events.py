from datetime import datetime


class DeviceEvents:

    def __init__(self):

        self.events = []

    def emit(
        self,
        device,
        event,
        payload=None,
    ):

        self.events.append(
            {
                "time": datetime.now().isoformat(),
                "device": device,
                "event": event,
                "payload": payload,
            }
        )

    def all(self):

        return self.events.copy()

    def clear(self):

        self.events.clear()


device_events = DeviceEvents()
