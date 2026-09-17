from __future__ import annotations

from typing import Any

from app.modules.runtime.runtime_context import (
    RuntimeContext,
)
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

    ALLOWED_RUNTIME_ACTIONS = {
        "start",
        "pause",
        "resume",
        "stop",
        "emergency_stop",
        "reset_emergency_stop",
        "status",
    }

    def __init__(self) -> None:
        self._runtime: (
            RuntimeContext | None
        ) = None

    def bind_runtime(
        self,
        runtime: RuntimeContext,
    ) -> RuntimeContext:
        if not isinstance(
            runtime,
            RuntimeContext,
        ):
            raise TypeError(
                "runtime must be a "
                "RuntimeContext"
            )

        self._runtime = runtime

        self.update_runtime_status(
            runtime.status()
        )

        ui_event_bus.publish(
            UIEvent(
                name="runtime_bound",
                payload={
                    "project_id": (
                        runtime.project_id
                    ),
                },
            )
        )

        return runtime

    def unbind_runtime(self) -> None:
        runtime = self._runtime

        self._runtime = None

        ui_event_bus.publish(
            UIEvent(
                name="runtime_unbound",
                payload={
                    "project_id": (
                        runtime.project_id
                        if runtime
                        else None
                    ),
                },
            )
        )

    def runtime_bound(self) -> bool:
        return self._runtime is not None

    def runtime(
        self,
    ) -> RuntimeContext | None:
        return self._runtime

    def require_runtime(
        self,
    ) -> RuntimeContext:
        if self._runtime is None:
            raise RuntimeError(
                "No RuntimeContext is bound "
                "to the UI"
            )

        return self._runtime

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

    def refresh_runtime_status(
        self,
    ) -> dict:
        runtime = (
            self.require_runtime()
        )

        status = runtime.status()

        self.update_runtime_status(
            status
        )

        return status

    def execute_runtime_action(
        self,
        action: str,
        parameters: (
            dict[str, Any] | None
        ) = None,
    ):
        runtime = (
            self.require_runtime()
        )

        normalized = str(
            action
        ).strip().lower()

        if (
            normalized
            not in self.ALLOWED_RUNTIME_ACTIONS
        ):
            raise ValueError(
                "Unsupported runtime action: "
                f"{action}"
            )

        parameters = dict(
            parameters or {}
        )

        if normalized == "start":
            runtime.start()
            result = runtime.status()

        elif normalized == "pause":
            runtime.pause()
            result = runtime.status()

        elif normalized == "resume":
            runtime.resume()
            result = runtime.status()

        elif normalized == "stop":
            runtime.stop()
            result = runtime.status()

        elif (
            normalized
            == "emergency_stop"
        ):
            reason = str(
                parameters.get(
                    "reason",
                    "UI emergency stop",
                )
            )

            runtime.emergency_stop(
                reason
            )

            result = runtime.status()

        elif (
            normalized
            == "reset_emergency_stop"
        ):
            runtime.reset_emergency_stop()

            result = runtime.status()

        elif normalized == "status":
            result = runtime.status()

        else:
            raise ValueError(
                "Unsupported runtime action: "
                f"{action}"
            )

        self.update_runtime_status(
            result
        )

        ui_event_bus.publish(
            UIEvent(
                name=(
                    "runtime_action_executed"
                ),
                payload={
                    "action": normalized,
                    "project_id": (
                        runtime.project_id
                    ),
                    "status": result,
                },
            )
        )

        return {
            "executed": True,
            "action": normalized,
            "project_id": (
                runtime.project_id
            ),
            "status": result,
        }

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
        runtime_status = None

        if self._runtime is not None:
            runtime_status = (
                self._runtime.status()
            )

        return {
            "runtime_bound": (
                self.runtime_bound()
            ),
            "runtime": runtime_status,
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
