import threading
import time

from app.runtime.registry import registry
from app.runtime.scheduler import scheduler


class RuntimeEngine:

    def __init__(self):
        self.running = False
        self.thread = None
        self.cycle = 0

    def start(self):
        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.loop,
            daemon=True,
        )

        self.thread.start()

    def stop(self):
        self.running = False

    def status(self):
        return {
            "running": self.running,
            "cycle": self.cycle,
            "registry": registry.stats(),
        }

    def loop(self):
        while self.running:
            self.execute_cycle()
            time.sleep(0.1)

    def execute_cycle(self):
        self.cycle += 1

        scheduler.execute()

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
