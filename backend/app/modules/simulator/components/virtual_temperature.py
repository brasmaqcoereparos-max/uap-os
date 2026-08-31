"""
Sensor virtual de temperatura.
"""

import random

from app.modules.simulator.components.virtual_sensor import (
    VirtualSensor,
)


class VirtualTemperature(
    VirtualSensor
):

    def __init__(
        self,
        sensor_id,
        name,
        minimum=18.0,
        maximum=35.0,
        unit="°C",
    ):
        super().__init__(
            sensor_id=sensor_id,
            name=name,
            sensor_type="TEMPERATURE",
            value=0.0,
            unit=unit,
        )

        self.minimum = float(
            minimum
        )

        self.maximum = float(
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

        value = round(
            random.uniform(
                self.minimum,
                self.maximum,
            ),
            1,
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
        minimum = float(
            minimum
        )

        maximum = float(
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
            <= float(value)
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
