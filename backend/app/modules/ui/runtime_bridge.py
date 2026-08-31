from typing import Any

from app.modules.ui.binding_manager import (
    ui_binding_manager,
)
from app.modules.ui.event import (
    UIEvent,
)
from app.modules.ui.event_bus import (
    ui_event_bus,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.state import (
    ui_state,
)


class UIRuntimeBridge:

    def update_state(
        self,
        key: str,
        value: Any,
    ):
        ui_state.set(
            key,
            value,
        )

        event = UIEvent(
            name="state_changed",
            payload={
                "key": key,
                "value": value,
            },
        )

        ui_event_bus.publish(event)

        self.refresh_bindings()

        return value

    def update_many(
        self,
        values: dict[str, Any],
    ):
        for key, value in values.items():
            ui_state.set(
                key,
                value,
            )

        event = UIEvent(
            name="state_batch_changed",
            payload={
                "values": dict(values),
            },
        )

        ui_event_bus.publish(event)

        self.refresh_bindings()

        return ui_state.snapshot()

    def refresh_bindings(self):
        results = {}

        for screen in (
            ui_registry.list_screens()
        ):
            applied = (
                ui_binding_manager
                .apply_screen(
                    screen,
                    ui_state,
                )
            )

            if applied:
                results[
                    screen.id
                ] = applied

        return results

    def snapshot(self):
        return {
            "state": ui_state.snapshot(),
            "screens": [
                screen.to_dict()
                for screen
                in ui_registry.list_screens()
            ],
        }


ui_runtime_bridge = (
    UIRuntimeBridge()
)
