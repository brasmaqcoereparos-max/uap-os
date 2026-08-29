"""
Classe base para dispositivos simulados do UAP.
"""

import uuid


class DeviceBase:
    def __init__(
        self,
        name,
        device_id=None,
        category="generic",
        description="",
        icon="",
        metadata=None,
    ):
        self.device_id = (
            str(device_id)
            if device_id is not None
            else str(uuid.uuid4())
        )

        self.id = self.device_id
        self.name = str(name)
        self.category = str(category)
        self.description = str(description)
        self.icon = str(icon)

        self.enabled = True
        self.initialized = False

        self.properties = {}
        self.metadata = dict(
            metadata or {}
        )

    def initialize(self):
        self.initialized = True
        return True

    def shutdown(self):
        self.initialized = False
        return True

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def is_enabled(self):
        return self.enabled

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

    def update(self):
        return None

    def reset(self):
        return None

    def to_dict(self):
        return {
            "id": self.device_id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "icon": self.icon,
            "enabled": self.enabled,
            "initialized": self.initialized,
            "properties": dict(
                self.properties
            ),
            "metadata": dict(
                self.metadata
            ),
        }
