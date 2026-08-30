"""
Registro de serviços do Core do simulador UAP.

Contrato original preservado:

    service_registry.register(name, service)
    service_registry.get(name)
    service_registry.exists(name)
    service_registry.clear()
"""


class ServiceRegistry:

    def __init__(self):
        self._services = {}

        self._metadata = {}

        self.register_count = 0

    def register(
        self,
        name,
        service,
        replace=True,
        metadata=None,
    ):
        name = str(name)

        if (
            name in self._services
            and not replace
        ):
            return self._services[
                name
            ]

        self._services[
            name
        ] = service

        if metadata is not None:
            self._metadata[
                name
            ] = dict(
                metadata
            )

        self.register_count += 1

        return service

    def get(
        self,
        name,
        default=None,
    ):
        return self._services.get(
            str(name),
            default,
        )

    def require(
        self,
        name,
    ):
        name = str(name)

        if name not in self._services:
            raise KeyError(
                f"Serviço não registrado: {name}"
            )

        return self._services[
            name
        ]

    def exists(
        self,
        name,
    ):
        return (
            str(name)
            in self._services
        )

    def unregister(
        self,
        name,
    ):
        name = str(name)

        self._metadata.pop(
            name,
            None,
        )

        return self._services.pop(
            name,
            None,
        )

    def names(self):
        return list(
            self._services.keys()
        )

    def all(self):
        return dict(
            self._services
        )

    def count(self):
        return len(
            self._services
        )

    def metadata(
        self,
        name,
        default=None,
    ):
        return self._metadata.get(
            str(name),
            default,
        )

    def set_metadata(
        self,
        name,
        metadata,
    ):
        name = str(name)

        if name not in self._services:
            return False

        self._metadata[
            name
        ] = dict(
            metadata or {}
        )

        return True

    def clear(self):
        count = len(
            self._services
        )

        self._services.clear()
        self._metadata.clear()

        return count

    def reset(self):
        self.clear()

        self.register_count = 0

        return True

    def status(self):
        return {
            "count": self.count(),
            "services": (
                self.names()
            ),
            "register_count": (
                self.register_count
            ),
        }

    def to_dict(self):
        return {
            **self.status(),
            "metadata": {
                key: dict(value)
                for key, value
                in self._metadata.items()
            },
        }


service_registry = (
    ServiceRegistry()
        )
