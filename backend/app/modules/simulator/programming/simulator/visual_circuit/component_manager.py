"""
Gerenciador dos componentes do circuito visual UAP.
"""


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

    def get(
        self,
        component_id,
    ):
        return self.components.get(
            str(component_id)
        )

    def exists(
        self,
        component_id,
    ):
        return (
            str(component_id)
            in self.components
        )

    def remove(
        self,
        component_id,
    ):
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

    def find_by_name(
        self,
        name,
    ):
        expected = str(
            name
        ).lower()

        return [
            component
            for component
            in self.components.values()
            if str(
                getattr(
                    component,
                    "name",
                    "",
                )
            ).lower()
            == expected
        ]

    def find_by_type(
        self,
        component_type,
    ):
        expected = str(
            component_type
        ).lower()

        return [
            component
            for component
            in self.components.values()
            if str(
                getattr(
                    component,
                    "component_type",
                    "",
                )
            ).lower()
            == expected
        ]

    def enabled(self):
        return [
            component
            for component
            in self.components.values()
            if getattr(
                component,
                "enabled",
                True,
            )
        ]

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

    def select(
        self,
        component_id,
        exclusive=False,
    ):
        component = self.get(
            component_id
        )

        if component is None:
            return False

        if exclusive:
            self.clear_selection()

        selector = getattr(
            component,
            "select",
            None,
        )

        if callable(selector):
            selector()
        else:
            component.selected = True

        return True

    def deselect(
        self,
        component_id,
    ):
        component = self.get(
            component_id
        )

        if component is None:
            return False

        deselector = getattr(
            component,
            "deselect",
            None,
        )

        if callable(deselector):
            deselector()
        else:
            component.selected = False

        return True

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
            move(
                x,
                y,
            )
        else:
            component.x = float(x)
            component.y = float(y)

        return True

    def move_by(
        self,
        component_id,
        dx,
        dy,
    ):
        component = self.get(
            component_id
        )

        if component is None:
            return False

        move = getattr(
            component,
            "move_by",
            None,
        )

        if callable(move):
            move(
                dx,
                dy,
            )
        else:
            component.x += float(dx)
            component.y += float(dy)

        return True

    def rotate(
        self,
        component_id,
        angle,
    ):
        component = self.get(
            component_id
        )

        if component is None:
            return False

        method = getattr(
            component,
            "rotate",
            None,
        )

        if callable(method):
            method(angle)

        else:
            component.rotation = (
                float(
                    getattr(
                        component,
                        "rotation",
                        0,
                    )
                )
                + float(angle)
            ) % 360

        return True

    def bind_device(
        self,
        component_id,
        device,
    ):
        component = self.get(
            component_id
        )

        if component is None:
            return False

        binder = getattr(
            component,
            "bind_device",
            None,
        )

        if callable(binder):
            binder(device)
        else:
            component.device = device

        return True

    def update_devices(self):
        result = {}

        for component_id, component in (
            self.components.items()
        ):
            updater = getattr(
                component,
                "update_device",
                None,
            )

            if callable(updater):
                result[
                    component_id
                ] = updater()

        return result

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

            elif hasattr(
                component,
                "selected",
            ):
                component.selected = (
                    False
                )

    def clear(self):
        count = len(
            self.components
        )

        self.components.clear()

        return count

    def count(self):
        return len(
            self.components
        )

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
