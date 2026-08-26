from app.runtime.runtime_context import (
    runtime_context,
)

from app.runtime.runtime_events import (
    runtime_events,
)

from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)


class RuntimeBoot:

    def start(self):

        register_builtin_drivers()

        runtime_context.running = True

        runtime_events.emit(
            "runtime.started",
            "runtime_boot",
            {
                "mode": runtime_context.mode,
            },
        )

        return runtime_context.to_dict()

    def stop(self):

        runtime_context.running = False

        runtime_events.emit(
            "runtime.stopped",
            "runtime_boot",
        )

        return runtime_context.to_dict()


runtime_boot = RuntimeBoot()
