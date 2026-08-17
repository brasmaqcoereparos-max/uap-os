class CleaningActionExecutor:

    def __init__(
        self,
        navigation,
        cleaning_system,
    ):

        self.navigation = navigation
        self.cleaning_system = cleaning_system

    def execute(self, action):

        if action.action == "move":

            speed = action.value or 0

            self.navigation.forward(
                speed
            )

        elif action.action == "brush":

            self.cleaning_system.brush.enable()

        elif action.action == "vacuum":

            self.cleaning_system.vacuum.enable()

        elif action.action == "water":

            self.cleaning_system.pump.water_on()

        elif action.action == "detergent":

            self.cleaning_system.pump.detergent_on()

        elif action.action == "dry":

            self.cleaning_system.dryer.enable()

        elif action.action == "stop":

            self.navigation.stop()

            self.cleaning_system.stop_cleaning()

        elif action.action == "return_base":

            self.navigation.stop()

        else:

            return False

        return True
