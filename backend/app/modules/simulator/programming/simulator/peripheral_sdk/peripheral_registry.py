"""
Registry global dos periféricos UAP.
"""


class PeripheralRegistry:

    def __init__(self):
        self._registry = {}
        self._metadata = {}
        self._aliases = {}

    def register(
        self,
        peripheral_class,
        name=None,
        aliases=None,
        metadata=None,
        replace=True,
    ):
        if not callable(
            peripheral_class
        ):
            raise TypeError(
                "peripheral_class precisa "
                "ser uma classe ou factory."
            )

        key = str(
            name
            or getattr(
                peripheral_class,
                "name",
                peripheral_class.__name__,
            )
        )

        if (
            key in self._registry
            and not replace
        ):
            raise ValueError(
                "Periférico já registrado: "
                f"{key}"
            )

        self._registry[
            key
        ] = peripheral_class

        self._metadata[
            key
        ] = dict(
            metadata or {}
        )

        for alias in (
            aliases or []
        ):
            self._aliases[
                str(alias)
            ] = key

        return peripheral_class

    def unregister(
        self,
        name,
    ):
        key = self.resolve(
            name
        )

        if key is None:
            return None

        for alias, target in list(
            self._aliases.items()
        ):
            if target == key:
                self._aliases.pop(
                    alias,
                    None,
                )

        self._metadata.pop(
            key,
            None,
        )

        return self._registry.pop(
            key,
            None,
        )

    def resolve(
        self,
        name,
    ):
        key = str(name)

        if key in self._registry:
            return key

        alias = self._aliases.get(
            key
        )

        if alias is not None:
            return alias

        lowered = key.lower()

        for candidate in (
            self._registry
        ):
            if (
                candidate.lower()
                == lowered
            ):
                return candidate

        for alias_name, target in (
            self._aliases.items()
        ):
            if (
                alias_name.lower()
                == lowered
            ):
                return target

        return None

    def get(
        self,
        name,
    ):
        key = self.resolve(
            name
        )

        if key is None:
            return None

        return self._registry.get(
            key
        )

    def exists(
        self,
        name,
    ):
        return (
            self.resolve(name)
            is not None
        )

    def all(self):
        return self._registry.copy()

    def names(self):
        return list(
            self._registry.keys()
        )

    def info(
        self,
        name,
    ):
        key = self.resolve(
            name
        )

        if key is None:
            return None

        return dict(
            self._metadata.get(
                key,
                {},
            )
        )

    def clear(self):
        self._registry.clear()
        self._metadata.clear()
        self._aliases.clear()

    def count(self):
        return len(
            self._registry
        )

    def to_dict(self):
        return {
            "count": self.count(),
            "peripherals": {
                name: dict(
                    self._metadata.get(
                        name,
                        {},
                    )
                )
                for name
                in self._registry
            },
            "aliases": dict(
                self._aliases
            ),
        }


peripheral_registry = (
    PeripheralRegistry()
        )
