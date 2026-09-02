from app.modules.ui.component import (
    UIComponent,
)


class UIComponentRegistry:

    def __init__(self):
        self._components: dict[
            str,
            UIComponent,
        ] = {}

    def register(
        self,
        component: UIComponent,
    ):
        self._components[
            component.id
        ] = component

        return component

    def get(
        self,
        component_id: str,
    ):
        return self._components.get(
            component_id
        )

    def remove(
        self,
        component_id: str,
    ):
        return self._components.pop(
            component_id,
            None,
        )

    def list_all(self):
        return list(
            self._components.values()
        )

    def by_category(
        self,
        category: str,
    ):
        return [
            component
            for component
            in self._components.values()
            if component.category
            == category
        ]

    def clear(self):
        self._components.clear()


ui_component_registry = (
    UIComponentRegistry()
  )
