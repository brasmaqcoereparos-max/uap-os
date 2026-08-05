class Clipboard:

    def __init__(self):

        self.data = None

    def copy(

        self,

        obj,

    ):

        self.data = obj

    def paste(self):

        return self.data


clipboard = Clipboard()
