from app.runtime.runtime_api import (
    runtime_api,
)


class RuntimeGateway:

    def execute(self, command):
        return runtime_api.execute(
            command
        )

    def start(self):
        return runtime_api.start()

    def stop(self):
        return runtime_api.stop()

    def health(self):
        return runtime_api.health()

    def diagnostics(self):
        return runtime_api.diagnostics()


runtime_gateway = RuntimeGateway()
