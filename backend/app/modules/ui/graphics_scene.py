from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.transform import (
    UITransform,
)


@dataclass
class UIGraphicObject:
    id: str
    name: str
    object_type: str

    transform: UITransform = field(
        default_factory=UITransform
    )

    properties: dict[str, Any] = field(
        default_factory=dict
    )

    visible: bool = True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "object_type": (
                self.object_type
            ),
            "transform": (
                self.transform.to_dict()
            ),
            "properties": dict(
                self.properties
            ),
            "visible": self.visible,
        }


class UIGraphicsScene:

    def __init__(
        self,
        scene_id: str,
        name: str,
    ):
        self.id = scene_id
        self.name = name

        self._objects: dict[
            str,
            UIGraphicObject,
        ] = {}

    def add(
        self,
        graphic: UIGraphicObject,
    ):
        if graphic.id in self._objects:
            raise ValueError(
                "Graphic object already "
                f"exists: {graphic.id}"
            )

        self._objects[
            graphic.id
        ] = graphic

        return graphic

    def get(
        self,
        object_id: str,
    ):
        return self._objects.get(
            object_id
        )

    def remove(
        self,
        object_id: str,
    ):
        return self._objects.pop(
            object_id,
            None,
        )

    def list_objects(self):
        return list(
            self._objects.values()
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "objects": [
                graphic.to_dict()
                for graphic
                in self._objects.values()
            ],
      }
