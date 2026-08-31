from app.modules.vision.ai.model_registry import (
    model_registry,
)


class AIModelManager:

    def register(
        self,
        name,
        model,
        auto_load=True,
    ):

        if auto_load:

            load = getattr(
                model,
                "load",
                None,
            )

            if callable(load):
                load()

        return model_registry.register(
            name,
            model,
        )

    def unregister(self, name):

        model = model_registry.remove(
            name
        )

        if model is not None:

            close = getattr(
                model,
                "close",
                None,
            )

            if callable(close):
                close()

        return model

    def get(self, name):

        model = model_registry.get(
            name
        )

        if model is None:
            raise KeyError(
                f"Modelo '{name}' não encontrado."
            )

        return model

    def list(self):

        return model_registry.list()

    def status(self, name):

        model = self.get(name)

        status = getattr(
            model,
            "status",
            None,
        )

        if callable(status):
            return status()

        return {
            "name": name,
            "loaded": False,
        }

    def status_all(self):

        return {
            name: self.status(name)
            for name in model_registry.names()
        }


ai_model_manager = AIModelManager()
