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
        super().__init__(name)

        self.weight = 0.0
        self.tare_value = 0.0
        self.calibration_factor = 1.0

    def set_weight(
        self,
        weight,
    ):
        self.weight = max(
            0.0,
            float(weight),
        )

    def read(self):
        return (
            self.weight
            - self.tare_value
        ) * self.calibration_factor

    def tare(self):
        self.tare_value = self.weight

    def calibrate(
        self,
        factor,
    ):
        factor = float(factor)

        if factor <= 0:
            raise ValueError(
                "O fator de calibração deve ser maior que zero."
            )

        self.calibration_factor = factor

    def get_raw_value(self):
        return self.weight

    def get_calibration_factor(self):
        return self.calibration_factor

    def update(self):
        pass

    def reset(self):
        self.weight = 0.0
        self.tare_value = 0.0
        self.calibration_factor = 1.0
