from __future__ import annotations

from typing import Any

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

        self.io = IOManager(
            self.ports
        )

        self.sensors = (
            SensorManager()
        )

        self.actuators = (
            ActuatorManager()
        )

        self.events = (
            HardwareEventBus()
        )

        self.state = (
            AutomationState(
                project_id=project_id,
            )
        )

        self._install_metrics_bridge()

    def _install_metrics_bridge(
        self,
    ) -> None:

        try:
            from app.modules.metrics.runtime_metrics_bridge import (
                runtime_metrics_bridge,
            )

            runtime_metrics_bridge.attach(
                self
            )

        except ImportError:
            pass

    def _publish(
        self,
        event_type: str,
        value: Any = None,
        metadata: (
            dict[str, Any] | None
        ) = None,
    ):

        event_metadata = {
            "project_id": (
                self.project_id
            ),
            "machine_id": (
                self.project_id
            ),
        }

        if metadata:
            event_metadata.update(
                metadata
            )

        self.events.publish(
            HardwareEvent(
                event_type=event_type,
                device_id=(
                    self.project_id
                ),
                source="runtime",
                value=value,
                metadata=(
                    event_metadata
                ),
            )
        )

    def start(self) -> None:

        self.state.start()

        self._publish(
            "runtime.started"
        )

    def pause(self) -> None:

        was_running = (
            self.state.running
        )

        was_paused = (
            self.state.paused
        )

        self.state.pause()

        if (
            was_running
            and not was_paused
            and self.state.paused
        ):
            self._publish(
                "runtime.paused"
            )

    def resume(self) -> None:

        was_paused = (
            self.state.paused
        )

        self.state.resume()

        if (
            was_paused
            and not self.state.paused
            and self.state.running
        ):
            self._publish(
                "runtime.resumed"
            )

    def stop(self) -> None:

        was_running = (
            self.state.running
            or self.state.paused
        )

        self.state.stop()

        if was_running:
            self._publish(
                "runtime.stopped"
            )

    def emergency_stop(self) -> None:

        self.state.emergency_stop_now()

        self._publish(
            "runtime.emergency_stop"
        )

    def complete_cycle(
        self,
        duration_seconds: float,
        *,
        good_units: int = 1,
        rejected_units: int = 0,
        metadata: (
            dict[str, Any] | None
        ) = None,
    ) -> None:

        self.state.increment_cycle()

        self._publish(
            "runtime.cycle_completed",
            value={
                "cycle": (
                    self.state.cycle
                ),
                "duration_seconds": (
                    float(
                        duration_seconds
                    )
                ),
                "good_units": (
                    int(
                        good_units
                    )
                ),
                "rejected_units": (
                    int(
                        rejected_units
                    )
                ),
            },
            metadata=metadata,
        )

    def publish_telemetry(
        self,
        name: str,
        value: float,
        *,
        unit: str = "",
        tags: (
            dict[str, str] | None
        ) = None,
        metadata: (
            dict[str, Any] | None
        ) = None,
    ) -> None:

        self._publish(
            "runtime.telemetry",
            value={
                "name": name,
                "value": value,
                "unit": unit,
                "tags": dict(
                    tags or {}
                ),
            },
            metadata=metadata,
        )

    def publish_fault(
        self,
        code: str,
        message: str,
        *,
        severity: str = "error",
        metadata: (
            dict[str, Any] | None
        ) = None,
    ) -> None:

        self._publish(
            "runtime.fault",
            value={
                "code": code,
                "message": message,
                "severity": severity,
            },
            metadata=metadata,
        )

    def record_consumption(
        self,
        resource: str,
        amount: float,
        *,
        unit: str = "",
        metadata: (
            dict[str, Any] | None
        ) = None,
    ) -> None:

        self._publish(
            "runtime.consumption",
            value={
                "resource": resource,
                "amount": float(
                    amount
                ),
                "unit": unit,
            },
            metadata=metadata,
        )

    def status(self) -> dict:

        return {
            "project_id": (
                self.project_id
            ),
            "automation": (
                self.state.to_dict()
            ),
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
