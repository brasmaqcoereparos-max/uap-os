class ModelRegistry:

    def __init__(self):
        self._models = {}

    def register(
        self,
        name,
        model,
    ):

        if not name:
            raise ValueError(
                "Nome do modelo obrigatório."
            )

        if model is None:
            raise ValueError(
                "Modelo inválido."
            )

        self._models[
            str(name)
        ] = model

        return model

    def get(self, name):

        return self._models.get(
            str(name)
        )

    def remove(self, name):

        return self._models.pop(
            str(name),
            None,
        )

    def exists(self, name):

        return (
            str(name)
            in self._models
        )

    def list(self):

        return dict(
            self._models
        )

    def names(self):

        return list(
            self._models.keys()
        )

    def count(self):

        return len(
            self._models
        )

    def clear(self):

        self._models.clear()


model_registry = ModelRegistry()
