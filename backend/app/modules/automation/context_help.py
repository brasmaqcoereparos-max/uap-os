class ContextHelp:

    def __init__(self):

        self.help_items = {}

    def register(
        self,
        key,
        title,
        description,
        example="",
    ):

        self.help_items[key] = {
            "title": title,
            "description": description,
            "example": example,
        }

    def get(
        self,
        key,
    ):

        return self.help_items.get(
            key
        )

    def list(self):

        return dict(
            self.help_items
        )


context_help = ContextHelp()
