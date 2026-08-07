class MotionLibrary:

    def __init__(self):

        self.library = {}

    def add(

        self,

        name,

        sequence,

    ):

        self.library[name] = sequence

    def get(

        self,

        name,

    ):

        return self.library.get(name)

    def remove(

        self,

        name,

    ):

        self.library.pop(name, None)

    def list(self):

        return list(self.library.keys())


motion_library = MotionLibrary()
