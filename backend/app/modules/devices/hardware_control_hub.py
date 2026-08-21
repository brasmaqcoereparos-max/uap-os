from __future__ import annotations

from app.modules.devices.sensor_hub import (
    SensorHub,
)
from app.modules.devices.actuator_hub import (
    ActuatorHub,
)
from app.modules.devices.hardware_hub import (
    HardwareHub,
)
from app.modules.runtime.motion_hub import (
    MotionHub,
)


class HardwareControlHub:
    """
    Integração central do hardware do UAP Box.

    Sensores -> processamento -> movimento -> atuadores.

    Esta camada permite que o mesmo núcleo seja usado
    em diferentes máquinas, robôs e automações.
    """

    def __init__(self) -> None:
        self.hardware = HardwareHub()
        self.sensors = SensorHub()
        self.actuators = ActuatorHub()
        self.motion = MotionHub()

    def emergency_stop(self) -> None:
        self.actuators.stop_all()
        self.motion.emergency_stop()

    def is_safe(self) -> bool:
        return self.motion.is_safe()

    def status(self) -> dict:
        return {
            "hardware": self.hardware.status(),
            "sensors": self.sensors.status(),
            "actuators": self.actuators.status(),
            "motion": self.motion.status(),
            "safe": self.is_safe(),
        }
