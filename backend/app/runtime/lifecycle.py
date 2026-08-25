from app.runtime.driver_manager import (
    driver_manager,
)

from app.runtime.device_manager import (
    device_manager,
)

from app.runtime.plugin_manager import (
    plugin_manager,
)

from app.runtime.flow_manager import (
    flow_manager,
)

from app.runtime.automation_manager import (
    automation_manager,
)

from app.runtime.runtime_loader import (
    runtime_loader,
)

from app.runtime.command_processor import (
    command_processor,
)

from app.runtime.logger import (
    runtime_logger,
)


class RuntimeLifecycle:

    def __init__(self):

        self.commands_registered = False

    def _register_device_commands(self):

        commands = (
            "device.connect",
            "device.disconnect",
            "device.read",
            "device.write",
            "device.update",
            "device.status",
        )

        for action in commands:

            command_processor.register(
                action,
                device_manager.execute_command,
            )

        self.commands_registered = True

    def startup(self):

        runtime_logger.info(
            "Initializing Runtime..."
        )

        runtime_loader.load()

        self._register_device_commands()

        driver_manager.connect_all()

        device_manager.connect_all()

        plugin_manager.start_all()

        flow_manager.start_all()

        automation_manager.start_all()

        runtime_logger.info(
            "Runtime initialized successfully"
        )

        return True

    def shutdown(self):

        runtime_logger.info(
            "Stopping Runtime..."
        )

        automation_manager.stop_all()

        flow_manager.stop_all()

        plugin_manager.stop_all()

        device_manager.disconnect_all()

        driver_manager.disconnect_all()

        runtime_logger.info(
            "Runtime stopped successfully"
        )

        return True


runtime_lifecycle = RuntimeLifecycle()
