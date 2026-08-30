"""
Container simples de dependências do núcleo UAP.

Mantém:
    services
    bind()
    resolve()
    exists()
    clear()
    container
"""


class Container:

    def __init__(self):
        self.services = {}

    def bind(
        self,
        name,
        instance,
        replace=True,
    ):
        name = str(name)

        if (
            name in self.services
            and not replace
        ):
            return self.services[name]

        self.services[name] = instance

        return instance

    def resolve(
        self,
        name,
        default=None,
    ):
        return self.services.get(
            str(name),
            default,
        )

    def require(
        self,
        name,
    ):
        name = str(name)

        if name not in self.services:
            raise KeyError(
                f"Serviço não encontrado: {name}"
            )

        return self.services[name]

    def exists(
        self,
        name,
    ):
        return (
            str(name)
            in self.services
        )

    def unbind(
        self,
        name,
    ):
        return self.services.pop(
            str(name),
            None,
        )

    def names(self):
        return list(
            self.services.keys()
        )

    def all(self):
        return dict(
            self.services
        )

    def count(self):
        return len(
            self.services
        )

    def clear(self):
        count = len(
            self.services
        )

        self.services.clear()

        return count

    def status(self):
        return {
            "count": self.count(),
            "services": self.names(),
        }


container = Container()
