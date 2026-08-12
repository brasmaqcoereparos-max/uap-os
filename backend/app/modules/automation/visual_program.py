class VisualProgram:

    def __init__(
        self,
        name="Visual Program",
    ):

        self.name = name
        self.sequence = None
        self.description = ""

    def set_sequence(
        self,
        sequence,
    ):

        self.sequence = sequence

    def set_description(
        self,
        description,
    ):

        self.description = description

    def get_blocks(self):

        if self.sequence is None:
            return []

        return self.sequence.get_all()

    def to_dict(self):

        return {
            "name": self.name,
            "description": self.description,
            "blocks": [
                block.to_dict()
                for block in self.get_blocks()
            ],
        }
