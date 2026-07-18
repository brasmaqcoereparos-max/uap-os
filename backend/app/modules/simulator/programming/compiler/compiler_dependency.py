class CompilerDependency:

    def __init__(self):

        self.dependencies = {}

    def add(
        self,
        source,
        dependency,
    ):

        self.dependencies.setdefault(

            source,

            set(),

        ).add(dependency)

    def get(
        self,
        source,
    ):

        return sorted(

            self.dependencies.get(

                source,

                set(),

            )

        )

    def clear(self):

        self.dependencies.clear()

    def all(self):

        return {

            key: sorted(value)

            for key, value

            in self.dependencies.items()

        }


compiler_dependency = CompilerDependency()
