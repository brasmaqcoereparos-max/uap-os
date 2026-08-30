"""
Hardware Virtual Engine (HVE).

Camada responsável pelo universo lógico de hardware virtual
do simulador UAP.

Estrutura:

    VirtualClock
          ↓
    VirtualWorld
          ↓
    VirtualDevice(s)

O HVE é propositalmente independente do UHAL físico.
"""

from app.modules.simulator.programming.simulator.hve.virtual_clock import (
    VirtualClock,
    virtual_clock,
)

from app.modules.simulator.programming.simulator.hve.virtual_device import (
    VirtualDevice,
)

from app.modules.simulator.programming.simulator.hve.virtual_world import (
    VirtualWorld,
    virtual_world,
)


__all__ = [
    "VirtualClock",
    "virtual_clock",
    "VirtualDevice",
    "VirtualWorld",
    "virtual_world",
]
