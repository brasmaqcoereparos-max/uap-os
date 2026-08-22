"""
Representação intermediária (IR) do UAP.

Existe uma única definição de IRInstruction para evitar
incompatibilidades entre o IR builder e os consumidores.
"""


class IRInstruction:

    def __init__(
        self,
        opcode,
        operands=None,
        metadata=None,
    ):

        if not opcode:
            raise ValueError(
                "Opcode é obrigatório."
            )

        self.opcode = str(
            opcode
        )

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

    @classmethod
    def from_dict(
        cls,
        data,
    ):

        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "A instrução IR deve ser um dicionário."
            )

        return cls(
            opcode=data.get(
                "opcode"
            ),
            operands=data.get(
                "operands",
                [],
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
        )


class CompilerIR:

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
                    IRInstruction.from_dict(
                        instruction
                    )
                )

            else:

                raise TypeError(
                    "Tipo de instrução IR inválido."
                )

    def all(self):

        return [
            instruction.to_dict()
            for instruction in self.instructions
        ]

    def clear(self):

        self.instructions.clear()

    def __len__(self):

        return len(
            self.instructions
        )


compiler_ir = CompilerIR()
