import uuid


class Component:
    def __init__(
        self,
        component_id=None,
        name="Component",
        component_type="generic",
        x=0,
        y=0,
        rotation=0,
        metadata=None,
    ):
        self.id = (
            str(component_id)
            if component_id is not None
            else str(uuid.uuid4())
        )

        self.name = str(name)
        self.component_type = str(
            component_type
        )

        self.x = float(x)
        self.y = float(y)
        self.rotation = float(rotation)

        self.enabled = True
        self.selected = False

        self.properties = {}
        self.metadata = dict(
            metadata or {}
        )

    def move_to(self, x, y):
        self.x = float(x)
        self.y = float(y)

        return self

    def move_by(self, dx, dy):
        self.x += float(dx)
        self.y += float(dy)

        return self

    def rotate(self, angle):
        self.rotation = (
            self.rotation
            + float(angle)
        ) % 360

        return self.rotation

    def set_rotation(self, angle):
        self.rotation = (
            float(angle) % 360
        )

        return self.rotation

    def set_property(
        self,
        name,
        value,
    ):
        self.properties[
            str(name)
        ] = value

        return value

    def get_property(
        self,
        name,
        default=None,
    ):
        return self.properties.get(
            str(name),
            default,
        )

    def select(self):
        self.selected = True
        return self

    def deselect(self):
        self.selected = False
        return self

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.component_type,
            "x": self.x,
            "y": self.y,
            "rotation": self.rotation,
            "enabled": self.enabled,
            "selected": self.selected,
            "properties": dict(
                self.properties
            ),
            "metadata": dict(
                self.metadata
            ),
        }
