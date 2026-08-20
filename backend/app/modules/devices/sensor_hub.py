from __future__ import annotations

from app.modules.devices.distance_sensor_manager import (
    DistanceSensorManager,
)
from app.modules.devices.temperature_manager import (
    TemperatureManager,
)
from app.modules.devices.pressure_manager import (
    PressureManager,
)
from app.modules.devices.electrical_sensor_manager import (
    ElectricalSensorManager,
)
from app.modules.devices.presence_sensor_manager import (
    PresenceSensorManager,
)
from app.modules.devices.light_sensor_manager import (
    LightSensorManager,
)


class SensorHub:
    """
    Centro universal de sensores do UAP.

    Permite combinar sensores diferentes em
    qualquer projeto criado pelo sistema.
    """

    def __init__(self) -> None:
        self.distance = DistanceSensorManager()
        self.temperature = TemperatureManager()
        self.pressure = PressureManager()
        self.electrical = ElectricalSensorManager()
        self.presence = PresenceSensorManager()
        self.light = LightSensorManager()

    def status(self) -> dict:
        return {
            "distance": len(
                self.distance.list()
            ),
            "temperature": len(
                self.temperature.list()
            ),
            "pressure": len(
                self.pressure.list()
            ),
            "electrical": len(
                self.electrical.list()
            ),
            "presence": len(
                self.presence.list()
            ),
            "light": len(
                self.light.list()
            ),
            "presence_detected":
                self.presence.any_detected(),
        }
