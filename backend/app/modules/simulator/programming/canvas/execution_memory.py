class ExecutionMemory:

    def __init__(self):

        self.memory = {}

    def write(
        self,
        address,
        value,
    ):

        self.memory[address] = value

    def read(
        self,
        address,
        default=0,
    ):

        return self.memory.get(
            address,
            default,
        )

    def reset(self):

        self.memory.clear()

    def dump(self):

        return self.memory.copy()


execution_memory = ExecutionMemory()
