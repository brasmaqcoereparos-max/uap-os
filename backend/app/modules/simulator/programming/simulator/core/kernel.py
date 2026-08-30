"""
Kernel central do simulador UAP.

Preserva o pipeline original:

    HALLoader
        ↓
    PluginLoader
        ↓
    ModuleLoader
        ↓
    ModuleManager.boot()
"""

from app.modules.simulator.programming.simulator.plugins.plugin_loader import (
    PluginLoader,
)

from app.modules.simulator.programming.simulator.core.module_loader import (
    ModuleLoader,
)

from app.modules.simulator.programming.simulator.core.module_manager import (
    module_manager,
)

from app.modules.simulator.programming.simulator.hal.hal_loader import (
    HALLoader,
)


class Kernel:

    initialized = False
    boot_count = 0

    last_error = None

    @classmethod
    def boot(cls):
        if cls.initialized:
            return True

        try:
            HALLoader.load()

            PluginLoader.load()

            ModuleLoader.load()

            module_manager.boot()

            cls.initialized = True
            cls.boot_count += 1
            cls.last_error = None

            return True

        except Exception as exc:
            cls.initialized = False
            cls.last_error = str(exc)

            raise

    @classmethod
    def shutdown(cls):
        shutdown = getattr(
            module_manager,
            "shutdown",
            None,
        )

        if callable(shutdown):
            shutdown()

        cls.initialized = False

        return True

    @classmethod
    def reset(cls):
        reset = getattr(
            module_manager,
            "reset",
            None,
        )

        if callable(reset):
            reset()

        cls.initialized = False
        cls.boot_count = 0
        cls.last_error = None

        return True

    @classmethod
    def is_initialized(cls):
        return cls.initialized

    @classmethod
    def status(cls):
        manager_status = getattr(
            module_manager,
            "status",
            None,
        )

        return {
            "initialized": (
                cls.initialized
            ),
            "boot_count": (
                cls.boot_count
            ),
            "last_error": (
                cls.last_error
            ),
            "modules": (
                manager_status()
                if callable(manager_status)
                else None
            ),
        }
