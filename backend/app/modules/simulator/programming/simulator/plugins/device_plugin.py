from app.modules.simulator.programming.simulator.plugins.plugin_base import (
    PluginBase,
)


class DevicePlugin(PluginBase):

    name = "Devices"

    version = "1.0"

    def initialize(self):

        print(

            "Device Plugin Loaded"

        )
