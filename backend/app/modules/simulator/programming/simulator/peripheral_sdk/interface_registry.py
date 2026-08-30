"""
Registry de interfaces do UAP Peripheral SDK.
"""


class InterfaceRegistry:

    def __init__(self):
        self.interfaces = {}
        self.aliases = {}

    def register(
        self,
        interface,
        name=None,
        aliases=None,
        replace=True,
    ):
        if interface is None:
            raise ValueError(
                "Interface não informada."
            )

        key = str(
            name
            or getattr(
                interface,
                "name",
                "",
            )
        ).strip()

        if not key:
            raise ValueError(
                "Interface precisa possuir nome."
            )

        if (
            key in self.interfaces
            and not replace
        ):
            raise ValueError(
                "Interface já registrada: "
                f"{key}"
            )

        self.interfaces[
            key
        ] = interface

        for alias in (
            aliases or []
        ):
            alias = str(
                alias
            ).strip()

            if alias:
                self.aliases[
                    alias
                ] = key

        return interface

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
            self.aliases.items()
        ):
            if target == key:
                self.aliases.pop(
                    alias,
                    None,
                )

        return self.interfaces.pop(
            key,
            None,
        )

    def resolve(
        self,
        name,
    ):
        name = str(name)

        if name in self.interfaces:
            return name

        if name in self.aliases:
            return self.aliases[
                name
            ]

        lowered = name.lower()

        for key in self.interfaces:
            if (
                key.lower()
                == lowered
            ):
                return key

        for alias, target in (
            self.aliases.items()
        ):
            if (
                alias.lower()
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

        return self.interfaces.get(
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
        return self.interfaces.copy()

    def names(self):
        return list(
            self.interfaces.keys()
        )

    def by_type(
        self,
        interface_type,
    ):
        expected = str(
            interface_type
        ).lower()

        return [
            interface
            for interface
            in self.interfaces.values()
            if str(
                getattr(
                    interface,
                    "type",
                    getattr(
                        interface,
                        "interface_type",
                        "",
                    ),
                )
            ).lower()
            == expected
        ]

    def enabled(self):
        return [
            interface
            for interface
            in self.interfaces.values()
            if getattr(
                interface,
                "enabled",
                True,
            )
        ]

    def clear(self):
        count = len(
            self.interfaces
        )

        self.interfaces.clear()
        self.aliases.clear()

        return count

    def count(self):
        return len(
            self.interfaces
        )

    def to_dict(self):
        result = {}

        for name, interface in (
            self.interfaces.items()
        ):
            serializer = getattr(
                interface,
                "to_dict",
                None,
            )

            if callable(serializer):
                result[name] = (
                    serializer()
                )
            else:
                result[name] = {
                    "name": name,
                    "type": getattr(
                        interface,
                        "type",
                        None,
                    ),
                }

        return {
            "count": self.count(),
            "interfaces": result,
            "aliases": dict(
                self.aliases
            ),
        }


interface_registry = (
    InterfaceRegistry()
    )
