class ComponentLibrary:

    def __init__(self):

        self.components = {}

    def register(

        self,

        component_class,

    ):

        self.components[component_class.__name__] = component_class

    def get(

        self,

        name,

    ):

        return self.components.get(name)

    def all(self):

        return self.components.copy()


component_library = ComponentLibrary()
