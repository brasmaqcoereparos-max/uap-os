from app.runtime.engine import engine
from app.runtime.lifecycle import runtime_lifecycle
from app.runtime.logger import runtime_logger


class RuntimeManager:

    @staticmethod
    def start():
        runtime_logger.info("Starting Runtime Manager")

        runtime_lifecycle.startup()

        engine.start()

    @staticmethod
    def stop():
        runtime_logger.info("Stopping Runtime Manager")

        engine.stop()

        runtime_lifecycle.shutdown()

    @staticmethod
    def restart():
        RuntimeManager.stop()
        RuntimeManager.start()

    @staticmethod
    def status():
        return engine.status()
