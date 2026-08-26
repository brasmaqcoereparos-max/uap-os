import threading
import time


class PipelineScheduler:

    def __init__(self):

        self._running = False
        self._thread = None

    def start(
        self,
        callback,
        interval: float = 0.1,
    ):

        if self._running:
            return False

        if not callable(callback):
            raise TypeError(
                "callback deve ser executável."
            )

        self._running = True

        def loop():

            while self._running:

                try:
                    callback()

                except Exception:
                    pass

                time.sleep(
                    max(
                        0.01,
                        float(interval),
                    )
                )

        self._thread = threading.Thread(
            target=loop,
            daemon=True,
        )

        self._thread.start()

        return True

    def stop(self):

        self._running = False

        if (
            self._thread
            and self._thread.is_alive()
        ):
            self._thread.join(
                timeout=1.0
            )

        self._thread = None

        return True

    def running(self):

        return self._running


pipeline_scheduler = PipelineScheduler()
