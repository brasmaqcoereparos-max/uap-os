"""
UAP Peripheral Development Kit (PDK).

Infraestrutura universal para descrição, registro,
validação, criação e carregamento de periféricos
reutilizáveis pelo simulador UAP.
"""

from app.modules.simulator.programming.simulator.peripheral_sdk.interface import (
    Interface,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.interface_registry import (
    InterfaceRegistry,
    interface_registry,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_base import (
    PeripheralBase,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_description import (
    PeripheralDescription,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_registry import (
    PeripheralRegistry,
    peripheral_registry,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_factory import (
    PeripheralFactory,
    peripheral_factory,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_loader import (
    PeripheralLoader,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_validator import (
    PeripheralValidator,
    peripheral_validator,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_generator import (
    PeripheralGenerator,
    peripheral_generator,
)


__all__ = [
    "Interface",
    "InterfaceRegistry",
    "interface_registry",
    "PeripheralBase",
    "PeripheralDescription",
    "PeripheralRegistry",
    "peripheral_registry",
    "PeripheralFactory",
    "peripheral_factory",
    "PeripheralLoader",
    "PeripheralValidator",
    "peripheral_validator",
    "PeripheralGenerator",
    "peripheral_generator",
]
