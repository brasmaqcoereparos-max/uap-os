from app.runtime.runtime_controller import (
    runtime_controller,
)


class RuntimeService:

    def start(self):
        return runtime_controller.start()

    def stop(self):
        return runtime_controller.stop()

    def status(self):
        return runtime_controller.status()

    def execute(self, command):
        return runtime_controller.execute(
            command
        )


runtime_service = RuntimeService()
