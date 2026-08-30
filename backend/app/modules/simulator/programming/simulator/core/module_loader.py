"""
Carregador dos módulos padrão do Core UAP.

Mantém DeviceModule como módulo padrão.
"""

from app.modules.simulator.programming.simulator.core.module_manager import (
    module_manager,
)

from app.modules.simulator.programming.simulator.core.device_module import (
    DeviceModule,
)


class ModuleLoader:

    loaded = False

    module_classes = [
        DeviceModule,
    ]

    @classmethod
    def load(cls):
        if cls.loaded:
            return module_manager.all()

        for module_class in (
            cls.module_classes
        ):
            module = module_class()

            module_manager.register(
                module
            )

        cls.loaded = True

        return module_manager.all()

    @classmethod
    def register_module(
        cls,
        module_class,
    ):
        if module_class not in (
            cls.module_classes
        ):
            cls.module_classes.append(
                module_class
            )

        return module_class

    @classmethod
    def unregister_module(
        cls,
        module_class,
    ):
        if module_class not in (
            cls.module_classes
        ):
            return False

        cls.module_classes.remove(
            module_class
        )

        return True

    @classmethod
    def available(cls):
        return list(
            cls.module_classes
        )

    @classmethod
    def reset(cls):
        cls.loaded = False

        return True

    @classmethod
    def status(cls):
        return {
            "loaded": cls.loaded,
            "module_classes": [
                getattr(
                    item,
                    "name",
                    item.__name__,
                )
                for item
                in cls.module_classes
            ],
        }
