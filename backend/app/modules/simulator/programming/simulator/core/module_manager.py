"""
Gerenciador central dos módulos do simulador UAP.

Mantém:
    modules
    register()
    boot()
    all()
    module_manager
"""


class ModuleManager:

    def __init__(self):
        self.modules = []

        self.boot_count = 0
        self.register_count = 0

        self.last_error = None

    def register(
        self,
        module,
    ):
        if module is None:
            return None

        if module in self.modules:
            return module

        try:
            module.register()

            self.modules.append(
                module
            )

            self.register_count += 1
            self.last_error = None

            return module

        except Exception as exc:
            self.last_error = str(exc)

            raise

    def unregister(
        self,
        module,
    ):
        if module not in self.modules:
            return False

        shutdown = getattr(
            module,
            "shutdown",
            None,
        )

        if callable(shutdown):
            shutdown()

        self.modules.remove(
            module
        )

        return True

    def get(
        self,
        name,
    ):
        name = str(name)

        for module in self.modules:
            if str(
                getattr(
                    module,
                    "name",
                    "",
                )
            ) == name:
                return module

        return None

    def exists(
        self,
        name,
    ):
        return (
            self.get(name)
            is not None
        )

    def boot(self):
        results = []

        try:
            for module in list(
                self.modules
            ):
                if not getattr(
                    module,
                    "enabled",
                    True,
                ):
                    continue

                results.append(
                    module.boot()
                )

            self.boot_count += 1
            self.last_error = None

            return results

        except Exception as exc:
            self.last_error = str(exc)

            raise

    def shutdown(self):
        results = []

        for module in reversed(
            self.modules
        ):
            shutdown = getattr(
                module,
                "shutdown",
                None,
            )

            if callable(shutdown):
                results.append(
                    shutdown()
                )

        return results

    def reset(self):
        for module in self.modules:
            reset = getattr(
                module,
                "reset",
                None,
            )

            if callable(reset):
                reset()

        self.boot_count = 0
        self.register_count = 0
        self.last_error = None

        return True

    def all(self):
        return self.modules.copy()

    def count(self):
        return len(
            self.modules
        )

    def clear(self):
        self.shutdown()

        count = len(
            self.modules
        )

        self.modules.clear()

        return count

    def status(self):
        return {
            "count": self.count(),
            "boot_count": (
                self.boot_count
            ),
            "register_count": (
                self.register_count
            ),
            "last_error": (
                self.last_error
            ),
            "modules": [
                (
                    module.status()
                    if hasattr(
                        module,
                        "status",
                    )
                    else {
                        "name": getattr(
                            module,
                            "name",
                            type(module).__name__,
                        )
                    }
                )
                for module
                in self.modules
            ],
        }


module_manager = ModuleManager()
