from datetime import datetime

from app.runtime.engine import engine
from app.runtime.registry import registry
from app.runtime.logger import runtime_logger


class RuntimeHealth:

    @staticmethod
    def status():
        return {
            "timestamp": datetime.now().isoformat(),
            "engine": engine.status(),
            "registry": registry.stats(),
            "logs": len(runtime_logger.logs),
            "healthy": engine.running,
        }


runtime_health = RuntimeHealth()
