"""
Motor principal do Runtime UAP.
"""

import threading
import time

from app.runtime.registry import (
    registry,
)

from app.runtime.scheduler import (
    scheduler,
)

from app.runtime.command_processor import (
    command_processor,
)

from app.runtime.logger import (
    runtime_logger,
)

from app.runtime.metrics import (
    runtime_metrics,
)

from app.runtime.config import (
    runtime_config,
)


class RuntimeEngine:

    def __init__(self):

        self.running = False
        self.thread = None
        self.cycle = 0
        self._lock = threading.Lock()

    def start(self):

        with self._lock:

            if self.running:
                return False

            runtime_logger.info(
                "Runtime Engine started"
            )

            self.running = True

            self.thread = threading.Thread(
                target=self.loop,
                daemon=True,
                name="uap-runtime",
            )

            self.thread.start()

            return True

    def stop(self):

        with self._lock:

            if not self.running:
                return False

            runtime_logger.info(
                "Runtime Engine stopped"
            )

            self.running = False

        thread = self.thread

        if (
            thread is not None
            and thread is not threading.current_thread()
        ):

            thread.join(
                timeout=2.0
            )

        self.thread = None

        return True

    def restart(self):

        self.stop()

        return self.start()

    def status(self):

        return {
            "running": self.running,
            "cycle": self.cycle,
            "queue": (
                command_processor
                and self._queue_size()
            ),
            "registry": registry.stats(),
            "metrics": runtime_metrics.status(),
        }

    def loop(self):

        while self.running:

            started = time.monotonic()

            try:

                self.execute_cycle()

            except Exception as exc:

                runtime_metrics.error()

                runtime_logger.error(
                    str(exc)
                )

            elapsed = (
                time.monotonic()
                - started
            )

            interval = max(
                0.0,
                runtime_config.ENGINE_CYCLE_TIME
                - elapsed,
            )

            if interval:

                time.sleep(
                    interval
                )

    def execute_cycle(self):

        self.cycle += 1

        runtime_metrics.cycle()

        scheduler.execute()

        command_processor.process()

        self._update_collection(
            registry.drivers
        )

        self._update_collection(
            registry.devices
        )

        self._update_collection(
            registry.flows
        )

        self._update_collection(
            registry.automations
        )

    @staticmethod
    def _update_collection(
        collection,
    ):

        for item in list(
            collection.values()
        ):

            update = getattr(
                item,
                "update",
                None,
            )

            execute = getattr(
                item,
                "execute",
                None,
            )

            if callable(update):

                update()

            elif callable(execute):

                execute()

    @staticmethod
    def _queue_size():

        from app.runtime.command_queue import (
            command_queue,
        )

        return command_queue.size()


engine = RuntimeEngine()
