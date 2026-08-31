from dataclasses import dataclass


@dataclass
class UIIndicator:
    id: str
    name: str

    active: bool = False

    label: str = ""

    active_text: str = "ON"
    inactive_text: str = "OFF"

    severity: str = "normal"

    def set_active(
        self,
        active: bool,
    ):
        self.active = bool(active)

        return self.active

    def toggle(self):
        self.active = not self.active

        return self.active

    def text(self):
        if self.active:
            return self.active_text

        return self.inactive_text

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "active": self.active,
            "label": self.label,
            "text": self.text(),
            "severity": self.severity,
        }
