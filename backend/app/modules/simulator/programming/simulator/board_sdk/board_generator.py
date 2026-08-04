from app.modules.simulator.programming.simulator.board_sdk.board_validator import (
    board_validator,
)

from app.modules.simulator.programming.simulator.board_sdk.board_registry import (
    board_registry,
)


class BoardGenerator:

    def register(

        self,

        board_class,

    ):

        board_validator.validate(

            board_class,

        )

        board_registry.register(

            board_class,

        )


board_generator = BoardGenerator()
