class Layer:

    def __init__(self, name):

        self.name = name

        self.visible = True

        self.locked = False

    def to_dict(self):

        return {
            "name": self.name,
            "visible": self.visible,
            "locked": self.locked,
        }


class LayerManager:

    def __init__(self):

        self.layers = {
            "Default": Layer("Default")
        }

    def add(self, name):

        if name not in self.layers:
            self.layers[name] = Layer(name)

    def remove(self, name):

        if name != "Default":
            self.layers.pop(name, None)

    def all(self):

        return [
            layer.to_dict()
            for layer in self.layers.values()
        ]


layers = LayerManager()
