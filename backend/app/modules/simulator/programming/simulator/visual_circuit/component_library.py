class ComponentLibrary:
    def __init__(self):
        self.components = {}
        self.metadata = {}

    def register(
        self,
        component_class,
        name=None,
        category="generic",
        description="",
        icon="",
        replace=True,
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

        self.metadata[
            key
        ] = {
            "name": key,
            "category": str(category),
            "description": str(
                description
            ),
            "icon": str(icon),
        }

        return component_class

    def unregister(self, name):
        key = str(name)

        self.metadata.pop(
            key,
            None,
        )

        return self.components.pop(
            key,
            None,
        )

    def get(self, name):
        return self.components.get(
            str(name)
        )

    def exists(self, name):
        return (
            str(name)
            in self.components
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

    def search(self, text):
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
                data["category"],
                data["description"],
            ]).lower()

            if query in searchable:
                result.append(name)

        return result

    def info(self, name):
        data = self.metadata.get(
            str(name)
        )

        return (
            dict(data)
            if data is not None
            else None
        )

    def count(self):
        return len(self.components)

    def clear(self):
        self.components.clear()
        self.metadata.clear()


component_library = (
    ComponentLibrary()
)
