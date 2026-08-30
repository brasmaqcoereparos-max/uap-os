"""
Aplicação principal do núcleo do simulador UAP.

Mantém o contrato original:
    Application.started
    Application.start()
"""

from app.modules.simulator.programming.simulator.core.kernel import (
    Kernel,
)


class Application:

    started = False
    start_count = 0
    last_error = None

    @classmethod
    def start(cls):
        if cls.started:
            return True

        try:
            Kernel.boot()

            cls.started = True
            cls.start_count += 1
            cls.last_error = None

            return True

        except Exception as exc:
            cls.started = False
            cls.last_error = str(exc)

            raise

    @classmethod
    def stop(cls):
        if not cls.started:
            return True

        shutdown = getattr(
            Kernel,
            "shutdown",
            None,
        )

        if callable(shutdown):
            shutdown()

        cls.started = False

        return True

    @classmethod
    def restart(cls):
        cls.stop()

        return cls.start()

    @classmethod
    def reset(cls):
        reset = getattr(
            Kernel,
            "reset",
            None,
        )

        if callable(reset):
            reset()

        cls.started = False
        cls.start_count = 0
        cls.last_error = None

        return True

    @classmethod
    def status(cls):
        kernel_status = getattr(
            Kernel,
            "status",
            None,
        )

        return {
            "started": cls.started,
            "start_count": cls.start_count,
            "last_error": cls.last_error,
            "kernel": (
                kernel_status()
                if callable(kernel_status)
                else None
            ),
        }
