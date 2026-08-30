"""
Loader de periféricos do UAP Peripheral SDK.

Permite carregar classes de periféricos de módulos Python
e registrá-las no PeripheralRegistry sem acoplar o SDK
a uma lista fixa de componentes.
"""

import importlib
import inspect

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_base import (
    PeripheralBase,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_registry import (
    peripheral_registry,
)


class PeripheralLoader:

    loaded = False

    loaded_modules = set()
    loaded_classes = set()
    errors = []

    @classmethod
    def load(
        cls,
        modules=None,
        registry=None,
        strict=False,
    ):
        registry = (
            registry
            or peripheral_registry
        )

        modules = list(
            modules or []
        )

        if not modules:
            cls.loaded = True

            return {
                "loaded": True,
                "modules": list(
                    cls.loaded_modules
                ),
                "classes": list(
                    cls.loaded_classes
                ),
                "errors": list(
                    cls.errors
                ),
            }

        for module_name in modules:
            cls.load_module(
                module_name,
                registry=registry,
                strict=strict,
            )

        cls.loaded = True

        return {
            "loaded": True,
            "modules": sorted(
                cls.loaded_modules
            ),
            "classes": sorted(
                cls.loaded_classes
            ),
            "errors": list(
                cls.errors
            ),
        }

    @classmethod
    def load_module(
        cls,
        module_name,
        registry=None,
        strict=False,
    ):
        registry = (
            registry
            or peripheral_registry
        )

        module_name = str(
            module_name
        )

        try:
            module = (
                importlib.import_module(
                    module_name
                )
            )

        except Exception as exc:
            error = {
                "module": (
                    module_name
                ),
                "error": str(exc),
            }

            cls.errors.append(
                error
            )

            if strict:
                raise

            return []

        registered = []

        for _, candidate in (
            inspect.getmembers(
                module,
                inspect.isclass,
            )
        ):
            if candidate is (
                PeripheralBase
            ):
                continue

            if not issubclass(
                candidate,
                PeripheralBase,
            ):
                continue

            if (
                candidate.__module__
                != module.__name__
            ):
                continue

            try:
                registry.register(
                    candidate
                )

                registered.append(
                    candidate
                )

                cls.loaded_classes.add(
                    candidate.__name__
                )

            except Exception as exc:
                error = {
                    "module": (
                        module_name
                    ),
                    "class": (
                        candidate.__name__
                    ),
                    "error": (
                        str(exc)
                    ),
                }

                cls.errors.append(
                    error
                )

                if strict:
                    raise

        cls.loaded_modules.add(
            module_name
        )

        cls.loaded = True

        return registered

    @classmethod
    def load_class(
        cls,
        module_name,
        class_name,
        registry=None,
    ):
        registry = (
            registry
            or peripheral_registry
        )

        module = (
            importlib.import_module(
                str(module_name)
            )
        )

        peripheral_class = getattr(
            module,
            str(class_name),
        )

        if not inspect.isclass(
            peripheral_class
        ):
            raise TypeError(
                f"{class_name} não é uma classe."
            )

        if not issubclass(
            peripheral_class,
            PeripheralBase,
        ):
            raise TypeError(
                f"{class_name} não herda "
                "PeripheralBase."
            )

        registry.register(
            peripheral_class
        )

        cls.loaded_modules.add(
            str(module_name)
        )

        cls.loaded_classes.add(
            peripheral_class.__name__
        )

        cls.loaded = True

        return peripheral_class

    @classmethod
    def is_loaded(cls):
        return cls.loaded

    @classmethod
    def reset(cls):
        cls.loaded = False

        cls.loaded_modules.clear()
        cls.loaded_classes.clear()
        cls.errors.clear()

        return True

    @classmethod
    def status(cls):
        return {
            "loaded": cls.loaded,
            "loaded_modules": sorted(
                cls.loaded_modules
            ),
            "loaded_classes": sorted(
                cls.loaded_classes
            ),
            "errors": list(
                cls.errors
            ),
        }
