"""
Gerador e registrador de placas do UAP Board SDK.
"""

from app.modules.simulator.programming.simulator.board_sdk.board_validator import (
    board_validator,
)

from app.modules.simulator.programming.simulator.board_sdk.board_registry import (
    board_registry,
)


class BoardGenerator:

    def __init__(
        self,
        registry=None,
        validator=None,
    ):
        self.registry = (
            registry
            or board_registry
        )

        self.validator = (
            validator
            or board_validator
        )

        self.registration_count = 0
        self.creation_count = 0
        self.last_registered = None

    def register(
        self,
        board_class,
        name=None,
        aliases=None,
        metadata=None,
        replace=True,
    ):
        self.validator.validate_class(
            board_class
        )

        result = (
            self.registry.register(
                board_class,
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
                board_class,
                "name",
                board_class.__name__,
            )
        )

        return result

    def register_many(
        self,
        board_classes,
        replace=True,
    ):
        return [
            self.register(
                board_class,
                replace=replace,
            )
            for board_class
            in (
                board_classes or []
            )
        ]

    def create(
        self,
        name,
        *args,
        **kwargs,
    ):
        board_class = (
            self.registry.get(
                name
            )
        )

        if board_class is None:
            raise ValueError(
                f"Placa não registrada: {name}"
            )

        instance = board_class(
            *args,
            **kwargs,
        )

        self.validator.validate_instance(
            instance
        )

        self.creation_count += 1

        return instance

    def unregister(
        self,
        name,
    ):
        return (
            self.registry.unregister(
                name
            )
        )

    def exists(
        self,
        name,
    ):
        return self.registry.exists(
            name
        )

    def available(self):
        return self.registry.names()

    def reset_statistics(self):
        self.registration_count = 0
        self.creation_count = 0
        self.last_registered = None

    def to_dict(self):
        return {
            "registration_count": (
                self.registration_count
            ),
            "creation_count": (
                self.creation_count
            ),
            "last_registered": (
                self.last_registered
            ),
            "available": (
                self.available()
            ),
        }


board_generator = BoardGenerator()
