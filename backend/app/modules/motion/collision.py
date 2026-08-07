class CollisionDetector:

    def __init__(self):

        self.enabled = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def check(

        self,

        position,

    ):

        """
        Futuramente executará
        detecção de colisão.
        """

        return False


collision_detector = CollisionDetector()
