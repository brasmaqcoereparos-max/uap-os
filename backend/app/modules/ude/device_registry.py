class DeviceRegistry:

    def __init__(self):

        self.registry = {}

    def register(

        self,

        device_type,

        device_class,

    ):

        self.registry[device_type] = device_class

    def create(

        self,

        device_type,

        *args,

        **kwargs,

    ):

        cls = self.registry.get(device_type)

        if cls:

            return cls(

                *args,

                **kwargs,

            )

        return None


device_registry = DeviceRegistry()"""
Universal Device Engine
"""
