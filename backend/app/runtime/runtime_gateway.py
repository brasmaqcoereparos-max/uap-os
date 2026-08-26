from app.runtime.runtime_service import runtime_service
from app.runtime.runtime_hardware_bridge import (
    runtime_hardware_bridge,
)


class RuntimeGateway:

    def start(self):
        return runtime_service.start()

    def stop(self):
        return runtime_service.stop()

    def status(self):
        return {
            "runtime": runtime_service.status(),
            "hardware": runtime_hardware_bridge.status(),
        }

    def device(self, command):
        return runtime_service.execute(command)

    def hardware(self, command):
        return runtime_hardware_bridge.execute(command)

    def execute(self, command):

        if not isinstance(command, dict):
            raise TypeError(
                "Comando inválido."
            )

        domain = str(
            command.get("domain", "")
        ).strip().lower()

        if domain == "device":
            return self.device(command)

        if domain in {
            "hardware",
            "gpio",
            "uhal",
        }:
            return self.hardware(command)

        raise ValueError(
            f"Domínio desconhecido: {domain}"
        )


runtime_gateway = RuntimeGateway()
