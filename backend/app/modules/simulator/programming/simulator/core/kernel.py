from app.modules.simulator.programming.simulator.plugins.plugin_loader import (
    PluginLoader,
)

from app.modules.simulator.programming.simulator.core.module_loader import (
    ModuleLoader,
)

from app.modules.simulator.programming.simulator.core.module_manager import (
    module_manager,
)


class Kernel:

    initialized = False

    @classmethod
    def boot(cls):

        if cls.initialized:

            return

        PluginLoader.load()

        ModuleLoader.load()

        module_manager.boot()

        cls.initialized = True
