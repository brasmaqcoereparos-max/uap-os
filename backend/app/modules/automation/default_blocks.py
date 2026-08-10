from app.modules.automation.block import (
    AutomationBlock,
)

from app.modules.automation.block_types import (
    BlockType,
)

from app.modules.automation.block_library import (
    block_library,
)


def register_default_blocks():

    definitions = [

        (
            BlockType.INPUT.value,
            "Entrada",
        ),

        (
            BlockType.OUTPUT.value,
            "Saída",
        ),

        (
            BlockType.SENSOR.value,
            "Sensor",
        ),

        (
            BlockType.MOTOR.value,
            "Motor",
        ),

        (
            BlockType.RELAY.value,
            "Relé",
        ),

        (
            BlockType.VALVE.value,
            "Válvula",
        ),

        (
            BlockType.TIMER.value,
            "Temporizador",
        ),

        (
            BlockType.CONDITION.value,
            "Condição",
        ),

        (
            BlockType.COUNTER.value,
            "Contador",
        ),

        (
            BlockType.VARIABLE.value,
            "Variável",
        ),

        (
            BlockType.STOCK.value,
            "Estoque",
        ),

        (
            BlockType.MEASUREMENT.value,
            "Medição",
        ),

        (
            BlockType.VISION.value,
            "Visão",
        ),

        (
            BlockType.ROBOT.value,
            "Robô",
        ),

        (
            BlockType.MOTION.value,
            "Movimento",
        ),

        (
            BlockType.AI.value,
            "IA",
        ),
    ]

    for block_type, name in definitions:

        block_library.register(
            AutomationBlock(
                block_type,
                name,
            )
        )
