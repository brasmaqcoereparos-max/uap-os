class CanvasTheme:

    def __init__(self):

        self.theme = "dark"

        self.background = "#1e1e1e"

        self.grid = "#2d2d2d"

        self.selection = "#4fa3ff"

    def dark(self):

        self.theme = "dark"
        self.background = "#1e1e1e"
        self.grid = "#2d2d2d"
        self.selection = "#4fa3ff"

    def light(self):

        self.theme = "light"
        self.background = "#ffffff"
        self.grid = "#d0d0d0"
        self.selection = "#0066ff"

    def to_dict(self):

        return {
            "theme": self.theme,
            "background": self.background,
            "grid": self.grid,
            "selection": self.selection,
        }


theme = CanvasTheme()
