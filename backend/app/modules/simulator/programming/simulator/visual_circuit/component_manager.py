class ComponentManager:
    def __init__(self):
        self.components = {}

    def add(
        self,
        component,
        replace=True,
    ):
        if component is None:
            raise ValueError(
                "Componente não informado."
            )

        component_id = getattr(
            component,
            "id",
            None,
        )

        if component_id is None:
            raise ValueError(
                "Componente sem ID."
            )

        component_id = str(
            component_id
        )

        if (
            component_id
            in self.components
            and not replace
        ):
            raise ValueError(
                "Componente já existente: "
                f"{component_id}"
            )

        self.components[
            component_id
        ] = component

        return component

    def get(self, component_id):
        return self.components.get(
            str(component_id)
        )

    def exists(self, component_id):
        return (
            str(component_id)
            in self.components
        )

    def remove(self, component_id):
        return self.components.pop(
            str(component_id),
            None,
        )

    def all(self):
        return list(
            self.components.values()
        )

    def ids(self):
        return list(
            self.components.keys()
        )

    def selected(self):
        return [
            component
            for component
            in self.components.values()
            if getattr(
                component,
                "selected",
                False,
            )
        ]

    def move(
        self,
        component_id,
        x,
        y,
    ):
        component = self.get(
            component_id
        )

        if component is None:
            return False

        move = getattr(
            component,
            "move_to",
            None,
        )

        if callable(move):
            move(x, y)
        else:
            component.x = float(x)
            component.y = float(y)

        return True

    def clear_selection(self):
        for component in (
            self.components.values()
        ):
            deselect = getattr(
                component,
                "deselect",
                None,
            )

            if callable(deselect):
                deselect()

    def clear(self):
        count = len(
            self.components
        )

        self.components.clear()

        return count

    def count(self):
        return len(self.components)

    def to_dict(self):
        return {
            component_id: (
                component.to_dict()
                if hasattr(
                    component,
                    "to_dict",
                )
                else str(component)
            )
            for component_id, component
            in self.components.items()
        }


component_manager = (
    ComponentManager()
            )
