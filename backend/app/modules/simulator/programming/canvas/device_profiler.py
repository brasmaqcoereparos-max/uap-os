from datetime import datetime


class DeviceProfiler:

    def __init__(self):

        self.data = {}

    def begin(self, device):

        self.data[device] = {
            "start": datetime.now(),
            "elapsed": 0.0,
            "calls": self.data.get(device, {}).get("calls", 0),
        }

    def finish(self, device):

        if device not in self.data:
            return

        elapsed = (
            datetime.now()
            - self.data[device]["start"]
        ).total_seconds()

        self.data[device]["elapsed"] = elapsed
        self.data[device]["calls"] += 1

    def get(self, device):

        return self.data.get(device)

    def clear(self):

        self.data.clear()


device_profiler = DeviceProfiler()
