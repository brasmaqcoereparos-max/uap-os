from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.property_definition import (
    UIPropertyDefinition,
)


@dataclass
class UIPropertySchema:
    target_type: str

    properties: list[
        UIPropertyDefinition
    ] = field(
        default_factory=list
    )

    def add(
        self,
        definition: UIPropertyDefinition,
    ):
        existing = self.get(
            definition.name
        )

        if existing:
            self.properties.remove(
                existing
            )

        self.properties.append(
            definition
        )

        return definition

    def get(
        self,
        name: str,
    ):
        for definition in (
            self.properties
        ):
            if (
                definition.name
                == name
            ):
                return definition

        return None

    def remove(
        self,
        name: str,
    ) -> bool:
        definition = self.get(
            name
        )

        if definition is None:
            return False

        self.properties.remove(
            definition
        )

        return True

    def categories(self):
        return sorted(
            {
                definition.category
                for definition
                in self.properties
            }
        )

    def validate(
        self,
        values: dict[str, Any],
        *,
        partial: bool = False,
    ) -> dict[str, Any]:
        result: dict[str, Any] = {}

        for definition in (
            self.properties
        ):
            if (
                definition.name
                not in values
            ):
                if (
                    definition.required
                    and not partial
                ):
                    if (
                        definition.default
                        is None
                    ):
                        raise ValueError(
                            "Missing required "
                            "property: "
                            f"{definition.name}"
                        )

                    result[
                        definition.name
                    ] = definition.coerce(
                        definition.default
                    )

                continue

            result[
                definition.name
            ] = definition.coerce(
                values[
                    definition.name
                ]
            )

        return result

    def defaults(self):
        return {
            definition.name: (
                definition.default
            )
            for definition
            in self.properties
            if definition.default
            is not None
        }

    def to_dict(self):
        return {
            "target_type": (
                self.target_type
            ),
            "properties": [
                definition.to_dict()
                for definition
                in self.properties
            ],
        }
