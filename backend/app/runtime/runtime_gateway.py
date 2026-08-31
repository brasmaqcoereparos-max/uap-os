class RuntimeGateway:

    def _api(self):
        from app.runtime.runtime_api import (
            runtime_api,
        )

        return runtime_api

    def execute(
        self,
        command,
    ):
        return self._api().execute(
            command
        )

    def start(self):
        return self._api().start()

    def stop(self):
        return self._api().stop()

    def health(self):
        return self._api().health()

    def diagnostics(self):
        return self._api().diagnostics()


runtime_gateway = RuntimeGateway()
