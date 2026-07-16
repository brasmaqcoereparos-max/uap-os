import copy


class CanvasTemplates:

    def __init__(self):

        self.templates = {}

    def save(
        self,
        name,
        canvas,
    ):

        self.templates[name] = copy.deepcopy(
            canvas.status()
        )

    def load(
        self,
        name,
    ):

        return copy.deepcopy(
            self.templates.get(name)
        )

    def delete(
        self,
        name,
    ):

        self.templates.pop(
            name,
            None,
        )

    def list(self):

        return sorted(
            self.templates.keys()
        )


templates = CanvasTemplates()
