"""
Dispositivo LoRa simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class LoRaDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Comunicação LoRa simulada",
            icon="radio",
        )

        self.connected = False
        self.frequency = 0

        self.messages = []
        self.received_messages = []

        self.bandwidth = 125000
        self.spreading_factor = 7

        self.sent_count = 0
        self.received_count = 0

    def connect(self, frequency):
        if not self.enabled:
            return False

        frequency = float(frequency)

        if frequency <= 0:
            raise ValueError(
                "A frequência LoRa deve ser maior que zero."
            )

        self.frequency = frequency
        self.connected = True
        return True

    def disconnect(self):
        self.connected = False
        return True

    def configure(
        self,
        bandwidth=None,
        spreading_factor=None,
    ):
        if bandwidth is not None:
            bandwidth = int(bandwidth)

            if bandwidth <= 0:
                raise ValueError(
                    "Bandwidth deve ser maior que zero."
                )

            self.bandwidth = bandwidth

        if spreading_factor is not None:
            spreading_factor = int(
                spreading_factor
            )

            if not 5 <= spreading_factor <= 12:
                raise ValueError(
                    "Spreading factor deve estar entre 5 e 12."
                )

            self.spreading_factor = spreading_factor

        return True

    def send(self, message):
        if not self.enabled or not self.connected:
            return False

        self.messages.append(message)
        self.sent_count += 1
        return True

    def receive(self):
        if self.received_messages:
            message = self.received_messages.pop(0)
        elif self.messages:
            message = self.messages.pop(0)
        else:
            return None

        self.received_count += 1
        return message

    def inject_received(self, message):
        self.received_messages.append(message)
        return True

    def update(self):
        return {
            "connected": self.connected,
            "frequency": self.frequency,
            "bandwidth": self.bandwidth,
            "spreading_factor": self.spreading_factor,
        }

    def reset(self):
        self.messages.clear()
        self.received_messages.clear()

        self.frequency = 0
        self.sent_count = 0
        self.received_count = 0

        self.disconnect()
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "connected": self.connected,
            "frequency": self.frequency,
            "bandwidth": self.bandwidth,
            "spreading_factor": self.spreading_factor,
            "sent_count": self.sent_count,
            "received_count": self.received_count,
        })
        return data
