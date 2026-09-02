from dataclasses import dataclass


@dataclass
class UIPaletteCategory:
    id: str
    name: str

    order: int = 0

    icon: str | None = None

    description: str = ""

    enabled: bool = True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "order": self.order,
            "icon": self.icon,
            "description": (
                self.description
            ),
            "enabled": self.enabled,
        }
