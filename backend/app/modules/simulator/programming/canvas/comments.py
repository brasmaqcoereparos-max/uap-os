class Comment:

    def __init__(
        self,
        x,
        y,
        text,
    ):

        self.x = x

        self.y = y

        self.text = text

    def to_dict(self):

        return {

            "x": self.x,

            "y": self.y,

            "text": self.text,

        }


class CommentManager:

    def __init__(self):

        self.comments = []

    def add(
        self,
        x,
        y,
        text,
    ):

        self.comments.append(

            Comment(
                x,
                y,
                text,
            )

        )

    def clear(self):

        self.comments.clear()

    def all(self):

        return [

            c.to_dict()

            for c in self.comments

        ]


comments = CommentManager()
