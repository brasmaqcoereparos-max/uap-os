from __future__ import annotations

from app.modules.metrics.history_service import (
    metrics_history_service,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)


class MetricsEnergyBridge:

    def record(
        self,
        machine_id: str,
        *,
        voltage: float,
        current: float,
        duration_seconds: (
            float | None
        ) = None,
    ):

        normalized_voltage = float(
            voltage
        )

        normalized_current = float(
            current
        )

        power_watts = (
            normalized_voltage
            * normalized_current
        )

        telemetry_service.record(
            "voltage",
            normalized_voltage,
            unit="V",
            source=machine_id,
        )

        telemetry_service.record(
            "current",
            normalized_current,
            unit="A",
            source=machine_id,
        )

        telemetry_service.record(
            "power",
            power_watts,
            unit="W",
            source=machine_id,
        )

        energy_kwh = None

        if duration_seconds is not None:

            duration = max(
                0.0,
                float(
                    duration_seconds
                ),
            )

            energy_kwh = (
                power_watts
                * duration
                / 3_600_000.0
            )

        result = {
            "machine_id": (
                machine_id
            ),
            "voltage": (
                normalized_voltage
            ),
            "current": (
                normalized_current
            ),
            "power_watts": (
                power_watts
            ),
            "duration_seconds": (
                duration_seconds
            ),
            "energy_kwh": (
                energy_kwh
            ),
        }

        metrics_history_service.record(
            "energy",
            result,
            source=machine_id,
        )

        return result

    def from_runtime_reading(
        self,
        machine_id: str,
        reading,
        *,
        duration_seconds: (
            float | None
        ) = None,
    ):

        if reading is None:
            raise ValueError(
                "Energy reading "
                "is required"
            )

        return self.record(
            machine_id,
            voltage=(
                reading.voltage
            ),
            current=(
                reading.current
            ),
            duration_seconds=(
                duration_seconds
            ),
        )


metrics_energy_bridge = (
    MetricsEnergyBridge()
      )
