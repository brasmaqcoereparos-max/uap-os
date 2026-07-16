class ColorPalette:

    def __init__(self):

        self.colors = [

            "#4CAF50",

            "#2196F3",

            "#FF9800",

            "#9C27B0",

            "#F44336",

            "#607D8B",

            "#009688",

            "#795548",

        ]

    def add(
        self,
        color,
    ):

        if color not in self.colors:

            self.colors.append(color)

    def remove(
        self,
        color,
    ):

        if color in self.colors:

            self.colors.remove(color)

    def all(self):

        return self.colors


palette = ColorPalette()
