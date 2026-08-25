"""
Gerenciador de dispositivos do Runtime UAP.

Responsável por registrar, localizar, conectar,
desconectar, atualizar e executar comandos nos
dispositivos registrados no Runtime.
"""


class DeviceManager:

    def __init__(self):
        self.devices = {}

    def register(self, device):
        if device is None:
            raise ValueError(
                "Dispositivo não informado."
            )

        device_id = getattr(
            device,
            "id",
            None,
        )

        if device_id is None:
            raise ValueError(
                "Dispositivo sem id."
            )

        self.devices[device_id] = device

        return device

    def unregister(self, device_id):
        return self.devices.pop(
            device_id,
            None,
        )

    def get(self, device_id):
        return self.devices.get(
            device_id
        )

    def list(self):
        return list(
            self.devices.values()
        )

    def connect_all(self):

        results = {}

        for device_id, device in list(
            self.devices.items()
        ):

            connect = getattr(
                device,
                "connect",
                None,
            )

            if callable(connect):

                try:
                    results[device_id] = connect()

                except Exception as exc:
                    results[device_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def disconnect_all(self):

        results = {}

        for device_id, device in list(
            self.devices.items()
        ):

            disconnect = getattr(
                device,
                "disconnect",
                None,
            )

            if callable(disconnect):

                try:
                    results[device_id] = disconnect()

                except Exception as exc:
                    results[device_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def update(self):

        results = {}

        for device_id, device in list(
            self.devices.items()
        ):

            update = getattr(
                device,
                "update",
                None,
            )

            if callable(update):

                try:
                    results[device_id] = update()

                except Exception as exc:
                    results[device_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def execute_command(
        self,
        command,
    ):
        """
        Executa uma operação sobre um dispositivo.

        Formato esperado:

        {
            "action": "device.write",
            "device_id": "device-01",
            "data": {...}
        }

        Operações suportadas:

        device.connect
        device.disconnect
        device.read
        device.write
        device.update
        device.status
        """

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

        if not device_id:
            raise ValueError(
                "Comando de dispositivo sem device_id."
            )

        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        operations = {
            "device.connect": "connect",
            "device.disconnect": "disconnect",
            "device.read": "read",
            "device.write": "write",
            "device.update": "update",
            "device.status": "status",
        }

        method_name = operations.get(
            action
        )

        if method_name is None:
            raise ValueError(
                f"Ação de dispositivo desconhecida: {action}"
            )

        method = getattr(
            device,
            method_name,
            None,
        )

        if not callable(method):
            raise AttributeError(
                f"Dispositivo '{device_id}' "
                f"não implementa '{method_name}'."
            )

        if action == "device.write":

            if "data" not in command:
                raise ValueError(
                    "device.write exige o campo 'data'."
                )

            result = method(
                command["data"]
            )

        else:

            result = method()

        return {
            "success": True,
            "action": action,
            "device_id": device_id,
            "result": result,
        }

    def clear(self):
        self.devices.clear()

    def count(self):
        return len(
            self.devices
        )


device_manager = DeviceManager()
