from app.modules.simulator.programming.simulator.plugins.plugin_manager import (
    plugin_manager,
)

from app.modules.simulator.programming.simulator.plugins.device_plugin import (
    DevicePlugin,
)


class PluginLoader:

    loaded = False

    @classmethod
    def load(cls):

        if cls.loaded:

            return

        plugin_manager.register(

            DevicePlugin(),

        )

        cls.loaded = True
