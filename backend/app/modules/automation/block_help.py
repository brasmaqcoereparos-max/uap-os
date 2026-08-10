class BlockHelp:

    def __init__(
        self,
        title,
        description,
        example="",
    ):

        self.title = title
        self.description = description
        self.example = example

    def text(self):

        return {
            "title": self.title,
            "description": self.description,
            "example": self.example,
        }
