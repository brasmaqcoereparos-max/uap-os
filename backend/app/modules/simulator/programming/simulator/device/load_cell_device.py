"""
Célula de carga / sensor de peso simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class LoadCellDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="sensor",
            description=(
                "Célula de carga / "
                "sensor de peso"
            ),
            icon="scale",
        )

        self.weight = 0.0
        self.tare_value = 0.0
        self.calibration_factor = 1.0

        self.unit = "kg"

    def set_weight(
        self,
        weight,
    ):
        if not self.enabled:
            return False

        self.weight = max(
            0.0,
            float(weight),
        )

        return self.weight

    def read(self):
        value = (
            self.weight
            - self.tare_value
        ) * self.calibration_factor

        return max(
            0.0,
            value,
        )

    def tare(self):
        self.tare_value = (
            self.weight
        )

        return self.tare_value

    def calibrate(
        self,
        factor,
    ):
        factor = float(factor)

        if factor <= 0:
            raise ValueError(
                "O fator de calibração "
                "deve ser maior que zero."
            )

        self.calibration_factor = (
            factor
        )

        return self.calibration_factor

    def set_unit(
        self,
        unit,
    ):
        self.unit = str(unit)

        return self.unit

    def get_raw_value(self):
        return self.weight

    def get_calibration_factor(self):
        return self.calibration_factor

    def update(self):
        return self.read()

    def reset(self):
        self.weight = 0.0
        self.tare_value = 0.0
        self.calibration_factor = 1.0

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "weight": self.weight,
            "value": self.read(),
            "tare_value": (
                self.tare_value
            ),
            "calibration_factor": (
                self.calibration_factor
            ),
            "unit": self.unit,
        })

        return data
