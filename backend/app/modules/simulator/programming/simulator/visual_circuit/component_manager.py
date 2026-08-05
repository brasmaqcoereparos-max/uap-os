class ComponentManager:

    def __init__(self):

        self.components = {}

    def add(

        self,

        component,

    ):

        self.components[component.id] = component

    def get(

        self,

        component_id,

    ):

        return self.components.get(component_id)

    def remove(

        self,

        component_id,

    ):

        self.components.pop(

            component_id,

            None,

        )

    def all(self):

        return list(self.components.values())


component_manager = ComponentManager()
