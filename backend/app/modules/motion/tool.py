class MotionTool:

    def __init__(

        self,

        name,

    ):

        self.name = name

        self.outputs = {}

    def set_output(

        self,

        channel,

        value,

    ):

        self.outputs[channel] = value

    def get_output(

        self,

        channel,

    ):

        return self.outputs.get(channel)
