import copy


class MacroManager:

    def __init__(self):

        self.macros = {}

    def save(
        self,
        name,
        nodes,
    ):

        self.macros[name] = copy.deepcopy(nodes)

    def load(
        self,
        name,
    ):

        if name not in self.macros:
            return []

        return copy.deepcopy(
            self.macros[name]
        )

    def remove(
        self,
        name,
    ):

        self.macros.pop(
            name,
            None,
        )

    def all(self):

        return sorted(
            self.macros.keys()
        )


macros = MacroManager()
