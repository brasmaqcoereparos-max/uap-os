"""
Dispositivo MQTT simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class MQTTDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(name)

        self.connected = False
        self.broker = None
        self.port = 1883
        self.subscriptions = set()
        self.messages = []

    def connect(self, broker, port=1883):
        self.broker = broker
        self.port = port
        self.connected = True

    def disconnect(self):
        self.connected = False

    def subscribe(self, topic):
        self.subscriptions.add(topic)

    def unsubscribe(self, topic):
        self.subscriptions.discard(topic)

    def publish(self, topic, message):

        if not self.connected:
            return False

        self.messages.append({
            "topic": topic,
            "message": message,
        })

        return True

    def receive(self):

        if not self.messages:
            return None

        return self.messages.pop(0)

    def update(self):
        pass

    def reset(self):

        self.messages.clear()
        self.subscriptions.clear()
        self.broker = None
        self.disconnect()
