from dataclasses import dataclass


@dataclass
class UIInteractionMode:
    name: str = "select"

    allow_selection: bool = True
    allow_move: bool = True
    allow_resize: bool = True

    allow_pan: bool = True
    allow_zoom: bool = True

    readonly: bool = False

    def can_edit(self):
        return not self.readonly

    def to_dict(self):
        return {
            "name": self.name,
            "allow_selection": (
                self.allow_selection
            ),
            "allow_move": (
                self.allow_move
            ),
            "allow_resize": (
                self.allow_resize
            ),
            "allow_pan": (
                self.allow_pan
            ),
            "allow_zoom": (
                self.allow_zoom
            ),
            "readonly": (
                self.readonly
            ),
        }
