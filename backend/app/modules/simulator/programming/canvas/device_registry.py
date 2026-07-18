class DeviceRegistry:

    def __init__(self):

        self.registry = {}

    def register(

        self,

        category,

        device,

    ):

        self.registry.setdefault(

            category,

            [],

        ).append(device)

    def categories(self):

        return sorted(

            self.registry.keys()

        )

    def devices(

        self,

        category,

    ):

        return self.registry.get(

            category,

            [],

        )

    def clear(self):

        self.registry.clear()


device_registry = DeviceRegistry()
