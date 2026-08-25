"""
Gerenciador de dispositivos do Runtime UAP.
"""

from app.runtime.driver_manager import (
    driver_manager,
)


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

    def count(self):

        return len(
            self.devices
        )

    def clear(self):

        self.devices.clear()

    def _get_driver(self, device):

        driver_id = getattr(
            device,
            "driver_id",
            None,
        )

        if driver_id is not None:

            driver = driver_manager.get(
                driver_id
            )

            if driver is not None:
                return driver

        driver_name = getattr(
            device,
            "driver",
            None,
        )

        if isinstance(
            driver_name,
            str,
        ):

            driver = driver_manager.get(
                driver_name
            )

            if driver is not None:
                return driver

        return None

    def connect(self, device_id):

        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        driver = self._get_driver(
            device
        )

        if driver is not None:

            connect = getattr(
                driver,
                "connect",
                None,
            )

            if callable(connect):

                result = connect(
                    device
                )

                if result is False:
                    return False

        connect = getattr(
            device,
            "connect",
            None,
        )

        if callable(connect):
            return connect()

        return True

    def disconnect(self, device_id):

        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        disconnect = getattr(
            device,
            "disconnect",
            None,
        )

        if callable(disconnect):
            return disconnect()

        return True

    def read(
        self,
        device_id,
    ):

        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        driver = self._get_driver(
            device
        )

        if driver is not None:

            read = getattr(
                driver,
                "read",
                None,
            )

            if callable(read):
                return read(
                    device
                )

        read = getattr(
            device,
            "read",
            None,
        )

        if callable(read):
            return read()

        raise AttributeError(
            f"Dispositivo '{device_id}' não implementa read()."
        )

    def write(
        self,
        device_id,
        data,
    ):

        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        driver = self._get_driver(
            device
        )

        if driver is not None:

            write = getattr(
                driver,
                "write",
                None,
            )

            if callable(write):

                return write(
                    device,
                    data,
                )

        write = getattr(
            device,
            "write",
            None,
        )

        if callable(write):
            return write(
                data
            )

        raise AttributeError(
            f"Dispositivo '{device_id}' não implementa write()."
        )

    def update(
        self,
        device_id,
    ):

        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        update = getattr(
            device,
            "update",
            None,
        )

        if callable(update):
            return update()

        return None

    def execute_command(
        self,
        command,
    ):

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
                "Comando sem device_id."
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
                command.get(
                    "data"
                ),
            )

        elif action == "device.update":

            result = self.update(
                device_id
            )

        elif action == "device.status":

            device = self.get(
                device_id
            )

            status = getattr(
                device,
                "status",
                None,
            )

            result = (
                status()
                if callable(status)
                else status
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
