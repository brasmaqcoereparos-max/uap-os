from __future__ import annotations

from app.modules.devices.actuator_manager import (
    ActuatorManager,
)
from app.modules.devices.sensor_manager import (
    SensorManager,
)
from app.modules.runtime.automation_state import (
    AutomationState,
)
from app.modules.runtime.hardware_events import (
    HardwareEventBus,
)
from app.modules.runtime.io_manager import (
    IOManager,
)
from app.modules.uhal.port_manager import (
    PortManager,
)


class RuntimeContext:
    def __init__(
        self,
        project_id: str,
    ) -> None:
        self.project_id = project_id

        self.ports = PortManager()
        self.io = IOManager(self.ports)

        self.sensors = SensorManager()
        self.actuators = ActuatorManager()

        self.events = HardwareEventBus()

        self.state = AutomationState(
            project_id=project_id,
        )

    def start(self) -> None:
        self.state.start()

    def pause(self) -> None:
        self.state.pause()

    def resume(self) -> None:
        self.state.resume()

    def stop(self) -> None:
        self.state.stop()

    def emergency_stop(self) -> None:
        self.state.emergency_stop_now()

    def status(self) -> dict:
        return {
            "project_id": self.project_id,
            "automation": self.state.to_dict(),
            "ports": len(self.ports.list()),
            "sensors": len(self.sensors.list()),
            "actuators": len(self.actuators.list()),
        }
