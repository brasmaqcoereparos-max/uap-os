class DeviceMemory:

    def __init__(self):

        self.memory = {}

    def write(

        self,

        device,

        key,

        value,

    ):

        self.memory.setdefault(

            device,

            {},

        )[key] = value

    def read(

        self,

        device,

        key,

        default=None,

    ):

        return self.memory.get(

            device,

            {},

        ).get(

            key,

            default,

        )

    def clear(self):

        self.memory.clear()

    def dump(self):

        return self.memory.copy()


device_memory = DeviceMemory()
