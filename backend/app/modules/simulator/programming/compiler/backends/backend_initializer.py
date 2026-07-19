from app.modules.simulator.programming.compiler.compiler_backend_manager import (
    compiler_backend_manager,
)

from app.modules.simulator.programming.compiler.backends.arduino_backend import (
    arduino_backend,
)


class BackendInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:

            return

        compiler_backend_manager.register(

            arduino_backend,

        )

        cls.initialized = True
