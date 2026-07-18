from app.modules.simulator.programming.canvas.device_driver import (
    device_driver,
)
from app.modules.simulator.programming.canvas.device_events import (
    device_events,
)


class DeviceExecutor:

    def execute(
        self,
        device_name,
        command,
        *args,
        **kwargs,
    ):

        driver = device_driver.get(
            device_name
        )

        if driver is None:

            device_events.emit(

                device_name,

                "driver_not_found",

            )

            return None

        result = driver.execute(
            command,
            *args,
            **kwargs,
        )

        device_events.emit(

            device_name,

            "command",

            {

                "command": command,

                "result": result,

            },

        )

        return result


device_executor = DeviceExecutor()
