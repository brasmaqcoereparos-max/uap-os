
class RuntimeRegisters:

    def __init__(self):

        self.registers = {}

    def set(

        self,

        name,

        value,

    ):

        self.registers[name] = value

    def get(

        self,

        name,

        default=None,

    ):

        return self.registers.get(

            name,

            default,

        )

    def clear(self):

        self.registers.clear()

    def all(self):

        return self.registers.copy()


runtime_registers = RuntimeRegisters()
