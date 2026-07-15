from datetime import datetime


class RuntimeLogger:

    def __init__(self):
        self.logs = []

    def info(self, message: str):
        self.logs.append({
            "level": "INFO",
            "message": message,
            "timestamp": datetime.now().isoformat(),
        })

    def warning(self, message: str):
        self.logs.append({
            "level": "WARNING",
            "message": message,
            "timestamp": datetime.now().isoformat(),
        })

    def error(self, message: str):
        self.logs.append({
            "level": "ERROR",
            "message": message,
            "timestamp": datetime.now().isoformat(),
        })

    def latest(self, limit: int = 100):
        return self.logs[-limit:]

    def clear(self):
        self.logs.clear()


runtime_logger = RuntimeLogger()
