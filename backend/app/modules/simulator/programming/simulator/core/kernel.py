from app.modules.simulator.programming.simulator.plugins.plugin_loader import (
    PluginLoader,
)


class Kernel:

    initialized = False

    @classmethod
    def boot(cls):

        if cls.initialized:
            return

        PluginLoader.load()

        cls.initialized = True
