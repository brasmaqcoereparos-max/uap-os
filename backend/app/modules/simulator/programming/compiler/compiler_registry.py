class CompilerRegistry:

    def __init__(self):

        self.compilers = {}

    def register(

        self,

        platform,

        compiler,

    ):

        self.compilers[platform] = compiler

    def get(self, platform):

        return self.compilers.get(platform)

    def platforms(self):

        return sorted(

            self.compilers.keys()

        )


compiler_registry = CompilerRegistry()
