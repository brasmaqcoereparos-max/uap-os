class CompilerIncludeManager:

    def __init__(self):

        self.includes = set()

    def add(
        self,
        include,
    ):

        self.includes.add(include)

    def remove(
        self,
        include,
    ):

        self.includes.discard(include)

    def exists(
        self,
        include,
    ):

        return include in self.includes

    def all(self):

        return sorted(self.includes)

    def clear(self):

        self.includes.clear()


compiler_include_manager = CompilerIncludeManager()
