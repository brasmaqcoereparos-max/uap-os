from __future__ import annotations

from typing import Any

from app.modules.ui.property_definition import (
    UIPropertyDefinition,
)
from app.modules.ui.property_schema import (
    UIPropertySchema,
)


class UIPropertyInspector:

    def __init__(self):
        self._schemas: dict[
            str,
            UIPropertySchema,
        ] = {}

        self._register_defaults()

    def _register_defaults(self):
        widget = UIPropertySchema(
            target_type="widget"
        )

        definitions = [
            UIPropertyDefinition(
                name="name",
                label="Name",
                required=True,
            ),
            UIPropertyDefinition(
                name="x",
                value_type="number",
                category="geometry",
            ),
            UIPropertyDefinition(
                name="y",
                value_type="number",
                category="geometry",
            ),
            UIPropertyDefinition(
                name="width",
                value_type="number",
                category="geometry",
                minimum=1,
            ),
            UIPropertyDefinition(
                name="height",
                value_type="number",
                category="geometry",
                minimum=1,
            ),
            UIPropertyDefinition(
                name="visible",
                value_type="boolean",
                category="behavior",
            ),
            UIPropertyDefinition(
                name="enabled",
                value_type="boolean",
                category="behavior",
            ),
            UIPropertyDefinition(
                name="value",
                value_type="any",
                category="data",
            ),
        ]

        for definition in definitions:
            widget.add(
                definition
            )

        self.register_schema(
            widget
        )

    def register_schema(
        self,
        schema: UIPropertySchema,
    ):
        self._schemas[
            schema.target_type
        ] = schema

        return schema

    def schema(
        self,
        target_type: str,
    ):
        return self._schemas.get(
            target_type
        )

    def inspect_widget(
        self,
        widget,
    ):
        schema = self.schema(
            "widget"
        )

        if not schema:
            return {
                "schema": None,
                "values": {},
            }

        values = {}

        for definition in (
            schema.properties
        ):
            if hasattr(
                widget,
                definition.name,
            ):
                value = getattr(
                    widget,
                    definition.name
                )
            else:
                value = (
                    widget.properties.get(
                        definition.name,
                        definition.default,
                    )
                )

            values[
                definition.name
            ] = value

        return {
            "schema": (
                schema.to_dict()
            ),
            "values": values,
        }

    def update_widget(
        self,
        widget,
        values: dict[
            str,
            Any,
        ],
    ):
        schema = self.schema(
            "widget"
        )

        if not schema:
            return widget

        validated = schema.validate(
            values,
            partial=True,
        )

        for (
            key,
            value,
        ) in validated.items():
            definition = (
                schema.get(
                    key
                )
            )

            if (
                definition is None
                or not definition.editable
            ):
                continue

            if hasattr(
                widget,
                key,
            ):
                setattr(
                    widget,
                    key,
                    value,
                )
            else:
                widget.set_property(
                    key,
                    value,
                )

        return widget

    def update_property(
        self,
        widget,
        name: str,
        value: Any,
    ):
        return self.update_widget(
            widget,
            {
                name: value,
            },
        )

    def schemas(self):
        return list(
            self._schemas.values()
        )


ui_property_inspector = (
    UIPropertyInspector()
)
