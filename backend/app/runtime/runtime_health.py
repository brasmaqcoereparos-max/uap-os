from app.runtime.runtime_context import (
    runtime_context,
)


class RuntimeHealth:

    def check(self):

        return {
            "status": (
                "ok"
                if runtime_context.running
                else "stopped"
            ),
            "running": runtime_context.running,
            "mode": runtime_context.mode,
        }

    def ready(self):

        return bool(
            runtime_context.running
        )

    def diagnostics(self):

        return {
            "ready": self.ready(),
            "context": runtime_context.to_dict(),
        }


runtime_health = RuntimeHealth()
