from app.modules.ui.action_executor import (
    ui_action_executor,
)
from app.modules.ui.event import (
    UIEvent,
)
from app.modules.ui.event_bus import (
    ui_event_bus,
)
from app.modules.ui.input_event import (
    UIInputEvent,
)
from app.modules.ui.registry import (
    ui_registry,
)


class UIInteractionManager:

    def handle(
        self,
        screen_id: str,
        input_event: UIInputEvent,
    ):
        screen = ui_registry.get_screen(
            screen_id
        )

        if (
            not screen
            or not screen.layout
        ):
            raise ValueError(
                "Screen not found"
            )

        if not input_event.target_id:
            event = UIEvent(
                name=input_event.event_type,
                screen_id=screen_id,
                payload=(
                    input_event.to_dict()
                ),
            )

            ui_event_bus.publish(event)

            return {
                "handled": True,
                "action": None,
            }

        widget = screen.layout.get_widget(
            input_event.target_id
        )

        if not widget:
            raise ValueError(
                "Widget not found"
            )

        event = UIEvent(
            name=input_event.event_type,
            widget_id=widget.id,
            screen_id=screen_id,
            payload=(
                input_event.to_dict()
            ),
        )

        ui_event_bus.publish(event)

        result = None

        if input_event.event_type in {
            "click",
            "tap",
            "submit",
            "change",
        }:
            result = (
                ui_action_executor.execute(
                    widget,
                    payload={
                        "value": (
                            input_event.value
                        )
                    },
                )
            )

        return {
            "handled": True,
            "widget_id": widget.id,
            "action": result,
        }


ui_interaction_manager = (
    UIInteractionManager()
      )
