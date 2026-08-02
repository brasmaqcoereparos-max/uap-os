from app.modules.simulator.programming.simulator.core.kernel import (
    Kernel,
)


class Application:

    started = False

    @classmethod
    def start(cls):

        if cls.started:

            return

        Kernel.boot()

        cls.started = True
