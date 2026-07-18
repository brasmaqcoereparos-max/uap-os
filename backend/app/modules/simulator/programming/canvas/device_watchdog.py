from datetime import datetime, timedelta


class DeviceWatchdog:

    def __init__(self):

        self.devices = {}

        self.timeout = timedelta(seconds=10)

    def feed(self, device):

        self.devices[device] = datetime.now()

    def expired(self, device):

        if device not in self.devices:

            return True

        return (

            datetime.now()

            - self.devices[device]

        ) > self.timeout

    def remove(self, device):

        self.devices.pop(

            device,

            None,

        )

    def clear(self):

        self.devices.clear()

    def all(self):

        return {

            device: {

                "last_feed": value.isoformat(),

                "expired": self.expired(device),

            }

            for device, value

            in self.devices.items()

        }


device_watchdog = DeviceWatchdog()
