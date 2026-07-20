
class RuntimeInstruction:

    def __init__(

        self,

        opcode,

        operands=None,

    ):

        self.opcode = opcode

        self.operands = operands or []

    def to_dict(self):

        return {

            "opcode": self.opcode,

            "operands": self.operands,

        }
