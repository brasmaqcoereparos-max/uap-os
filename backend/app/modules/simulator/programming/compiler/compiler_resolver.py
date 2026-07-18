from app.modules.simulator.programming.compiler.compiler_dependency import (
    compiler_dependency,
)


class CompilerResolver:

    def resolve(self):

        resolved = []

        visited = set()

        for item in compiler_dependency.all():

            self._visit(

                item,

                visited,

                resolved,

            )

        return resolved

    def _visit(

        self,

        item,

        visited,

        resolved,

    ):

        if item in visited:

            return

        visited.add(item)

        for dependency in compiler_dependency.get(item):

            self._visit(

                dependency,

                visited,

                resolved,

            )

        resolved.append(item)


compiler_resolver = CompilerResolver()
