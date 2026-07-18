from app.modules.simulator.programming.compiler.compiler_context import (
    compiler_context,
)


class CompilerBase:

    def compile(self, canvas):

        raise NotImplementedError()

    def context(self):

        return compiler_context

    def reset(self):

        compiler_context.includes.clear()

        compiler_context.definitions.clear()

        compiler_context.globals.clear()

        compiler_context.setup.clear()

        compiler_context.loop.clear()

        compiler_context.variables.clear()
