class RuntimeMemory:

    def __init__(self):

        self.data = {}

    def write(

        self,

        address,

        value,

    ):

        self.data[address] = value

    def read(

        self,

        address,

        default=None,

    ):

        return self.data.get(

            address,

            default,

        )

    def clear(self):

        self.data.clear()


runtime_memory = RuntimeMemory()
