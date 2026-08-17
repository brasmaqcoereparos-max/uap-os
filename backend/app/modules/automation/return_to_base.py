class ReturnToBase:

    def __init__(
        self,
        navigation,
    ):

        self.navigation = navigation
        self.active = False

    def start(self):

        self.active = True

    def stop(self):

        self.active = False

    def is_active(self):

        return self.active

    def update(self):

        if not self.active:

            return None

        return {
            "action": "return_to_base"
        }
