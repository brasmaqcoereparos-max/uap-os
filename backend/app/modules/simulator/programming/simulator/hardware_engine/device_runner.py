"""
Executor dos dispositivos físicos/virtuais do simulador UAP.

Responsável por:
- inicializar dispositivos;
- iniciar/parar execução;
- atualizar dispositivos por ciclo;
- contabilizar ciclos;
- registrar erros de atualização.
"""

from app.modules.simulator.programming.simulator.device.device_manager import (
    device_manager,
)

from app.modules.simulator.programming.simulator.device.device_initializer import (
    DeviceInitializer,
)


class DeviceRunner:

    def __init__(self):
        self.running = False
        self.initialized = False

        self.update_count = 0
        self.error_count = 0

        self.last_error = None

    def initialize(self):
        if self.initialized:
            return True

        try:
            DeviceInitializer.initialize()

            self.initialized = True
            self.last_error = None

            return True

        except Exception as exc:
            self.error_count += 1
            self.last_error = str(exc)

            raise

    def start(self):
        if self.running:
            return True

        self.initialize()

        self.running = True

        return True

    def stop(self):
        self.running = False

        return True

    def update(self):
        if not self.running:
            return None

        try:
            result = (
                device_manager.update_all()
            )

            self.update_count += 1
            self.last_error = None

            return result

        except Exception as exc:
            self.error_count += 1
            self.last_error = str(exc)

            raise

    def reset(self):
        result = (
            device_manager.reset_all()
        )

        self.running = False

        self.update_count = 0
        self.error_count = 0
        self.last_error = None

        return result

    def device_count(self):
        return device_manager.count()

    def devices(self):
        return device_manager.all()

    def is_running(self):
        return self.running

    def is_initialized(self):
        return self.initialized

    def status(self):
        return {
            "running": self.running,
            "initialized": (
                self.initialized
            ),
            "device_count": (
                self.device_count()
            ),
            "update_count": (
                self.update_count
            ),
            "error_count": (
                self.error_count
            ),
            "last_error": (
                self.last_error
            ),
        }

    def to_dict(self):
        return self.status()
