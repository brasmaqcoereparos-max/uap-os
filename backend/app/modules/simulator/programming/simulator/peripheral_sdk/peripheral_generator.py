"""
Gerador e registrador de periféricos do UAP.

Centraliza a validação e registro de classes de
periféricos no PeripheralRegistry.
"""

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_registry import (
    peripheral_registry,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_validator import (
    peripheral_validator,
)


class PeripheralGenerator:

    def __init__(
        self,
        registry=None,
        validator=None,
    ):
        self.registry = (
            registry
            or peripheral_registry
        )

        self.validator = (
            validator
            or peripheral_validator
        )

        self.registration_count = 0
        self.last_registered = None

    def register(
        self,
        peripheral_class,
        name=None,
        aliases=None,
        metadata=None,
        replace=True,
    ):
        self.validator.validate_class(
            peripheral_class
        )

        registered = (
            self.registry.register(
                peripheral_class,
                name=name,
                aliases=aliases,
                metadata=metadata,
                replace=replace,
            )
        )

        self.registration_count += 1

        self.last_registered = str(
            name
            or getattr(
                peripheral_class,
                "name",
                peripheral_class.__name__,
            )
        )

        return registered

    def register_many(
        self,
        peripheral_classes,
        replace=True,
    ):
        result = []

        for peripheral_class in (
            peripheral_classes or []
        ):
            result.append(
                self.register(
                    peripheral_class,
                    replace=replace,
                )
            )

        return result

    def unregister(
        self,
        name,
    ):
        return self.registry.unregister(
            name
        )

    def create(
        self,
        peripheral_class,
        *args,
        register=False,
        **kwargs,
    ):
        self.validator.validate_class(
            peripheral_class
        )

        if register:
            self.register(
                peripheral_class
            )

        instance = peripheral_class(
            *args,
            **kwargs,
        )

        self.validator.validate_instance(
            instance
        )

        return instance

    def generate_from_description(
        self,
        peripheral_class,
        description,
        register=True,
    ):
        self.validator.validate_class(
            peripheral_class
        )

        self.validator.validate_description(
            description
        )

        metadata = {}

        serializer = getattr(
            description,
            "to_dict",
            None,
        )

        if callable(serializer):
            metadata = serializer()

        if register:
            self.register(
                peripheral_class,
                metadata=metadata,
            )

        return peripheral_class

    def registered(
        self,
        name,
    ):
        return self.registry.exists(
            name
        )

    def reset_statistics(self):
        self.registration_count = 0
        self.last_registered = None

    def to_dict(self):
        return {
            "registration_count": (
                self.registration_count
            ),
            "last_registered": (
                self.last_registered
            ),
            "registry_count": (
                self.registry.count()
            ),
        }


peripheral_generator = (
    PeripheralGenerator()
        )
