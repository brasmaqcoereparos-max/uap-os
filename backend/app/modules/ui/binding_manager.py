from app.modules.ui.binding import (
    UIBinding,
)
from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.state import (
    UIState,
)


class UIBindingManager:

    def __init__(self):
        self._bindings: dict[
            str,
            UIBinding,
        ] = {}

    def register(
        self,
        binding: UIBinding,
    ):
        self._bindings[
            binding.id
        ] = binding

        return binding

    def get(
        self,
        binding_id: str,
    ):
        return self._bindings.get(
            binding_id
        )

    def remove(
        self,
        binding_id: str,
    ):
        return self._bindings.pop(
            binding_id,
            None,
        )

    def list_all(self):
        return list(
            self._bindings.values()
        )

    def apply_screen(
        self,
        screen: UIScreen,
        state: UIState,
    ):
        if not screen.layout:
            return []

        widgets = {
            widget.id: widget
            for widget
            in screen.layout.widgets
        }

        applied = []

        for binding in self._bindings.values():
            widget = widgets.get(
                binding.widget_id
            )

            if not widget:
                continue

            value = binding.apply(
                widget,
                state,
            )

            applied.append(
                {
                    "binding_id": (
                        binding.id
                    ),
                    "widget_id": (
                        widget.id
                    ),
                    "value": value,
                }
            )

        return applied


ui_binding_manager = (
    UIBindingManager()
      )
