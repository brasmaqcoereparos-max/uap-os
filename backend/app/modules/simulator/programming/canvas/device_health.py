from datetime import datetime


class DeviceHealth:

    def __init__(self):

        self.health = {}

    def heartbeat(self, device):

        self.health[device] = {

            "last_seen": datetime.now(),

            "online": True,

        }

    def offline(self, device):

        self.health[device] = {

            "last_seen": datetime.now(),

            "online": False,

        }

    def get(self, device):

        return self.health.get(device)

    def all(self):

        return {

            name: {

                "last_seen": value["last_seen"].isoformat(),

                "online": value["online"],

            }

            for name, value in self.health.items()

        }


device_health = DeviceHealth()
