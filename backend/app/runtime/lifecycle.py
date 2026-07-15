from app.runtime.driver_manager import driver_manager
from app.runtime.device_manager import device_manager
from app.runtime.plugin_manager import plugin_manager
from app.runtime.flow_manager import flow_manager
from app.runtime.automation_manager import automation_manager
from app.runtime.logger import runtime_logger


class RuntimeLifecycle:

    def startup(self):
        runtime_logger.info("Initializing Runtime...")

        driver_manager.connect_all()
        device_manager.connect_all()

        plugin_manager.start_all()
        flow_manager.start_all()
        automation_manager.start_all()

        runtime_logger.info("Runtime initialized successfully")

    def shutdown(self):
        runtime_logger.info("Stopping Runtime...")

        automation_manager.stop_all()
        flow_manager.stop_all()
        plugin_manager.stop_all()

        device_manager.disconnect_all()
        driver_manager.disconnect_all()

        runtime_logger.info("Runtime stopped successfully")


runtime_lifecycle = RuntimeLifecycle()
