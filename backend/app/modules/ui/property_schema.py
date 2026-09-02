from dataclasses import dataclass
from dataclasses import field

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

    def categories(self):
        return sorted(
            {
                definition.category
                for definition
                in self.properties
            }
        )

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
