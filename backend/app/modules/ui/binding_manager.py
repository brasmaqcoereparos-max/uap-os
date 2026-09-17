from __future__ import annotations

import uuid

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

    def create(
        self,
        widget_id: str,
        property_name: str,
        state_key: str,
        default=None,
    ):
        binding = UIBinding(
            id=str(
                uuid.uuid4()
            ),
            widget_id=widget_id,
            property_name=property_name,
            state_key=state_key,
            default=default,
        )

        return self.register(
            binding
        )

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

    def remove_widget(
        self,
        widget_id: str,
    ) -> int:
        ids = [
            binding.id
            for binding
            in self._bindings.values()
            if binding.widget_id
            == widget_id
        ]

        for binding_id in ids:
            self.remove(
                binding_id
            )

        return len(ids)

    def list_all(self):
        return list(
            self._bindings.values()
        )

    def for_widget(
        self,
        widget_id: str,
    ):
        return [
            binding
            for binding
            in self._bindings.values()
            if binding.widget_id
            == widget_id
        ]

    def for_state(
        self,
        state_key: str,
    ):
        return [
            binding
            for binding
            in self._bindings.values()
            if binding.state_key
            == state_key
        ]

    def apply_widget(
        self,
        widget,
        state: UIState,
    ):
        applied = []

        for binding in (
            self.for_widget(
                widget.id
            )
        ):
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
                    "property_name": (
                        binding
                        .property_name
                    ),
                    "value": value,
                }
            )

        return applied

    def apply_screen(
        self,
        screen: UIScreen,
        state: UIState,
    ):
        if not screen.layout:
            return []

        applied = []

        for widget in (
            screen.layout.widgets
        ):
            applied.extend(
                self.apply_widget(
                    widget,
                    state,
                )
            )

        return applied

    def write_back(
        self,
        widget,
        state: UIState,
    ):
        written = []

        for binding in (
            self.for_widget(
                widget.id
            )
        ):
            value = (
                binding.write_back(
                    widget,
                    state,
                )
            )

            written.append(
                {
                    "binding_id": (
                        binding.id
                    ),
                    "state_key": (
                        binding.state_key
                    ),
                    "value": value,
                }
            )

        return written

    def snapshot(self):
        return [
            binding.to_dict()
            for binding
            in self.list_all()
        ]

    def clear(self):
        self._bindings.clear()


ui_binding_manager = (
    UIBindingManager()
            )
