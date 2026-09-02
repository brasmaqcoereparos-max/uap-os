from typing import Any

from app.modules.ui.style_sheet import (
    UIStyleSheet,
)


class UIStyleManager:

    def __init__(self):
        self._sheets: dict[
            str,
            UIStyleSheet,
        ] = {}

    def register(
        self,
        sheet: UIStyleSheet,
    ):
        self._sheets[
            sheet.name
        ] = sheet

        return sheet

    def get(
        self,
        name: str,
    ):
        return self._sheets.get(
            name
        )

    def get_or_create(
        self,
        name: str,
    ):
        sheet = self.get(name)

        if sheet:
            return sheet

        sheet = UIStyleSheet(
            name=name
        )

        return self.register(
            sheet
        )

    def resolve_widget(
        self,
        widget,
        sheet_name: str = "default",
    ):
        sheet = self.get(
            sheet_name
        )

        resolved: dict[
            str,
            Any,
        ] = {}

        if sheet:
            type_name = (
                widget.widget_type.value
            )

            resolved.update(
                sheet.resolve(
                    f"type:{type_name}"
                )
            )

            resolved.update(
                sheet.resolve(
                    f"id:{widget.id}"
                )
            )

        resolved.update(
            widget.style
        )

        return resolved

    def remove(
        self,
        name: str,
    ):
        return self._sheets.pop(
            name,
            None,
        )

    def list_all(self):
        return list(
            self._sheets.values()
        )


ui_style_manager = (
    UIStyleManager()
    )
