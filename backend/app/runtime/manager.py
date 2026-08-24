"""
Gerenciador principal do Runtime UAP.
"""

from app.runtime.engine import (
    engine,
)

from app.runtime.lifecycle import (
    runtime_lifecycle,
)

from app.runtime.logger import (
    runtime_logger,
)


class RuntimeManager:

    def start(self):

        runtime_logger.info(
            "Starting Runtime Manager"
        )

        if not runtime_lifecycle.startup():
            return False

        return engine.start()

    def stop(self):

        runtime_logger.info(
            "Stopping Runtime Manager"
        )

        engine.stop()

        return runtime_lifecycle.shutdown()

    def restart(self):

        self.stop()

        return self.start()

    def status(self):

        return engine.status()

    def is_running(self):

        status = self.status()

        return bool(
            status.get(
                "running",
                False,
            )
        )


runtime_manager = RuntimeManager()
