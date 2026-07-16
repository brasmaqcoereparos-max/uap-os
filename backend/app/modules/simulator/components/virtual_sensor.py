from random import random


class VirtualSensor:

    def __init__(
        self,
        sensor_id,
        name,
        sensor_type,
    ):
        self.id = sensor_id
        self.name = name
        self.type = sensor_type
        self.value = 0

    def read(self):
        return self.value

    def update(self):
        pass

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "value": self.value,
        }
