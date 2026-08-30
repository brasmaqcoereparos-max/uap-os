"""
Factory de periféricos do UAP.
"""

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_registry import (
    peripheral_registry,
)


class PeripheralFactory:

    def __init__(
        self,
        registry=None,
    ):
        self.registry = (
            registry
            or peripheral_registry
        )

        self.created_count = 0

    def create(
        self,
        name,
        *args,
        **kwargs,
    ):
        peripheral = (
            self.registry.get(
                name
            )
        )

        if peripheral is None:
            raise ValueError(
                f"Periférico '{name}' "
                "não encontrado."
            )

        instance = peripheral(
            *args,
            **kwargs,
        )

        self.created_count += 1

        return instance

    def create_initialized(
        self,
        name,
        *args,
        **kwargs,
    ):
        instance = self.create(
            name,
            *args,
            **kwargs,
        )

        initializer = getattr(
            instance,
            "initialize",
            None,
        )

        if callable(initializer):
            initializer()

        return instance

    def create_many(
        self,
        name,
        count,
        *args,
        **kwargs,
    ):
        count = int(count)

        if count < 0:
            raise ValueError(
                "count não pode "
                "ser negativo."
            )

        return [
            self.create(
                name,
                *args,
                **kwargs,
            )
            for _ in range(count)
        ]

    def can_create(
        self,
        name,
    ):
        return (
            self.registry.get(name)
            is not None
        )

    def available(self):
        names = getattr(
            self.registry,
            "names",
            None,
        )

        if callable(names):
            return names()

        return list(
            self.registry.all().keys()
        )

    def count_available(self):
        return len(
            self.available()
        )

    def reset_statistics(self):
        self.created_count = 0

    def to_dict(self):
        return {
            "available": (
                self.available()
            ),
            "available_count": (
                self.count_available()
            ),
            "created_count": (
                self.created_count
            ),
        }


peripheral_factory = (
    PeripheralFactory()
        )
