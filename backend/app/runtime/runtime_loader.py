from app.runtime.automation_manager import (
    automation_manager,
)
from app.runtime.device_manager import (
    device_manager,
)
from app.runtime.driver_manager import (
    driver_manager,
)
from app.runtime.flow_manager import (
    flow_manager,
)
from app.runtime.logger import (
    runtime_logger,
)
from app.runtime.plugin_manager import (
    plugin_manager,
)


class RuntimeLoader:

    def __init__(self):
        self.loaded = False

    def load(self):

        if self.loaded:
            return

        runtime_logger.info(
            "Loading Runtime objects..."
        )

        self.load_drivers()
        self.load_devices()
        self.load_plugins()
        self.load_flows()
        self.load_automations()

        self.loaded = True

        runtime_logger.info(
            "Runtime objects loaded."
        )

    def load_drivers(self):

        runtime_logger.info(
            f"Drivers: "
            f"{len(driver_manager.drivers)}"
        )

    def load_devices(self):

        runtime_logger.info(
            f"Devices: "
            f"{len(device_manager.devices)}"
        )

    def load_plugins(self):

        runtime_logger.info(
            f"Plugins: "
            f"{len(plugin_manager.plugins)}"
        )

    def load_flows(self):

        runtime_logger.info(
            f"Flows: "
            f"{len(flow_manager.flows)}"
        )

    def load_automations(self):

        runtime_logger.info(
            f"Automations: "
            f"{len(automation_manager.automations)}"
        )

    def reset(self):
        self.loaded = False


runtime_loader = RuntimeLoader()
