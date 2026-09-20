from __future__ import annotations

import threading
import time
from typing import Callable


class PipelineScheduler:

    def __init__(self):
        self._running = False

        self._thread: (
            threading.Thread | None
        ) = None

        self._stop_event = (
            threading.Event()
        )

        self._lock = (
            threading.RLock()
        )

        self._cycles = 0

        self._last_error: (
            str | None
        ) = None

    def start(
        self,
        callback: Callable,
        interval: float = 0.1,
    ):
        if not callable(
            callback
        ):
            raise TypeError(
                "callback deve ser executável."
            )

        normalized_interval = max(
            0.01,
            float(interval),
        )

        with self._lock:
            if self._running:
                return False

            self._running = True

            self._cycles = 0

            self._last_error = None

            self._stop_event.clear()

            self._thread = (
                threading.Thread(
                    target=self._loop,
                    args=(
                        callback,
                        normalized_interval,
                    ),
                    daemon=True,
                )
            )

            self._thread.start()

        return True

    def _loop(
        self,
        callback: Callable,
        interval: float,
    ):
        try:
            while (
                not self._stop_event
                .is_set()
            ):
                try:
                    callback()

                    with self._lock:
                        self._cycles += 1

                except Exception as exc:
                    with self._lock:
                        self._last_error = (
                            str(exc)
                        )

                if (
                    self._stop_event.wait(
                        interval
                    )
                ):
                    break

        finally:
            with self._lock:
                self._running = False

    def stop(self):
        with self._lock:
            self._running = False

            self._stop_event.set()

            thread = self._thread

        if (
            thread
            and thread.is_alive()
            and thread
            is not threading.current_thread()
        ):
            thread.join(
                timeout=1.0
            )

        with self._lock:
            self._thread = None

        return True

    def running(self):
        with self._lock:
            return self._running

    def cycles(self) -> int:
        with self._lock:
            return self._cycles

    def last_error(
        self,
    ) -> str | None:
        with self._lock:
            return self._last_error

    def clear_error(self):
        with self._lock:
            self._last_error = None

    def status(self):
        with self._lock:
            return {
                "running": (
                    self._running
                ),
                "cycles": (
                    self._cycles
                ),
                "last_error": (
                    self._last_error
                ),
                "thread_alive": (
                    self._thread
                    is not None
                    and self._thread
                    .is_alive()
                ),
            }


pipeline_scheduler = (
    PipelineScheduler()
        )
