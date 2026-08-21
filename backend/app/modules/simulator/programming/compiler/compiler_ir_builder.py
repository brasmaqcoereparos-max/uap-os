"""
Construtor intermediário de IR do compilador UAP.

Converte uma sequência de instruções de alto nível
para uma representação intermediária simples.
"""


class IRInstruction:

    def __init__(
        self,
        opcode,
        operands=None,
        metadata=None,
    ):
        self.opcode = opcode
        self.operands = list(
            operands or []
        )
        self.metadata = dict(
            metadata or {}
        )

    def to_dict(self):
        return {
            "opcode": self.opcode,
            "operands": list(
                self.operands
            ),
            "metadata": dict(
                self.metadata
            ),
        }


class IRBuilder:

    def __init__(self):
        self.instructions = []

    def emit(
        self,
        opcode,
        *operands,
        metadata=None,
    ):
        instruction = IRInstruction(
            opcode=opcode,
            operands=operands,
            metadata=metadata,
        )

        self.instructions.append(
            instruction
        )

        return instruction

    def extend(
        self,
        instructions,
    ):
        for instruction in instructions:
            if isinstance(
                instruction,
                IRInstruction,
            ):
                self.instructions.append(
                    instruction
                )
            elif isinstance(
                instruction,
                dict,
            ):
                self.instructions.append(
                    IRInstruction(
                        opcode=instruction.get(
                            "opcode"
                        ),
                        operands=instruction.get(
                            "operands",
                            [],
                        ),
                        metadata=instruction.get(
                            "metadata",
                            {},
                        ),
                    )
                )

    def clear(self):
        self.instructions.clear()

    def build(self):
        return [
            instruction.to_dict()
            for instruction in self.instructions
        ]

    def __len__(self):
        return len(
            self.instructions
        )
