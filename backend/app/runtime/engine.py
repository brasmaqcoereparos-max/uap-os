import threading
import time

from app.runtime.registry import registry
from app.runtime.scheduler import scheduler
from app.runtime.command_queue import command_queue
from app.runtime.command_processor import command_processor
from app.runtime.logger import runtime_logger
from app.runtime.metrics import runtime_metrics
from app.runtime.config import runtime_config


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

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        return {
            "running": self.running,
            "cycle": self.cycle,
            "queue": command_queue.size(),
            "registry": registry.stats(),
            "metrics": runtime_metrics.status(),
        }

    def loop(self):
        while self.running:
            try:
                self.execute_cycle()

            except Exception as exc:
                runtime_metrics.error()
                runtime_logger.error(str(exc))

            time.sleep(
                runtime_config.ENGINE_CYCLE_TIME
            )

    def execute_cycle(self):
        self.cycle += 1
        runtime_metrics.cycle()

        scheduler.execute()

        command_processor.process()

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
