from app.runtime.runtime_device_bridge import (
    runtime_device_bridge,
)

from app.modules.uhal.drivers.raspberry_pi.raspberry_pi_gpio_driver import (
    raspberry_pi_gpio_driver,
)


class RaspberryPiRuntime:

    def __init__(self):
        self.running = False

    def start(self):

        raspberry_pi_gpio_driver.initialize()

        self.running = True

        return True

    def stop(self):

        raspberry_pi_gpio_driver.shutdown()

        self.running = False

        return True

    def execute(
        self,
        command,
    ):

        if not self.running:
            self.start()

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando inválido."
            )

        action = command.get(
            "action"
        )

        device_id = command.get(
            "device_id"
        )

        if action == "device.connect":

            result = runtime_device_bridge.connect(
                device_id
            )

        elif action == "device.disconnect":

            result = runtime_device_bridge.disconnect(
                device_id
            )

        elif action == "device.read":

            result = runtime_device_bridge.read(
                device_id
            )

        elif action == "device.write":

            result = runtime_device_bridge.write(
                device_id,
                command.get("data"),
            )

        elif action == "device.status":

            result = runtime_device_bridge.status(
                device_id
            )

        else:

            raise ValueError(
                f"Ação desconhecida: {action}"
            )

        return {
            "success": True,
            "action": action,
            "device_id": device_id,
            "result": result,
        }


raspberry_pi_runtime = (
    RaspberryPiRuntime()
  )
