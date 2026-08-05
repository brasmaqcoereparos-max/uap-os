class Canvas:

    def __init__(self):

        self.width = 10000

        self.height = 10000

        self.zoom = 1.0

        self.offset_x = 0

        self.offset_y = 0

    def set_zoom(

        self,

        zoom,

    ):

        self.zoom = zoom

    def move(

        self,

        dx,

        dy,

    ):

        self.offset_x += dx

        self.offset_y += dy


canvas = Canvas()
