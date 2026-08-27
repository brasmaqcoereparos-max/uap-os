class VisualConfig:

    def __init__(
        self,
        label="",
        icon="",
        category="",
        color="",
    ):
        self.label = str(label)
        self.icon = str(icon)
        self.category = str(category)
        self.color = str(color)

        self.position = {
            "x": 0,
            "y": 0,
        }

        self.size = {
            "width": 160,
            "height": 80,
        }

        self.visible = True
        self.locked = False

    def set_position(
        self,
        x,
        y,
    ):
        self.position = {
            "x": float(x),
            "y": float(y),
        }

        return self

    def set_size(
        self,
        width,
        height,
    ):
        self.size = {
            "width": max(
                1,
                float(width),
            ),
            "height": max(
                1,
                float(height),
            ),
        }

        return self

    def set_label(
        self,
        label,
    ):
        self.label = str(label)
        return self

    def set_icon(
        self,
        icon,
    ):
        self.icon = str(icon)
        return self

    def set_category(
        self,
        category,
    ):
        self.category = str(
            category
        )

        return self

    def set_color(
        self,
        color,
    ):
        self.color = str(color)
        return self

    def show(self):
        self.visible = True
        return self

    def hide(self):
        self.visible = False
        return self

    def lock(self):
        self.locked = True
        return self

    def unlock(self):
        self.locked = False
        return self

    def update(
        self,
        data,
    ):
        if not isinstance(
            data,
            dict,
        ):
            return self

        if "label" in data:
            self.set_label(
                data["label"]
            )

        if "icon" in data:
            self.set_icon(
                data["icon"]
            )

        if "category" in data:
            self.set_category(
                data["category"]
            )

        if "color" in data:
            self.set_color(
                data["color"]
            )

        position = data.get(
            "position"
        )

        if isinstance(
            position,
            dict,
        ):
            self.set_position(
                position.get("x", 0),
                position.get("y", 0),
            )

        size = data.get("size")

        if isinstance(
            size,
            dict,
        ):
            self.set_size(
                size.get(
                    "width",
                    160,
                ),
                size.get(
                    "height",
                    80,
                ),
            )

        if "visible" in data:
            self.visible = bool(
                data["visible"]
            )

        if "locked" in data:
            self.locked = bool(
                data["locked"]
            )

        return self

    def to_dict(self):
        return {
            "label": self.label,
            "icon": self.icon,
            "category": self.category,
            "color": self.color,
            "position": dict(
                self.position
            ),
            "size": dict(
                self.size
            ),
            "visible": self.visible,
            "locked": self.locked,
                }
