
import time


class DeviceMonitor:

    def __init__(self):

        self.values = {}

    def update(
        self,
        device_id,
        value,
    ):

        self.values[device_id] = {
            "value": value,
            "timestamp": time.time(),
        }

    def get(
        self,
        device_id,
    ):

        return self.values.get(device_id)

    def all(self):

        return dict(self.values)
