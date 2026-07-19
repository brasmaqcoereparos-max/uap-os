from app.modules.simulator.programming.compiler.compiler_backend_manager import (
    compiler_backend_manager,
)

from app.modules.simulator.programming.compiler.backends.arduino_backend import (
    arduino_backend,
)

from app.modules.simulator.programming.compiler.backends.esp32_backend import (
    esp32_backend,
)

from app.modules.simulator.programming.compiler.backends.rp2040_backend import (
    rp2040_backend,
)

from app.modules.simulator.programming.compiler.backends.stm32_backend import (
    stm32_backend,
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

        compiler_backend_manager.register(
            esp32_backend,
        )

        compiler_backend_manager.register(
            rp2040_backend,
        )

        compiler_backend_manager.register(
            stm32_backend,
        )

        cls.initialized = True
