from app.runtime.engine import engine


class RuntimeManager:

    @staticmethod
    def start():
        engine.start()

    @staticmethod
    def stop():
        engine.stop()

    @staticmethod
    def restart():
        engine.stop()
        engine.start()

    @staticmethod
    def status():
        return engine.status()
