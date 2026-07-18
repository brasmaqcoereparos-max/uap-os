class CompilerLibraries:

    def __init__(self):

        self.libraries = set()

    def add(
        self,
        library,
    ):

        self.libraries.add(library)

    def remove(
        self,
        library,
    ):

        self.libraries.discard(library)

    def exists(
        self,
        library,
    ):

        return library in self.libraries

    def all(self):

        return sorted(self.libraries)

    def clear(self):

        self.libraries.clear()


compiler_libraries = CompilerLibraries()
