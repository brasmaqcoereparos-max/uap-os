"""
Biblioteca de componentes visuais do UAP.
"""


class ComponentLibrary:

    def __init__(self):
        self.components = {}
        self.metadata = {}
        self.aliases = {}

    def register(
        self,
        component_class,
        name=None,
        category="generic",
        description="",
        icon="",
        replace=True,
        aliases=None,
        tags=None,
        version="1.0",
    ):
        if not callable(
            component_class
        ):
            raise TypeError(
                "component_class precisa "
                "ser uma classe ou factory."
            )

        key = str(
            name
            or component_class.__name__
        )

        if (
            key in self.components
            and not replace
        ):
            raise ValueError(
                "Componente já registrado: "
                f"{key}"
            )

        self.components[
            key
        ] = component_class

        alias_list = [
            str(alias)
            for alias
            in (
                aliases or []
            )
        ]

        tag_list = [
            str(tag)
            for tag
            in (
                tags or []
            )
        ]

        self.metadata[
            key
        ] = {
            "name": key,
            "category": str(
                category
            ),
            "description": str(
                description
            ),
            "icon": str(icon),
            "aliases": alias_list,
            "tags": tag_list,
            "version": str(
                version
            ),
        }

        for alias in alias_list:
            self.aliases[
                alias
            ] = key

        return component_class

    def unregister(
        self,
        name,
    ):
        key = self.resolve_name(
            name
        )

        if key is None:
            return None

        metadata = self.metadata.pop(
            key,
            None,
        )

        if metadata:
            for alias in metadata.get(
                "aliases",
                [],
            ):
                self.aliases.pop(
                    alias,
                    None,
                )

        return self.components.pop(
            key,
            None,
        )

    def resolve_name(
        self,
        name,
    ):
        key = str(name)

        if key in self.components:
            return key

        alias = self.aliases.get(
            key
        )

        if alias is not None:
            return alias

        lowered = key.lower()

        for registered in (
            self.components
        ):
            if (
                registered.lower()
                == lowered
            ):
                return registered

        for alias_name, target in (
            self.aliases.items()
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
        key = self.resolve_name(
            name
        )

        if key is None:
            return None

        return self.components.get(
            key
        )

    def exists(
        self,
        name,
    ):
        return (
            self.resolve_name(name)
            is not None
        )

    def create(
        self,
        name,
        *args,
        **kwargs,
    ):
        component_class = self.get(
            name
        )

        if component_class is None:
            raise KeyError(
                "Componente não registrado: "
                f"{name}"
            )

        return component_class(
            *args,
            **kwargs,
        )

    def all(self):
        return self.components.copy()

    def names(self):
        return list(
            self.components.keys()
        )

    def categories(self):
        return sorted({
            item["category"]
            for item
            in self.metadata.values()
        })

    def by_category(
        self,
        category,
    ):
        expected = str(
            category
        ).lower()

        return [
            name
            for name, data
            in self.metadata.items()
            if (
                data.get(
                    "category",
                    "",
                ).lower()
                == expected
            )
        ]

    def by_tag(
        self,
        tag,
    ):
        expected = str(
            tag
        ).lower()

        result = []

        for name, data in (
            self.metadata.items()
        ):
            tags = [
                str(item).lower()
                for item
                in data.get(
                    "tags",
                    [],
                )
            ]

            if expected in tags:
                result.append(name)

        return result

    def search(
        self,
        text,
    ):
        query = str(
            text or ""
        ).strip().lower()

        if not query:
            return self.names()

        result = []

        for name, data in (
            self.metadata.items()
        ):
            searchable = " ".join([
                name,
                data.get(
                    "category",
                    "",
                ),
                data.get(
                    "description",
                    "",
                ),
                *data.get(
                    "aliases",
                    [],
                ),
                *data.get(
                    "tags",
                    [],
                ),
            ]).lower()

            if query in searchable:
                result.append(name)

        return result

    def info(
        self,
        name,
    ):
        key = self.resolve_name(
            name
        )

        if key is None:
            return None

        data = self.metadata.get(
            key
        )

        return (
            dict(data)
            if data is not None
            else None
        )

    def count(self):
        return len(
            self.components
        )

    def clear(self):
        self.components.clear()
        self.metadata.clear()
        self.aliases.clear()

    def to_dict(self):
        return {
            "count": self.count(),
            "categories": (
                self.categories()
            ),
            "components": {
                name: dict(data)
                for name, data
                in self.metadata.items()
            },
        }


component_library = (
    ComponentLibrary()
        )
