"""
Componente visual universal do simulador UAP.

Representa um componente colocado no circuito visual,
mantendo posição, rotação, propriedades, metadados,
portas e vínculo opcional com um dispositivo simulado.
"""

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

        self.rotation = (
            float(rotation) % 360
        )

        self.enabled = True
        self.selected = False

        self.properties = {}

        self.metadata = dict(
            metadata or {}
        )

        self.ports = {}

        self.device = None

        self.width = float(
            self.metadata.get(
                "width",
                80,
            )
        )

        self.height = float(
            self.metadata.get(
                "height",
                60,
            )
        )

        self.z_index = int(
            self.metadata.get(
                "z_index",
                0,
            )
        )

        self.locked = bool(
            self.metadata.get(
                "locked",
                False,
            )
        )

    @property
    def component_id(self):
        return self.id

    @property
    def type(self):
        return self.component_type

    def move_to(
        self,
        x,
        y,
    ):
        if self.locked:
            return self

        self.x = float(x)
        self.y = float(y)

        return self

    def move_by(
        self,
        dx,
        dy,
    ):
        if self.locked:
            return self

        self.x += float(dx)
        self.y += float(dy)

        return self

    def position(self):
        return (
            self.x,
            self.y,
        )

    def set_position(
        self,
        x,
        y,
    ):
        return self.move_to(
            x,
            y,
        )

    def rotate(
        self,
        angle,
    ):
        if self.locked:
            return self.rotation

        self.rotation = (
            self.rotation
            + float(angle)
        ) % 360

        return self.rotation

    def set_rotation(
        self,
        angle,
    ):
        if self.locked:
            return self.rotation

        self.rotation = (
            float(angle) % 360
        )

        return self.rotation

    def set_size(
        self,
        width,
        height,
    ):
        width = float(width)
        height = float(height)

        if (
            width <= 0
            or height <= 0
        ):
            raise ValueError(
                "As dimensões do componente "
                "devem ser maiores que zero."
            )

        self.width = width
        self.height = height

        return (
            self.width,
            self.height,
        )

    def bounds(self):
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "right": (
                self.x + self.width
            ),
            "bottom": (
                self.y + self.height
            ),
        }

    def contains_point(
        self,
        x,
        y,
    ):
        x = float(x)
        y = float(y)

        return (
            self.x
            <= x
            <= self.x + self.width
            and
            self.y
            <= y
            <= self.y + self.height
        )

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

    def remove_property(
        self,
        name,
    ):
        return self.properties.pop(
            str(name),
            None,
        )

    def update_properties(
        self,
        values,
    ):
        if values is None:
            return self.properties

        if not isinstance(
            values,
            dict,
        ):
            raise TypeError(
                "values deve ser um dicionário."
            )

        self.properties.update(
            values
        )

        return self.properties

    def set_metadata(
        self,
        name,
        value,
    ):
        self.metadata[
            str(name)
        ] = value

        return value

    def get_metadata(
        self,
        name,
        default=None,
    ):
        return self.metadata.get(
            str(name),
            default,
        )

    def add_port(
        self,
        name,
        port_type="generic",
        direction="bidirectional",
        metadata=None,
    ):
        name = str(name)

        if not name:
            raise ValueError(
                "Nome da porta é obrigatório."
            )

        port = {
            "name": name,
            "type": str(
                port_type
            ),
            "direction": str(
                direction
            ),
            "metadata": dict(
                metadata or {}
            ),
        }

        self.ports[name] = port

        return port

    def remove_port(
        self,
        name,
    ):
        return self.ports.pop(
            str(name),
            None,
        )

    def get_port(
        self,
        name,
    ):
        return self.ports.get(
            str(name)
        )

    def has_port(
        self,
        name,
    ):
        return (
            str(name)
            in self.ports
        )

    def all_ports(self):
        return {
            name: dict(port)
            for name, port
            in self.ports.items()
        }

    def bind_device(
        self,
        device,
    ):
        self.device = device

        return device

    def unbind_device(self):
        device = self.device
        self.device = None

        return device

    def has_device(self):
        return (
            self.device
            is not None
        )

    def update_device(self):
        if self.device is None:
            return None

        updater = getattr(
            self.device,
            "update",
            None,
        )

        if callable(updater):
            return updater()

        return None

    def select(self):
        self.selected = True
        return self

    def deselect(self):
        self.selected = False
        return self

    def enable(self):
        self.enabled = True

        if self.device is not None:
            method = getattr(
                self.device,
                "enable",
                None,
            )

            if callable(method):
                method()

        return self

    def disable(self):
        self.enabled = False

        if self.device is not None:
            method = getattr(
                self.device,
                "disable",
                None,
            )

            if callable(method):
                method()

        return self

    def lock(self):
        self.locked = True
        return self

    def unlock(self):
        self.locked = False
        return self

    def set_z_index(
        self,
        value,
    ):
        self.z_index = int(
            value
        )

        return self.z_index

    def to_dict(self):
        device_data = None

        if self.device is not None:
            serializer = getattr(
                self.device,
                "to_dict",
                None,
            )

            if callable(serializer):
                device_data = (
                    serializer()
                )
            else:
                device_data = {
                    "name": getattr(
                        self.device,
                        "name",
                        str(
                            self.device
                        ),
                    )
                }

        return {
            "id": self.id,
            "name": self.name,
            "type": (
                self.component_type
            ),
            "x": self.x,
            "y": self.y,
            "rotation": (
                self.rotation
            ),
            "width": self.width,
            "height": self.height,
            "z_index": (
                self.z_index
            ),
            "enabled": (
                self.enabled
            ),
            "selected": (
                self.selected
            ),
            "locked": self.locked,
            "properties": dict(
                self.properties
            ),
            "metadata": dict(
                self.metadata
            ),
            "ports": (
                self.all_ports()
            ),
            "device": (
                device_data
            ),
    }
