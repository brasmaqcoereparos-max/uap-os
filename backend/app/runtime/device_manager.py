from app.runtime.runtime_device_bridge import (
    runtime_device_bridge,
)


class DeviceManager:

    def connect(self, device_id):
        return runtime_device_bridge.connect(
            device_id
        )

    def disconnect(self, device_id):
        return runtime_device_bridge.disconnect(
            device_id
        )

    def read(self, device_id):
        return runtime_device_bridge.read(
            device_id
        )

    def write(
        self,
        device_id,
        value,
    ):
        return runtime_device_bridge.write(
            device_id,
            value,
        )

    def update(self, device_id):
        return runtime_device_bridge.update(
            device_id
        )

    def status(self, device_id):
        return runtime_device_bridge.status(
            device_id
        )

    def execute(self, command):
        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        device_id = command.get(
            "device_id"
        )

        if not device_id:
            raise ValueError(
                "device_id obrigatório."
            )

        if action == "device.connect":
            result = self.connect(
                device_id
            )

        elif action == "device.disconnect":
            result = self.disconnect(
                device_id
            )

        elif action == "device.read":
            result = self.read(
                device_id
            )

        elif action == "device.write":
            result = self.write(
                device_id,
                command.get("data"),
            )

        elif action == "device.update":
            result = self.update(
                device_id
            )

        elif action == "device.status":
            result = self.status(
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


device_manager = DeviceManager()
