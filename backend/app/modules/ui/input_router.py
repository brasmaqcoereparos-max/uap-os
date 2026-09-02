from app.modules.ui.command_dispatcher import (
    ui_command_dispatcher,
)
from app.modules.ui.input_event import (
    UIInputEvent,
)
from app.modules.ui.interaction_manager import (
    ui_interaction_manager,
)


class UIInputRouter:

    def route(
        self,
        screen_id: str,
        event: UIInputEvent,
    ):
        if (
            event.event_type
            == "key_down"
            and event.key
        ):
            result = (
                ui_command_dispatcher
                .dispatch_shortcut(
                    event.key,
                    event.modifiers,
                )
            )

            if result is not None:
                return {
                    "handled": True,
                    "source": (
                        "shortcut"
                    ),
                    "result": result,
                }

        result = (
            ui_interaction_manager
            .handle(
                screen_id,
                event,
            )
        )

        return {
            "handled": True,
            "source": (
                "interaction"
            ),
            "result": result,
        }


ui_input_router = UIInputRouter()
