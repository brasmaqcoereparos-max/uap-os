from typing import Any

from app.modules.ui.runtime_bridge import (
    ui_runtime_bridge,
)
from app.modules.ui.telemetry_buffer import (
    ui_telemetry_buffer,
)


class UITelemetryBridge:

    def publish(
        self,
        key: str,
        value: Any,
    ):
        sample = (
            ui_telemetry_buffer.add(
                key,
                value,
            )
        )

        ui_runtime_bridge.update_state(
            key,
            value,
        )

        return sample

    def publish_many(
        self,
        values: dict[str, Any],
    ):
        samples = []

        for key, value in values.items():
            samples.append(
                ui_telemetry_buffer.add(
                    key,
                    value,
                )
            )

        ui_runtime_bridge.update_many(
            values
        )

        return samples

    def latest(
        self,
        key: str | None = None,
    ):
        return (
            ui_telemetry_buffer.latest(
                key
            )
        )


ui_telemetry_bridge = (
    UITelemetryBridge()
)
