"""
Registry de placas do UAP Board SDK.
"""


class BoardRegistry:

    def __init__(self):
        self.boards = {}
        self.aliases = {}
        self.metadata = {}

    def register(
        self,
        board_class,
        name=None,
        aliases=None,
        metadata=None,
        replace=True,
    ):
        if board_class is None:
            raise ValueError(
                "board_class não informado."
            )

        key = str(
            name
            or getattr(
                board_class,
                "name",
                "",
            )
        ).strip()

        if not key:
            raise ValueError(
                "Placa precisa possuir nome."
            )

        if (
            key in self.boards
            and not replace
        ):
            raise ValueError(
                f"Placa já registrada: {key}"
            )

        self.boards[
            key
        ] = board_class

        self.metadata[
            key
        ] = dict(
            metadata or {}
        )

        for alias in (
            aliases or []
        ):
            self.aliases[
                str(alias)
            ] = key

        return board_class

    def resolve(
        self,
        name,
    ):
        name = str(name)

        if name in self.boards:
            return name

        if name in self.aliases:
            return self.aliases[
                name
            ]

        lowered = name.lower()

        for key in self.boards:
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

        return self.boards.get(
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

        self.metadata.pop(
            key,
            None,
        )

        return self.boards.pop(
            key,
            None,
        )

    def all(self):
        return self.boards.copy()

    def names(self):
        return list(
            self.boards.keys()
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
            self.metadata.get(
                key,
                {},
            )
        )

    def by_manufacturer(
        self,
        manufacturer,
    ):
        expected = str(
            manufacturer
        ).lower()

        return [
            board_class
            for board_class
            in self.boards.values()
            if (
                str(
                    getattr(
                        board_class,
                        "manufacturer",
                        "",
                    )
                ).lower()
                == expected
            )
        ]

    def clear(self):
        count = len(
            self.boards
        )

        self.boards.clear()
        self.aliases.clear()
        self.metadata.clear()

        return count

    def count(self):
        return len(
            self.boards
        )

    def to_dict(self):
        return {
            "count": self.count(),
            "boards": {
                name: {
                    "manufacturer": getattr(
                        board_class,
                        "manufacturer",
                        "",
                    ),
                    "cpu": getattr(
                        board_class,
                        "cpu",
                        "",
                    ),
                    **dict(
                        self.metadata.get(
                            name,
                            {},
                        )
                    ),
                }
                for name, board_class
                in self.boards.items()
            },
            "aliases": dict(
                self.aliases
            ),
        }


board_registry = BoardRegistry()
