import threading
import time

from app.runtime.registry import registry
from app.runtime.scheduler import scheduler
from app.runtime.command_queue import command_queue
from app.runtime.logger import runtime_logger
from app.runtime.websocket_manager import websocket_manager


class RuntimeEngine:

    def __init__(self):
        self.running = False
        self.thread = None
        self.cycle = 0

    def start(self):
        if self.running:
            return

        runtime_logger.info("Runtime Engine started")

        self.running = True

        self.thread = threading.Thread(
            target=self.loop,
            daemon=True,
        )

        self.thread.start()

    def stop(self):
        runtime_logger.info("Runtime Engine stopped")
        self.running = False

    def status(self):
        return {
            "running": self.running,
            "cycle": self.cycle,
            "registry": registry.stats(),
            "queue": command_queue.size(),
        }

    def loop(self):
        while self.running:
            try:
                self.execute_cycle()
            except Exception as exc:
                runtime_logger.error(str(exc))

            time.sleep(0.1)

    def execute_cycle(self):
        self.cycle += 1

        scheduler.execute()

        command = command_queue.get()

        if command:
            runtime_logger.info(f"Command: {command}")

        for driver in registry.drivers.values():
            if hasattr(driver, "update"):
                driver.update()

        for device in registry.devices.values():
            if hasattr(device, "update"):
                device.update()

        for flow in registry.flows.values():
            if hasattr(flow, "execute"):
                flow.execute()

        for automation in registry.automations.values():
            if hasattr(automation, "execute"):
                automation.execute()


engine = RuntimeEngine()
