class Container:

    def __init__(self):

        self.services = {}

    def bind(

        self,

        name,

        instance,

    ):

        self.services[name] = instance

    def resolve(

        self,

        name,

    ):

        return self.services.get(name)

    def exists(

        self,

        name,

    ):

        return name in self.services

    def clear(self):

        self.services.clear()


container = Container()
