class Pin:

    def __init__(

        self,

        number,

        name,

        modes=None,

    ):

        self.number = number

        self.name = name

        self.modes = modes or []

        self.value = 0
