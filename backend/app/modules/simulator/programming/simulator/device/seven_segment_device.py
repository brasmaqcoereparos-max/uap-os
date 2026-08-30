"""
Display de sete segmentos simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class SevenSegmentDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="display",
            description=(
                "Display de sete segmentos"
            ),
            icon="display",
        )

        self.value = 0
        self.decimal_point = False

    def display(
        self,
        value,
    ):
        if not self.enabled:
            return False

        self.value = max(
            0,
            min(
                9,
                int(value),
            ),
        )

        return self.value

    def clear(self):
        self.value = 0
        self.decimal_point = False

        return True

    def set_decimal_point(
        self,
        enabled,
    ):
        self.decimal_point = bool(
            enabled
        )

        return self.decimal_point

    def enable(self):
        super().enable()
        return self

    def disable(self):
        super().disable()
        return self

    def update(self):
        return self.value

    def reset(self):
        self.value = 0
        self.decimal_point = False
        self.enabled = True

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "value": self.value,
            "decimal_point": (
                self.decimal_point
            ),
        })

        return data
