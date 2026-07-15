from app.runtime.driver_base import DriverBase

from app.runtime.mqtt_driver import MQTTDriver


class ESP32Driver(DriverBase):

    def __init__(
        self,
        driver_id: str,
        name: str,
        broker: str,
        topic: str,
    ):
        super().__init__(driver_id, name)

        self.topic = topic

        self.mqtt = MQTTDriver(
            driver_id=driver_id,
            name=name,
            broker=broker,
            topic=topic,
        )

    def connect(self):
        self.mqtt.connect()
        self.connected = self.mqtt.connected

    def disconnect(self):
        self.mqtt.disconnect()
        self.connected = False

    def update(self):
        pass

    def digital_write(
        self,
        pin: int,
        value: int,
    ):
        self.mqtt.publish(
            self.topic,
            f"DW:{pin}:{value}",
        )

    def pwm_write(
        self,
        pin: int,
        value: int,
    ):
        self.mqtt.publish(
            self.topic,
            f"PWM:{pin}:{value}",
        )

    def digital_read(
        self,
        pin: int,
    ):
        self.mqtt.publish(
            self.topic,
            f"DR:{pin}",
        )

    def analog_read(
        self,
        pin: int,
    ):
        self.mqtt.publish(
            self.topic,
            f"AR:{pin}",
        )
