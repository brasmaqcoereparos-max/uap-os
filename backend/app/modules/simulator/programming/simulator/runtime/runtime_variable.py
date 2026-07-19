class RuntimeVariable:

    def __init__(

        self,

        name,

        value=None,

    ):

        self.name = name

        self.value = value

    def set(

        self,

        value,

    ):

        self.value = value

    def get(self):

        return self.value
