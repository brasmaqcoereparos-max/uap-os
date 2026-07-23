from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class MQTTDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.broker = None

    def connect(
        self,
        broker,
    ):
        self.connected = True
        self.broker = broker

    def disconnect(self):
        self.connected = False
        self.broker = None

    def publish(
        self,
        topic,
        payload,
    ):
        if not self.connected:
            return False

        return True

    def update(self):
        pass

    def reset(self):
        self.disconnect()
