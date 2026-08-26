from app.runtime.runtime_gateway import (
    runtime_gateway,
)


class RuntimeService:

    def execute(self, command):
        return runtime_gateway.execute(
            command
        )

    def start(self):
        return runtime_gateway.start()

    def stop(self):
        return runtime_gateway.stop()

    def health(self):
        return runtime_gateway.health()

    def diagnostics(self):
        return runtime_gateway.diagnostics()


runtime_service = RuntimeService()
