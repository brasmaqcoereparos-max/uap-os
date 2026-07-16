class SelectionBox:

    def __init__(self):

        self.active = False

        self.x1 = 0

        self.y1 = 0

        self.x2 = 0

        self.y2 = 0

    def start(self, x, y):

        self.active = True

        self.x1 = x

        self.y1 = y

        self.x2 = x

        self.y2 = y

    def update(self, x, y):

        self.x2 = x

        self.y2 = y

    def finish(self):

        self.active = False

    def bounds(self):

        return (

            min(self.x1, self.x2),

            min(self.y1, self.y2),

            max(self.x1, self.x2),

            max(self.y1, self.y2),

        )


selection_box = SelectionBox()
