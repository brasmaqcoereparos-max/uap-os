
from app.runtime.driver_manager import driver_manager
from app.runtime.device_manager import device_manager
from app.runtime.plugin_manager import plugin_manager
from app.runtime.flow_manager import flow_manager
from app.runtime.automation_manager import automation_manager
from app.runtime.logger import runtime_logger


class RuntimeLoader:

    def load(self):
        runtime_logger.info("Loading Runtime objects...")

        self.load_drivers()
        self.load_devices()
        self.load_plugins()
        self.load_flows()
        self.load_automations()

        runtime_logger.info("Runtime objects loaded.")

    def load_drivers(self):
        runtime_logger.info(
            f"Drivers: {len(driver_manager.drivers)}"
        )

    def load_devices(self):
        runtime_logger.info(
            f"Devices: {len(device_manager.devices)}"
        )

    def load_plugins(self):
        runtime_logger.info(
            f"Plugins: {len(plugin_manager.plugins)}"
        )

    def load_flows(self):
        runtime_logger.info(
            f"Flows: {len(flow_manager.flows)}"
        )

    def load_automations(self):
        runtime_logger.info(
            f"Automations: {len(automation_manager.automations)}"
        )


runtime_loader = RuntimeLoader()
