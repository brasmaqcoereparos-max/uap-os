from app.modules.simulator.programming.simulator.core.module_manager import (
    module_manager,
)

from app.modules.simulator.programming.simulator.core.device_module import (
    DeviceModule,
)


class ModuleLoader:

    loaded = False

    @classmethod
    def load(cls):

        if cls.loaded:

            return

        module_manager.register(

            DeviceModule(),

        )

        cls.loaded = True
