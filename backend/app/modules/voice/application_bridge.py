from typing import Any

from app.modules.ui.command_dispatcher import (
    ui_command_dispatcher,
)


class VoiceApplicationBridge:

    def dispatch(
        self,
        command: str,
        parameters: (
            dict[str, Any] | None
        ) = None,
    ):
        parameters = dict(
            parameters or {}
        )

        if command.startswith(
            "ui."
        ):
            return (
                ui_command_dispatcher
                .dispatch(
                    command,
                    parameters,
                )
            )

        return {
            "accepted": True,
            "target": "application",
            "command": command,
            "parameters": parameters,
        }


voice_application_bridge = (
    VoiceApplicationBridge()
)
