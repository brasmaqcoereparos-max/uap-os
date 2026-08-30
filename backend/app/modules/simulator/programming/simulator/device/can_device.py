"""
Barramento CAN simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class CANDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Barramento CAN simulado",
            icon="network",
        )

        self.frames = []
        self.tx_frames = []
        self.rx_frames = []

        self.bitrate = 500000
        self.sent_count = 0
        self.received_count = 0

    def configure(self, bitrate=500000):
        bitrate = int(bitrate)

        if bitrate <= 0:
            raise ValueError(
                "O bitrate CAN deve ser maior que zero."
            )

        self.bitrate = bitrate
        return self.bitrate

    def send(self, frame):
        if not self.enabled:
            return False

        self.frames.append(frame)
        self.tx_frames.append(frame)
        self.sent_count += 1

        return True

    def receive(self):
        if self.rx_frames:
            frame = self.rx_frames.pop(0)
            self.received_count += 1
            return frame

        if self.frames:
            frame = self.frames.pop(0)
            self.received_count += 1
            return frame

        return None

    def inject_frame(self, frame):
        self.rx_frames.append(frame)
        return True

    def pending(self):
        return len(self.rx_frames) + len(self.frames)

    def update(self):
        return {
            "bitrate": self.bitrate,
            "pending": self.pending(),
            "sent_count": self.sent_count,
            "received_count": self.received_count,
        }

    def reset(self):
        self.frames.clear()
        self.tx_frames.clear()
        self.rx_frames.clear()
        self.sent_count = 0
        self.received_count = 0
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "bitrate": self.bitrate,
            "pending": self.pending(),
            "sent_count": self.sent_count,
            "received_count": self.received_count,
        })
        return data
