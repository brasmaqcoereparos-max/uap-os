from __future__ import annotations

from app.modules.devices.actuator_manager import ActuatorManager
from app.modules.devices.camera_manager import CameraManager
from app.modules.devices.display_manager import DisplayManager
from app.modules.devices.motor_manager import MotorManager
from app.modules.devices.pump_manager import PumpManager
from app.modules.devices.relay_manager import RelayManager
from app.modules.devices.sensor_manager import SensorManager
from app.modules.devices.servo_manager import ServoManager


class DeviceHub:
    """
    Ponto único de gerenciamento dos principais
    dispositivos físicos do UAP.
    """

    def __init__(self) -> None:
        self.sensors = SensorManager()
        self.actuators = ActuatorManager()

        self.motors = MotorManager()
        self.servos = ServoManager()
        self.pumps = PumpManager()
        self.relays = RelayManager()

        self.cameras = CameraManager()
        self.displays = DisplayManager()

    def status(self) -> dict[str, int]:
        return {
            "sensors": len(self.sensors.list()),
            "actuators": len(self.actuators.list()),
            "motors": len(self.motors.list()),
            "servos": len(self.servos.list()),
            "pumps": len(self.pumps.list()),
            "relays": len(self.relays.list()),
            "cameras": len(self.cameras.list()),
            "displays": len(self.displays.list()),
        }
