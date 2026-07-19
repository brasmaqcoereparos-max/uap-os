class RuntimeContext:

    def __init__(self):

        self.variables = {}

        self.digital = {}

        self.analog = {}

        self.memory = {}

    def reset(self):

        self.variables.clear()

        self.digital.clear()

        self.analog.clear()

        self.memory.clear()


runtime_context = RuntimeContext()
