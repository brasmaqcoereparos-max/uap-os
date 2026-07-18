class CompilerDefineManager:

    def __init__(self):

        self.defines = {}

    def add(
        self,
        name,
        value="",
    ):

        self.defines[name] = value

    def remove(
        self,
        name,
    ):

        self.defines.pop(name, None)

    def exists(
        self,
        name,
    ):

        return name in self.defines

    def all(self):

        return self.defines.copy()

    def clear(self):

        self.defines.clear()


compiler_define_manager = CompilerDefineManager()
