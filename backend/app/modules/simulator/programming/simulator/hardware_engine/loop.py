"""
Loop principal do motor UAP.

Integra:
    Runtime
    Devices
    Timers
    Hardware Engine
"""

from app.modules.simulator.programming.simulator.hardware_engine.device_runner import (
    DeviceRunner,
)

from app.modules.simulator.programming.simulator.runtime.runtime_engine import (
    runtime_engine,
)


class SimulationLoop:

    def __init__(self):
        self.running = False
        self.paused = False

        self.device_runner = (
            DeviceRunner()
        )

        self.tick_count = 0

        self.last_error = None

    def start(self):
        if self.running:
            return True

        try:
            self.device_runner.start()
            runtime_engine.start()

            self.running = True
            self.paused = False

            self.last_error = None

            return True

        except Exception as exc:
            self.running = False
            self.paused = False

            self.last_error = str(exc)

            raise

    def stop(self):
        try:
            runtime_engine.stop()

        finally:
            self.device_runner.stop()

        self.running = False
        self.paused = False

        return True

    def pause(self):
        if not self.running:
            return False

        self.paused = True

        pause_method = getattr(
            runtime_engine,
            "pause",
            None,
        )

        if callable(
            pause_method
        ):
            pause_method()

        return True

    def resume(self):
        if not self.running:
            return False

        self.paused = False

        resume_method = getattr(
            runtime_engine,
            "resume",
            None,
        )

        if callable(
            resume_method
        ):
            resume_method()

        return True

    def tick(self):
        if (
            not self.running
            or self.paused
        ):
            return None

        try:
            device_result = (
                self.device_runner.update()
            )

            runtime_result = (
                runtime_engine.update()
            )

            self.tick_count += 1
            self.last_error = None

            return {
                "tick": (
                    self.tick_count
                ),
                "devices": (
                    device_result
                ),
                "runtime": (
                    runtime_result
                ),
            }

        except Exception as exc:
            self.last_error = str(exc)

            raise

    def reset(self):
        runtime_result = (
            runtime_engine.reset()
        )

        device_result = (
            self.device_runner.reset()
        )

        self.running = False
        self.paused = False

        self.tick_count = 0
        self.last_error = None

        return {
            "runtime": (
                runtime_result
            ),
            "devices": (
                device_result
            ),
        }

    def is_running(self):
        return self.running

    def is_paused(self):
        return self.paused

    def status(self):
        runtime_status = getattr(
            runtime_engine,
            "status",
            None,
        )

        return {
            "running": self.running,
            "paused": self.paused,
            "tick_count": (
                self.tick_count
            ),
            "last_error": (
                self.last_error
            ),
            "device_runner": (
                self.device_runner.status()
            ),
            "runtime": (
                runtime_status()
                if callable(
                    runtime_status
                )
                else None
            ),
        }
