from __future__ import annotations

from typing import Any

from app.modules.metrics.consumption_service import (
    consumption_service,
)
from app.modules.metrics.fault_service import (
    fault_service,
)
from app.modules.metrics.history_service import (
    metrics_history_service,
)
from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)
from app.modules.runtime.hardware_events import (
    HardwareEvent,
)


class RuntimeMetricsBridge:

    EVENT_TYPES = (
        "runtime.started",
        "runtime.paused",
        "runtime.resumed",
        "runtime.stopped",
        "runtime.emergency_stop",
        "runtime.cycle_completed",
        "runtime.telemetry",
        "runtime.fault",
        "runtime.consumption",
    )

    def __init__(self):
        self._contexts: set[
            int
        ] = set()

        self._handlers = {
            "runtime.started": (
                self._runtime_started
            ),
            "runtime.paused": (
                self._runtime_paused
            ),
            "runtime.resumed": (
                self._runtime_resumed
            ),
            "runtime.stopped": (
                self._runtime_stopped
            ),
            "runtime.emergency_stop": (
                self._emergency_stop
            ),
            "runtime.cycle_completed": (
                self._cycle_completed
            ),
            "runtime.telemetry": (
                self._telemetry
            ),
            "runtime.fault": (
                self._fault
            ),
            "runtime.consumption": (
                self._consumption
            ),
        }

    def attach(
        self,
        context,
    ) -> bool:

        context_key = id(
            context
        )

        if (
            context_key
            in self._contexts
        ):
            return False

        event_bus = getattr(
            context,
            "events",
            None,
        )

        if event_bus is None:
            raise ValueError(
                "Runtime context has "
                "no event bus"
            )

        for (
            event_type,
            handler,
        ) in self._handlers.items():

            event_bus.subscribe(
                event_type,
                handler,
            )

        self._contexts.add(
            context_key
        )

        return True

    def detach(
        self,
        context,
    ) -> bool:

        context_key = id(
            context
        )

        if (
            context_key
            not in self._contexts
        ):
            return False

        event_bus = getattr(
            context,
            "events",
            None,
        )

        if event_bus is not None:

            for (
                event_type,
                handler,
            ) in self._handlers.items():

                event_bus.unsubscribe(
                    event_type,
                    handler,
                )

        self._contexts.discard(
            context_key
        )

        return True

    def _machine_id(
        self,
        event: HardwareEvent,
    ) -> str:

        machine_id = (
            event.metadata.get(
                "machine_id"
            )
            or event.metadata.get(
                "project_id"
            )
            or event.device_id
            or event.source
            or "runtime"
        )

        return str(
            machine_id
        )

    def _record_state(
        self,
        event: HardwareEvent,
        state: str,
        value: float,
    ):

        machine_id = (
            self._machine_id(
                event
            )
        )

        telemetry_service.record(
            name="runtime_state",
            value=value,
            source=machine_id,
            tags={
                "state": state,
            },
            metadata={
                "event_type": (
                    event.event_type
                ),
            },
        )

        metrics_history_service.record(
            "runtime_state",
            {
                "state": state,
                "value": value,
                "event_type": (
                    event.event_type
                ),
            },
            source=machine_id,
            timestamp=event.timestamp,
        )

    def _runtime_started(
        self,
        event: HardwareEvent,
    ):

        self._record_state(
            event,
            "running",
            1.0,
        )

    def _runtime_paused(
        self,
        event: HardwareEvent,
    ):

        self._record_state(
            event,
            "paused",
            0.0,
        )

    def _runtime_resumed(
        self,
        event: HardwareEvent,
    ):

        self._record_state(
            event,
            "running",
            1.0,
        )

    def _runtime_stopped(
        self,
        event: HardwareEvent,
    ):

        self._record_state(
            event,
            "stopped",
            0.0,
        )

    def _emergency_stop(
        self,
        event: HardwareEvent,
    ):

        machine_id = (
            self._machine_id(
                event
            )
        )

        self._record_state(
            event,
            "emergency_stop",
            0.0,
        )

        fault_service.record(
            machine_id=machine_id,
            code="EMERGENCY_STOP",
            message=(
                "Runtime emergency stop"
            ),
            severity="critical",
            metadata=dict(
                event.metadata
            ),
        )

    def _cycle_completed(
        self,
        event: HardwareEvent,
    ):

        machine_id = (
            self._machine_id(
                event
            )
        )

        data = (
            event.value
            if isinstance(
                event.value,
                dict,
            )
            else {}
        )

        cycle = (
            production_service
            .record_cycle(
                machine_id=(
                    machine_id
                ),
                duration_seconds=float(
                    data.get(
                        "duration_seconds",
                        0.0,
                    )
                ),
                good_units=int(
                    data.get(
                        "good_units",
                        1,
                    )
                ),
                rejected_units=int(
                    data.get(
                        "rejected_units",
                        0,
                    )
                ),
                metadata=dict(
                    event.metadata
                ),
            )
        )

        metrics_history_service.record(
            "cycle",
            cycle.to_dict(),
            source=machine_id,
            timestamp=event.timestamp,
        )

    def _telemetry(
        self,
        event: HardwareEvent,
    ):

        machine_id = (
            self._machine_id(
                event
            )
        )

        data = (
            event.value
            if isinstance(
                event.value,
                dict,
            )
            else {}
        )

        name = str(
            data.get(
                "name",
                "",
            )
        ).strip()

        if not name:
            return

        value = data.get(
            "value"
        )

        if value is None:
            return

        point = telemetry_service.record(
            name=name,
            value=float(
                value
            ),
            unit=str(
                data.get(
                    "unit",
                    "",
                )
            ),
            source=machine_id,
            tags=dict(
                data.get(
                    "tags",
                    {},
                )
                or {}
            ),
            metadata=dict(
                event.metadata
            ),
        )

        metrics_history_service.record(
            "telemetry",
            point.to_dict(),
            source=machine_id,
            timestamp=event.timestamp,
        )

    def _fault(
        self,
        event: HardwareEvent,
    ):

        machine_id = (
            self._machine_id(
                event
            )
        )

        data = (
            event.value
            if isinstance(
                event.value,
                dict,
            )
            else {}
        )

        fault_service.record(
            machine_id=machine_id,
            code=str(
                data.get(
                    "code",
                    "RUNTIME_FAULT",
                )
            ),
            message=str(
                data.get(
                    "message",
                    "Runtime fault",
                )
            ),
            severity=str(
                data.get(
                    "severity",
                    "error",
                )
            ),
            metadata={
                **dict(
                    event.metadata
                ),
                **dict(
                    data.get(
                        "metadata",
                        {},
                    )
                    or {}
                ),
            },
        )

    def _consumption(
        self,
        event: HardwareEvent,
    ):

        machine_id = (
            self._machine_id(
                event
            )
        )

        data = (
            event.value
            if isinstance(
                event.value,
                dict,
            )
            else {}
        )

        resource = str(
            data.get(
                "resource",
                "",
            )
        ).strip()

        if not resource:
            return

        amount = float(
            data.get(
                "amount",
                0.0,
            )
        )

        total = (
            consumption_service.add(
                machine_id,
                resource,
                amount,
            )
        )

        metrics_history_service.record(
            "consumption",
            {
                "resource": resource,
                "amount": amount,
                "total": total,
                "unit": data.get(
                    "unit",
                    "",
                ),
            },
            source=machine_id,
            timestamp=event.timestamp,
        )


runtime_metrics_bridge = (
    RuntimeMetricsBridge()
        )
