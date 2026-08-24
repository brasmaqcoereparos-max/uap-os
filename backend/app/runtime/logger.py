from datetime import datetime
from threading import Lock


class RuntimeLogger:

    def __init__(self):
        self.logs = []
        self.lock = Lock()

    def _write(
        self,
        level,
        message,
    ):

        entry = {
            "level": str(level).upper(),
            "message": str(message),
            "timestamp": datetime.now().isoformat(),
        }

        with self.lock:
            self.logs.append(entry)

        return entry

    def info(self, message: str):
        return self._write(
            "INFO",
            message,
        )

    def warning(self, message: str):
        return self._write(
            "WARNING",
            message,
        )

    def error(self, message: str):
        return self._write(
            "ERROR",
            message,
        )

    def latest(
        self,
        limit: int = 100,
    ):

        try:
            limit = max(
                0,
                int(limit),
            )
        except (
            TypeError,
            ValueError,
        ):
            limit = 100

        with self.lock:

            if limit == 0:
                return []

            return list(
                self.logs[-limit:]
            )

    def clear(self):

        with self.lock:
            self.logs.clear()


runtime_logger = RuntimeLogger()
