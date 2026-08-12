from app.modules.automation.visual_block import (
    VisualBlock,
)

from app.modules.automation.block_sequence import (
    BlockSequence,
)

from app.modules.automation.visual_program import (
    VisualProgram,
)


class VisualProgramBuilder:

    def create(
        self,
        name="Visual Program",
    ):

        program = VisualProgram(name)

        program.set_sequence(
            BlockSequence()
        )

        return program

    def add_block(
        self,
        program,
        block_type,
        name=None,
    ):

        block = VisualBlock(
            block_type,
            name,
        )

        program.sequence.add(
            block
        )

        return block

    def insert_block(
        self,
        program,
        index,
        block_type,
        name=None,
    ):

        block = VisualBlock(
            block_type,
            name,
        )

        program.sequence.insert(
            index,
            block,
        )

        return block


visual_program_builder = (
    VisualProgramBuilder()
)
