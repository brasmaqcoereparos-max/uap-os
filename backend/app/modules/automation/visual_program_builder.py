from app.modules.automation.visual_block import (
    VisualBlock,
)

from app.modules.automation.block_sequence import (
    BlockSequence,
)

from app.modules.automation.visual_program import (
    VisualProgram,
)

from app.modules.automation.user_level import (
    user_level,
)


class VisualProgramBuilder:

    def create(
        self,
        name="Visual Program",
        level=None,
    ):
        selected_level = (
            user_level.normalize(level)
            if level is not None
            else user_level.get()
        )

        program = VisualProgram(
            name=name,
            user_level=selected_level,
        )

        program.set_sequence(
            BlockSequence()
        )

        return program

    def add_block(
        self,
        program,
        block_type,
        name=None,
        parameters=None,
        position=None,
        icon=None,
        color=None,
    ):
        block = VisualBlock(
            block_type,
            name,
        )

        for key, value in (
            parameters or {}
        ).items():
            block.set_parameter(
                key,
                value,
            )

        if isinstance(
            position,
            dict,
        ):
            block.set_position(
                position.get("x", 0),
                position.get("y", 0),
            )

        if icon is not None:
            block.set_icon(icon)

        if color is not None:
            block.set_color(color)

        if program.sequence is None:
            program.set_sequence(
                BlockSequence()
            )

        program.sequence.add(
            block
        )

        program.graph.add_block(
            block.block_id,
            block,
        )

        return block

    def insert_block(
        self,
        program,
        index,
        block_type,
        name=None,
        parameters=None,
    ):
        block = VisualBlock(
            block_type,
            name,
        )

        for key, value in (
            parameters or {}
        ).items():
            block.set_parameter(
                key,
                value,
            )

        if program.sequence is None:
            program.set_sequence(
                BlockSequence()
            )

        program.sequence.insert(
            index,
            block,
        )

        program.graph.add_block(
            block.block_id,
            block,
        )

        return block

    def remove_block(
        self,
        program,
        block_id,
    ):
        block_id = str(block_id)

        block = program.graph.get_block(
            block_id
        )

        if block is None:
            return False

        if program.sequence is not None:
            blocks = (
                program.sequence.blocks
            )

            program.sequence.blocks = [
                item
                for item in blocks
                if getattr(
                    item,
                    "block_id",
                    None,
                ) != block_id
            ]

        return program.graph.remove_block(
            block_id
        )

    def connect(
        self,
        program,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        return program.graph.connect(
            source=source,
            target=target,
            source_port=source_port,
            target_port=target_port,
        )

    def disconnect(
        self,
        program,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        return program.graph.disconnect(
            source=source,
            target=target,
            source_port=source_port,
            target_port=target_port,
        )

    def configure_block(
        self,
        block,
        parameters=None,
        position=None,
        icon=None,
        color=None,
    ):
        for key, value in (
            parameters or {}
        ).items():
            block.set_parameter(
                key,
                value,
            )

        if isinstance(
            position,
            dict,
        ):
            block.set_position(
                position.get("x", 0),
                position.get("y", 0),
            )

        if icon is not None:
            block.set_icon(icon)

        if color is not None:
            block.set_color(color)

        return block


visual_program_builder = (
    VisualProgramBuilder()
        )
