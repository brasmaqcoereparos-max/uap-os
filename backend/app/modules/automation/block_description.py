class BlockDescription:

    def __init__(
        self,
        name,
        simple_description,
        technical_description="",
    ):

        self.name = name

        self.simple_description = (
            simple_description
        )

        self.technical_description = (
            technical_description
        )

    def simple(self):

        return self.simple_description

    def technical(self):

        return self.technical_description
