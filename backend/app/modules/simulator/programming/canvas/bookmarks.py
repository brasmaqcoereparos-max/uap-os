class BookmarkManager:

    def __init__(self):

        self.bookmarks = {}

    def add(
        self,
        name,
        x,
        y,
        zoom,
    ):

        self.bookmarks[name] = {
            "x": x,
            "y": y,
            "zoom": zoom,
        }

    def remove(
        self,
        name,
    ):

        self.bookmarks.pop(
            name,
            None,
        )

    def get(
        self,
        name,
    ):

        return self.bookmarks.get(name)

    def all(self):

        return self.bookmarks


bookmarks = BookmarkManager()
