class RuntimeInstructionSet:

    def __init__(self):

        self.instructions = {}

    def register(

        self,

        opcode,

        callback,

    ):

        self.instructions[opcode] = callback

    def get(

        self,

        opcode,

    ):

        return self.instructions.get(opcode)

    def exists(

        self,

        opcode,

    ):

        return opcode in self.instructions

    def clear(self):

        self.instructions.clear()


runtime_instruction_set = RuntimeInstructionSet()
