class RuntimeGoto(Exception):

    def __init__(

        self,

        label,

    ):

        self.label = label


def instruction_goto(

    label,

):

    raise RuntimeGoto(

        label,

    )
