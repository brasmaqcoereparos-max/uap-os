class SnapManager:

    def __init__(self):

        self.grid = True

        self.nodes = True

        self.guides = True

    def enable_all(self):

        self.grid = True
        self.nodes = True
        self.guides = True

    def disable_all(self):

        self.grid = False
        self.nodes = False
        self.guides = False

    def to_dict(self):

        return {
            "grid": self.grid,
            "nodes": self.nodes,
            "guides": self.guides,
        }


snap = SnapManager()
