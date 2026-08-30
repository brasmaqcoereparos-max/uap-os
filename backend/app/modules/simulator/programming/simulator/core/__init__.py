"""
Universal Automation Platform
Simulator Core

Este pacote concentra a infraestrutura fundamental
do simulador:

    Application
        ↓
      Kernel
        ↓
    Module System

Além de:

    EventBus
    Scheduler
    ServiceRegistry
    Container
"""

from app.modules.simulator.programming.simulator.core.application import (
    Application,
)

from app.modules.simulator.programming.simulator.core.container import (
    Container,
    container,
)

from app.modules.simulator.programming.simulator.core.event import (
    Event,
)

from app.modules.simulator.programming.simulator.core.event_bus import (
    EventBus,
    event_bus,
)

from app.modules.simulator.programming.simulator.core.kernel import (
    Kernel,
)

from app.modules.simulator.programming.simulator.core.module import (
    Module,
)

from app.modules.simulator.programming.simulator.core.module_loader import (
    ModuleLoader,
)

from app.modules.simulator.programming.simulator.core.module_manager import (
    ModuleManager,
    module_manager,
)

from app.modules.simulator.programming.simulator.core.device_module import (
    DeviceModule,
)

from app.modules.simulator.programming.simulator.core.scheduler import (
    Scheduler,
    scheduler,
)

from app.modules.simulator.programming.simulator.core.service_registry import (
    ServiceRegistry,
    service_registry,
)

from app.modules.simulator.programming.simulator.core.version import (
    VERSION,
    NAME,
    AUTHOR,
    STATUS,
    VERSION_INFO,
    get_version,
    version_string,
    info,
)


__all__ = [
    "Application",
    "Container",
    "container",
    "Event",
    "EventBus",
    "event_bus",
    "Kernel",
    "Module",
    "ModuleLoader",
    "ModuleManager",
    "module_manager",
    "DeviceModule",
    "Scheduler",
    "scheduler",
    "ServiceRegistry",
    "service_registry",
    "VERSION",
    "NAME",
    "AUTHOR",
    "STATUS",
    "VERSION_INFO",
    "get_version",
    "version_string",
    "info",
]
