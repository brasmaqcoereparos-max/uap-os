class SelectionManager:

    def __init__(self):

        self.selected = []

    def clear(self):

        self.selected.clear()

    def add(

        self,

        component,

    ):

        if component not in self.selected:

            self.selected.append(component)

    def remove(

        self,

        component,

    ):

        if component in self.selected:

            self.selected.remove(component)

    def all(self):

        return self.selected.copy()


selection_manager = SelectionManager()
