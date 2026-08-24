"""
Bloco DIGITAL_READ do simulador UAP.
"""

from app.modules.simulator.programming.blocks.base_block import (
    BaseBlock,
)


class DigitalReadBlock(BaseBlock):

    def __init__(
        self,
        block_id,
        pin,
    ):

        super().__init__(
            block_id,
            "Digital Read",
        )

        self.pin = int(
            pin
        )

    def execute(
        self,
        context,
    ):

        key = f"D{self.pin}"

        context["value"] = context.get(
            key,
            0,
        )

        context[
            f"D{self.pin}_READ"
        ] = context[
            "value"
        ]

        return context
