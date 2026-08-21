"""
Universal Device Engine (UDE).

Núcleo universal para gerenciamento,
simulação e integração de dispositivos.
"""

from .device import Device
from .device_factory import (
    DeviceFactory,
    device_factory,
)
from .device_registry import (
    DeviceRegistry,
    device_registry,
)
from .device_status import (
    DeviceStatus,
    DeviceStatusInfo,
)
from .device_manager import (
    DeviceManager,
)
from .device_events import (
    DeviceEvent,
    DeviceEventManager,
    device_events,
)
from .profile import (
    DeviceProfile,
)
from .capabilities import (
    DeviceCapabilities,
)
from .connection import (
    DeviceConnection,
)
from .diagnostics import (
    DiagnosticResult,
    DeviceDiagnostics,
)
from .health import (
    DeviceHealth,
)
from .discovery import (
    DiscoveryResult,
    DeviceDiscovery,
)
from .simulator import (
    SimulatedDevice,
    DeviceSimulator,
    simulator,
)
from .virtual_device import (
    VirtualDevice,
)


__all__ = [
    "Device",
    "DeviceFactory",
    "device_factory",
    "DeviceRegistry",
    "device_registry",
    "DeviceStatus",
    "DeviceStatusInfo",
    "DeviceManager",
    "DeviceEvent",
    "DeviceEventManager",
    "device_events",
    "DeviceProfile",
    "DeviceCapabilities",
    "DeviceConnection",
    "DiagnosticResult",
    "DeviceDiagnostics",
    "DeviceHealth",
    "DiscoveryResult",
    "DeviceDiscovery",
    "SimulatedDevice",
    "DeviceSimulator",
    "simulator",
    "VirtualDevice",
]
