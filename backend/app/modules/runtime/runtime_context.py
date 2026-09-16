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
    HardwareEvent,
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

    def _publish_state(
        self,
        event_type: str,
    ) -> None:
        self.events.publish(
            HardwareEvent(
                event_type=event_type,
                source="runtime",
                value=self.state.to_dict(),
                metadata={
                    "project_id": self.project_id,
                },
            )
        )

    def start(self) -> None:
        self.state.start()
        self._publish_state(
            "runtime.started"
        )

    def pause(self) -> None:
        self.state.pause()
        self._publish_state(
            "runtime.paused"
        )

    def resume(self) -> None:
        self.state.resume()
        self._publish_state(
            "runtime.resumed"
        )

    def stop(self) -> None:
        self.state.stop()
        self._publish_state(
            "runtime.stopped"
        )

    def emergency_stop(self) -> None:
        self.state.emergency_stop_now()
        self._publish_state(
            "runtime.emergency_stop"
        )

    def reset_emergency_stop(self) -> None:
        self.state.reset_emergency_stop()
        self._publish_state(
            "runtime.emergency_stop_reset"
        )

    def status(self) -> dict:
        return {
            "project_id": self.project_id,
            "automation": self.state.to_dict(),
            "ports": len(self.ports.list()),
            "sensors": len(self.sensors.list()),
            "actuators": len(self.actuators.list()),
        }
