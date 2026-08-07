class HomeManager:

    def __init__(self):

        self.position = None

    def set(

        self,

        position,

    ):

        self.position = position

    def get(self):

        return self.position


home_manager = HomeManager()
