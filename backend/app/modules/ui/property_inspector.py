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
            widget.add(definition)

        self.register_schema(widget)

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

        result = {}

        if not schema:
            return result

        for definition in (
            schema.properties
        ):
            result[
                definition.name
            ] = getattr(
                widget,
                definition.name,
                definition.default,
            )

        return {
            "schema": (
                schema.to_dict()
            ),
            "values": result,
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

        for key, value in (
            values.items()
        ):
            definition = (
                schema.get(key)
            )

            if (
                not definition
                or not definition.editable
            ):
                continue

            if (
                definition.minimum
                is not None
                and isinstance(
                    value,
                    (int, float),
                )
            ):
                value = max(
                    definition.minimum,
                    value,
                )

            if (
                definition.maximum
                is not None
                and isinstance(
                    value,
                    (int, float),
                )
            ):
                value = min(
                    definition.maximum,
                    value,
                )

            setattr(
                widget,
                key,
                value,
            )

        return widget


ui_property_inspector = (
    UIPropertyInspector()
      )
