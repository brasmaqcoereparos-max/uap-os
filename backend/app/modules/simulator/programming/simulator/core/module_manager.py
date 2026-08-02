class ModuleManager:

    def __init__(self):

        self.modules = []

    def register(

        self,

        module,

    ):

        module.register()

        self.modules.append(module)

    def boot(self):

        for module in self.modules:

            module.boot()

    def all(self):

        return self.modules.copy()


module_manager = ModuleManager()
