class NodeStyle:

    def __init__(self):

        self.default = {

            "width": 180,

            "height": 70,

            "radius": 8,

            "border": "#666666",

            "background": "#2D2D2D",

            "text": "#FFFFFF",

            "font_size": 13,

        }

    def get(self):

        return self.default.copy()

    def update(
        self,
        values,
    ):

        self.default.update(values)

        return self.get()


node_style = NodeStyle()
