"""
UAP Board Development Kit (BDK).

Infraestrutura para descrição, validação,
registro e criação de placas eletrônicas,
pinos e periféricos utilizados pelo simulador.
"""

from app.modules.simulator.programming.simulator.board_sdk.pin import (
    Pin,
)

from app.modules.simulator.programming.simulator.board_sdk.pin_bank import (
    PinBank,
    pin_bank,
)

from app.modules.simulator.programming.simulator.board_sdk.peripheral import (
    Peripheral,
)

from app.modules.simulator.programming.simulator.board_sdk.peripheral_bank import (
    PeripheralBank,
    peripheral_bank,
)

from app.modules.simulator.programming.simulator.board_sdk.board_description import (
    BoardDescription,
)

from app.modules.simulator.programming.simulator.board_sdk.board_registry import (
    BoardRegistry,
    board_registry,
)

from app.modules.simulator.programming.simulator.board_sdk.board_validator import (
    BoardValidator,
    board_validator,
)

from app.modules.simulator.programming.simulator.board_sdk.board_generator import (
    BoardGenerator,
    board_generator,
)

from app.modules.simulator.programming.simulator.board_sdk.board_template import (
    BoardTemplate,
)


__all__ = [
    "Pin",
    "PinBank",
    "pin_bank",
    "Peripheral",
    "PeripheralBank",
    "peripheral_bank",
    "BoardDescription",
    "BoardRegistry",
    "board_registry",
    "BoardValidator",
    "board_validator",
    "BoardGenerator",
    "board_generator",
    "BoardTemplate",
]
