"""
Sensor ultrassônico virtual.
"""

import random

from app.modules.simulator.components.virtual_sensor import (
    VirtualSensor,
)


class VirtualUltrasonic(
    VirtualSensor
):

    def __init__(
        self,
        sensor_id,
        name,
        minimum=5.0,
        maximum=400.0,
        unit="cm",
    ):
        super().__init__(
            sensor_id=sensor_id,
            name=name,
            sensor_type="ULTRASONIC",
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
            2,
        )

        self.update_count += 1

        return self.set_value(
            value
        )

    def set_distance(
        self,
        distance,
    ):
        distance = float(
            distance
        )

        if distance < 0:
            raise ValueError(
                "Distância não pode "
                "ser negativa."
            )

        return self.set_value(
            distance
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

    def is_near(
        self,
        threshold,
    ):
        return (
            float(self.value)
            <= float(threshold)
        )

    def is_far(
        self,
        threshold,
    ):
        return (
            float(self.value)
            > float(threshold)
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
