from app.runtime.device_manager import (
    device_manager,
)


class RuntimeController:

    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

        return {
            "success": True,
            "running": True,
        }

    def stop(self):
        self.running = False

        return {
            "success": True,
            "running": False,
        }

    def status(self):
        return {
            "running": self.running,
        }

    def execute(self, command):
        if not self.running:
            self.start()

        return device_manager.execute(
            command
        )


runtime_controller = RuntimeController()
