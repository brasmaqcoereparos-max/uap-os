"""
Inicialização dos backends de compilação do UAP.
"""

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
from app.modules.simulator.programming.compiler.backends.python_backend import (
    python_backend,
)
from app.modules.simulator.programming.compiler.backends.micropython_backend import (
    micropython_backend,
)
from app.modules.simulator.programming.compiler.backends.raspberry_backend import (
    raspberry_backend,
)
from app.modules.simulator.programming.compiler.backends.json_backend import (
    json_backend,
)
from app.modules.simulator.programming.compiler.backends.text_backend import (
    text_backend,
)


class BackendInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:
            return

        backends = (
            arduino_backend,
            esp32_backend,
            rp2040_backend,
            stm32_backend,
            python_backend,
            micropython_backend,
            raspberry_backend,
            json_backend,
            text_backend,
        )

        for backend in backends:
            compiler_backend_manager.register(
                backend
            )

        cls.initialized = True

    @classmethod
    def reset(cls):

        from app.modules.simulator.programming.compiler.compiler_backend_registry import (
            compiler_backend_registry,
        )

        compiler_backend_registry.clear()
        cls.initialized = False
