from app.runtime.runtime_boot import runtime_boot
from app.runtime.runtime_health import runtime_health
from app.runtime.runtime_executor import runtime_executor

from app.modules.devices.device_controller import (
    device_controller,
)

from app.modules.uhal.hardware_controller import (
    hardware_controller,
)


class RuntimeRouter:

    def route(self, command):

        if not isinstance(command, dict):
            raise TypeError(
                "Comando inválido."
            )

        domain = str(
            command.get("domain", "")
        ).strip().lower()

        if domain == "device":
            return device_controller.execute(
                command
            )

        if domain in {
            "hardware",
            "gpio",
            "uhal",
        }:
            return hardware_controller.execute(
                command
            )

        if domain == "runtime":
            return self._runtime(command)

        raise ValueError(
            f"Domínio desconhecido: {domain}"
        )

    def _runtime(self, command):

        action = str(
            command.get("action", "")
        ).strip().lower()

        if action == "runtime.start":
            return runtime_boot.start()

        if action == "runtime.stop":
            return runtime_boot.stop()

        if action == "runtime.health":
            return runtime_health.check()

        if action == "runtime.diagnostics":
            return runtime_health.diagnostics()

        if action == "runtime.execute":
            return runtime_executor.execute(
                command.get("command")
            )

        raise ValueError(
            f"Ação de runtime desconhecida: {action}"
        )


runtime_router = RuntimeRouter()
