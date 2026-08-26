from app.runtime.runtime_boot import runtime_boot
from app.runtime.runtime_executor import runtime_executor
from app.runtime.runtime_health import runtime_health


class RuntimeService:

    def start(self):
        return runtime_boot.start()

    def stop(self):
        return runtime_boot.stop()

    def status(self):
        return runtime_health.check()

    def diagnostics(self):
        return runtime_health.diagnostics()

    def execute(self, command):
        return runtime_executor.execute(command)

    def execute_many(self, commands):
        return runtime_executor.execute_many(commands)


runtime_service = RuntimeService()
