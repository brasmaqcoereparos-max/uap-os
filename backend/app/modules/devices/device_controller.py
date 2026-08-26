from app.modules.devices.device_service import (
    device_service,
)


class DeviceController:

    def list(self):
        return [
            self._status(device)
            for device in device_service.list()
        ]

    def count(self):
        return {
            "count": device_service.count()
        }

    def connect(self, device_id):
        return device_service.connect(
            device_id
        )

    def disconnect(self, device_id):
        return device_service.disconnect(
            device_id
        )

    def read(self, device_id):
        return device_service.read(
            device_id
        )

    def write(
        self,
        device_id,
        value,
    ):
        return device_service.write(
            device_id,
            value,
        )

    def update(self, device_id):
        return device_service.update(
            device_id
        )

    def status(self, device_id):
        return device_service.status(
            device_id
        )

    def execute(self, command):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando de dispositivo inválido."
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

        if action == "device.list":
            return self.list()

        if action == "device.count":
            return self.count()

        if not device_id:
            raise ValueError(
                "device_id obrigatório."
            )

        if action == "device.connect":
            return self.connect(
                device_id
            )

        if action == "device.disconnect":
            return self.disconnect(
                device_id
            )

        if action == "device.read":
            return self.read(
                device_id
            )

        if action == "device.write":
            return self.write(
                device_id,
                command.get("data"),
            )

        if action == "device.update":
            return self.update(
                device_id
            )

        if action == "device.status":
            return self.status(
                device_id
            )

        raise ValueError(
            f"Ação desconhecida: {action}"
        )

    @staticmethod
    def _status(device):

        method = getattr(
            device,
            "status",
            None,
        )

        if callable(method):
            return method()

        return {
            "id": getattr(
                device,
                "id",
                None,
            )
        }


device_controller = DeviceController()
