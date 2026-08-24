"""
Bloco ANALOG_READ do simulador UAP.
"""

from app.modules.simulator.programming.blocks.base_block import (
    BaseBlock,
)


class AnalogReadBlock(BaseBlock):

    def __init__(
        self,
        block_id,
        pin,
    ):

        super().__init__(
            block_id,
            "Analog Read",
        )

        self.pin = int(
            pin
        )

    def execute(
        self,
        context,
    ):

        key = f"A{self.pin}"

        context["value"] = context.get(
            key,
            0,
        )

        context[
            f"A{self.pin}_READ"
        ] = context[
            "value"
        ]

        return context
