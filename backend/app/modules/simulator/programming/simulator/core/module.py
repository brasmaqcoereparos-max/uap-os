"""
Classe base dos módulos do Core UAP.

Mantém:
    Module.name
    Module.version
    register()
    boot()
"""


class Module:

    name = "Module"
    version = "1.0"

    def __init__(self):
        self.registered = False
        self.booted = False
        self.enabled = True

        self.register_count = 0
        self.boot_count = 0

        self.last_error = None

    def register(self):
        self.registered = True
        self.register_count += 1

        return True

    def boot(self):
        if not self.enabled:
            return False

        if not self.registered:
            self.register()

        self.booted = True
        self.boot_count += 1

        return True

    def shutdown(self):
        self.booted = False

        return True

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False
        self.booted = False

        return True

    def reset(self):
        self.registered = False
        self.booted = False

        self.register_count = 0
        self.boot_count = 0

        self.last_error = None

        return True

    def status(self):
        return {
            "name": self.name,
            "version": self.version,
            "registered": (
                self.registered
            ),
            "booted": self.booted,
            "enabled": self.enabled,
            "register_count": (
                self.register_count
            ),
            "boot_count": (
                self.boot_count
            ),
            "last_error": (
                self.last_error
            ),
        }

    def to_dict(self):
        return self.status()
