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
from app.modules.runtime.interlock_manager import (
    InterlockManager,
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
        self.interlocks = InterlockManager()

        self.state = AutomationState(
            project_id=project_id,
        )

    def _publish_state(
        self,
        event_type: str,
        metadata: dict | None = None,
    ) -> None:
        event_metadata = {
            "project_id": self.project_id,
        }

        if metadata:
            event_metadata.update(metadata)

        self.events.publish(
            HardwareEvent(
                event_type=event_type,
                source="runtime",
                value=self.state.to_dict(),
                metadata=event_metadata,
            )
        )

    def _check_interlocks(self) -> None:
        triggered = self.interlocks.check()

        if not triggered:
            return

        self.state.emergency_stop_now()

        self._publish_state(
            "runtime.interlock_triggered",
            {
                "interlocks": [
                    interlock.interlock_id
                    for interlock in triggered
                ],
            },
        )

        raise RuntimeError(
            "Runtime blocked by active interlock: "
            + ", ".join(
                interlock.interlock_id
                for interlock in triggered
            )
        )

    def start(self) -> None:
        self._check_interlocks()
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
        self._check_interlocks()
        self.state.resume()

        self._publish_state(
            "runtime.resumed"
        )

    def stop(self) -> None:
        self.state.stop()

        self._publish_state(
            "runtime.stopped"
        )

    def emergency_stop(
        self,
        reason: str = "Emergency stop",
    ) -> None:
        self.state.emergency_stop_now()

        self._publish_state(
            "runtime.emergency_stop",
            {
                "reason": reason,
            },
        )

    def reset_emergency_stop(self) -> None:
        if not self.interlocks.is_safe():
            raise RuntimeError(
                "Emergency stop cannot be reset "
                "while an interlock is active"
            )

        self.state.reset_emergency_stop()

        self._publish_state(
            "runtime.emergency_stop_reset"
        )

    def is_safe(self) -> bool:
        return (
            not self.state.emergency_stop
            and self.interlocks.is_safe()
        )

    def status(self) -> dict:
        triggered = self.interlocks.check()

        return {
            "project_id": self.project_id,
            "automation": self.state.to_dict(),
            "safe": (
                not self.state.emergency_stop
                and not triggered
            ),
            "interlocks": {
                "registered": len(
                    self.interlocks.list()
                ),
                "triggered": [
                    interlock.interlock_id
                    for interlock in triggered
                ],
            },
            "ports": len(
                self.ports.list()
            ),
            "sensors": len(
                self.sensors.list()
            ),
            "actuators": len(
                self.actuators.list()
            ),
    }
