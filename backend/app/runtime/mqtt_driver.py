from app.runtime.driver_base import DriverBase


class MQTTDriver(DriverBase):

    def __init__(
        self,
        driver_id: str,
        name: str,
        broker: str,
        port: int = 1883,
        topic: str = "",
    ):
        super().__init__(driver_id, name)

        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = None

    def connect(self):
        try:
            import paho.mqtt.client as mqtt

            self.client = mqtt.Client()
            self.client.connect(
                self.broker,
                self.port,
                60,
            )

            self.client.loop_start()

            self.connected = True

        except Exception:
            self.connected = False

    def disconnect(self):
        if self.client:
            self.client.loop_stop()
            self.client.disconnect()

        self.connected = False

    def update(self):
        if not self.connected:
            return

    def publish(
        self,
        topic: str,
        payload: str,
    ):
        if self.connected:
            self.client.publish(topic, payload)

    def subscribe(
        self,
        topic: str,
    ):
        if self.connected:
            self.client.subscribe(topic)
