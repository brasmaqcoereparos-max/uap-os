"""
Dispositivos virtuais públicos do simulador UAP.

Esta camada contém dispositivos simples utilizados pela
API pública do simulador.

Ela é independente dos dispositivos avançados existentes em:

    simulator/programming/simulator/device/

As duas camadas possuem responsabilidades diferentes e não
devem ser fundidas sem uma etapa explícita de integração.
"""

from app.modules.simulator.devices.virtual_device import (
    VirtualDevice,
)

from app.modules.simulator.devices.virtual_led import (
    VirtualLED,
)

from app.modules.simulator.devices.virtual_button import (
    VirtualButton,
)

from app.modules.simulator.devices.virtual_relay import (
    VirtualRelay,
)


__all__ = [
    "VirtualDevice",
    "VirtualLED",
    "VirtualButton",
    "VirtualRelay",
]
