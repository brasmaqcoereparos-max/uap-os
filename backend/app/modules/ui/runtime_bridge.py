from __future__ import annotations

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

        ui_event_bus.publish(
            event
        )

        self.refresh_bindings()

        return value

    def update_many(
        self,
        values: dict[str, Any],
    ):
        for (
            key,
            value,
        ) in values.items():
            ui_state.set(
                key,
                value,
            )

        event = UIEvent(
            name="state_batch_changed",
            payload={
                "values": dict(
                    values
                ),
            },
        )

        ui_event_bus.publish(
            event
        )

        self.refresh_bindings()

        return ui_state.snapshot()

    def update_runtime_status(
        self,
        status: dict[str, Any],
    ):
        if not isinstance(
            status,
            dict,
        ):
            raise TypeError(
                "Runtime status must be a dict"
            )

        values = {
            f"runtime.{key}": value
            for key, value
            in status.items()
        }

        return self.update_many(
            values
        )

    def refresh_bindings(
        self,
        screen_id: str | None = None,
    ):
        results = {}

        screens = (
            ui_registry.list_screens()
        )

        if screen_id is not None:
            screen = (
                ui_registry.get_screen(
                    screen_id
                )
            )

            screens = (
                [screen]
                if screen is not None
                else []
            )

        for screen in screens:
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

    def get_state(
        self,
        key: str,
        default: Any = None,
    ):
        getter = getattr(
            ui_state,
            "get",
            None,
        )

        if callable(getter):
            return getter(
                key,
                default,
            )

        return (
            ui_state.snapshot()
            .get(
                key,
                default,
            )
        )

    def snapshot(self):
        return {
            "state": (
                ui_state.snapshot()
            ),
            "screens": [
                screen.to_dict()
                for screen
                in ui_registry.list_screens()
            ],
        }


ui_runtime_bridge = (
    UIRuntimeBridge()
        )
