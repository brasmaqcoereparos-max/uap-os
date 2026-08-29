"""
Catálogo central de classes de dispositivos UAP.
"""

from typing import Dict, Type

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class DeviceCatalog:
    def __init__(self):
        self._devices: Dict[
            str,
            Type[DeviceBase],
        ] = {}

        self._metadata = {}

    @staticmethod
    def _key(name):
        return str(name).strip().upper()

    def register(
        self,
        name,
        device_class,
        category="generic",
        description="",
        icon="",
        metadata=None,
        replace=True,
    ):
        if not name:
            raise ValueError(
                "Nome do dispositivo "
                "é obrigatório."
            )

        if not callable(device_class):
            raise TypeError(
                "device_class precisa "
                "ser executável."
            )

        key = self._key(name)

        if (
            key in self._devices
            and not replace
        ):
            raise ValueError(
                "Dispositivo já "
                f"registrado: {key}"
            )

        self._devices[
            key
        ] = device_class

        self._metadata[
            key
        ] = {
            "name": key,
            "category": str(category),
            "description": str(
                description
            ),
            "icon": str(icon),
            "metadata": dict(
                metadata or {}
            ),
        }

        return device_class

    def unregister(self, name):
        key = self._key(name)

        self._metadata.pop(
            key,
            None,
        )

        return self._devices.pop(
            key,
            None,
        )

    def get(self, name):
        if not name:
            return None

        return self._devices.get(
            self._key(name)
        )

    def info(self, name):
        if not name:
            return None

        data = self._metadata.get(
            self._key(name)
        )

        return (
            dict(data)
            if data is not None
            else None
        )

    def exists(self, name):
        return self.get(name) is not None

    def all(self):
        return self._devices.copy()

    def metadata(self):
        return {
            key: dict(value)
            for key, value
            in self._metadata.items()
        }

    def names(self):
        return list(
            self._devices.keys()
        )

    def categories(self):
        return sorted({
            item["category"]
            for item
            in self._metadata.values()
        })

    def by_category(
        self,
        category,
    ):
        category = str(
            category
        ).strip().lower()

        return {
            name: self._devices[name]
            for name, data
            in self._metadata.items()
            if data[
                "category"
            ].lower() == category
        }

    def search(self, text):
        query = str(
            text or ""
        ).strip().lower()

        if not query:
            return self.names()

        result = []

        for name, data in (
            self._metadata.items()
        ):
            searchable = " ".join([
                name,
                data["category"],
                data["description"],
            ]).lower()

            if query in searchable:
                result.append(name)

        return result

    def count(self):
        return len(self._devices)

    def clear(self):
        self._devices.clear()
        self._metadata.clear()


device_catalog = DeviceCatalog()
