from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIDialog:
    id: str
    name: str

    title: str = ""
    message: str = ""

    dialog_type: str = "standard"

    visible: bool = False

    dismissible: bool = True

    width: float = 420
    height: float = 240

    data: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def open(
        self,
        data: (
            dict[str, Any] | None
        ) = None,
    ):
        if data:
            self.data.update(data)

        self.visible = True

        return self

    def close(self):
        self.visible = False

        return self

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "message": self.message,
            "dialog_type": (
                self.dialog_type
            ),
            "visible": self.visible,
            "dismissible": (
                self.dismissible
            ),
            "width": self.width,
            "height": self.height,
            "data": dict(self.data),
        }
