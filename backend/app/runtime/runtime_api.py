from app.runtime.runtime_router import (
    runtime_router,
)


class RuntimeAPI:

    def execute(self, command):
        return runtime_router.route(
            command
        )

    def start(self):
        return runtime_router.route(
            {
                "domain": "runtime",
                "action": "runtime.start",
            }
        )

    def stop(self):
        return runtime_router.route(
            {
                "domain": "runtime",
                "action": "runtime.stop",
            }
        )

    def health(self):
        return runtime_router.route(
            {
                "domain": "runtime",
                "action": "runtime.health",
            }
        )

    def diagnostics(self):
        return runtime_router.route(
            {
                "domain": "runtime",
                "action": "runtime.diagnostics",
            }
        )


runtime_api = RuntimeAPI()
