"""
Universal Device Engine
Registro central de classes de dispositivos.
"""


class DeviceRegistry:

    def __init__(self):
        self.registry = {}

    def register(
        self,
        device_type,
        device_class,
    ):
        self.registry[device_type] = device_class

    def unregister(
        self,
        device_type,
    ):
        return self.registry.pop(
            device_type,
            None,
        )

    def get(
        self,
        device_type,
    ):
        return self.registry.get(
            device_type
        )

    def create(
        self,
        device_type,
        *args,
        **kwargs,
    ):
        device_class = self.registry.get(
            device_type
        )

        if device_class is None:
            return None

        return device_class(
            *args,
            **kwargs,
        )

    def list_types(self):
        return list(
            self.registry.keys()
        )


device_registry = DeviceRegistry()
