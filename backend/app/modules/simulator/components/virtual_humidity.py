"""
Sensor virtual de umidade.
"""

import random

from app.modules.simulator.components.virtual_sensor import (
    VirtualSensor,
)


class VirtualHumidity(
    VirtualSensor
):

    def __init__(
        self,
        sensor_id,
        name,
        minimum=20,
        maximum=90,
        unit="%",
    ):
        super().__init__(
            sensor_id=sensor_id,
            name=name,
            sensor_type="HUMIDITY",
            value=0,
            unit=unit,
        )

        self.minimum = int(
            minimum
        )

        self.maximum = int(
            maximum
        )

        if (
            self.minimum
            > self.maximum
        ):
            raise ValueError(
                "minimum não pode ser "
                "maior que maximum."
            )

    def update(self):
        if not self.enabled:
            return self.value

        value = random.randint(
            self.minimum,
            self.maximum,
        )

        self.update_count += 1

        return self.set_value(
            value
        )

    def set_range(
        self,
        minimum,
        maximum,
    ):
        minimum = int(
            minimum
        )

        maximum = int(
            maximum
        )

        if minimum > maximum:
            raise ValueError(
                "Faixa inválida."
            )

        self.minimum = minimum
        self.maximum = maximum

        return True

    def in_range(
        self,
        value=None,
    ):
        if value is None:
            value = self.value

        return (
            self.minimum
            <= int(value)
            <= self.maximum
        )

    def status(self):
        data = super().status()

        data[
            "minimum"
        ] = self.minimum

        data[
            "maximum"
        ] = self.maximum

        return data
