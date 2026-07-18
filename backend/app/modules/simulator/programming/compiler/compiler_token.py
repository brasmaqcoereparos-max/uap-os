class CompilerToken:

    def __init__(

        self,

        token_type,

        value,

        line=0,

        column=0,

    ):

        self.type = token_type

        self.value = value

        self.line = line

        self.column = column

    def to_dict(self):

        return {

            "type": self.type,

            "value": self.value,

            "line": self.line,

            "column": self.column,

        }
