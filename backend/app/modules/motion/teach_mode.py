from app.modules.motion.motion_step import MotionStep


class TeachMode:

    def __init__(self):

        self.enabled = False

        self.current_sequence = None

        self.current_tool = None

        self.home_position = None

    def start(

        self,

        sequence,

    ):

        self.enabled = True

        self.current_sequence = sequence

    def stop(self):

        self.enabled = False

    def set_home(

        self,

        position,

    ):

        self.home_position = position.copy()

    def get_home(self):

        return self.home_position

    def select_tool(

        self,

        tool,

    ):

        self.current_tool = tool

    def record_position(

        self,

        position,

        name="",

    ):

        if not self.enabled:

            return None

        step = MotionStep(name)

        step.position = position.copy()

        step.tool = self.current_tool

        self.current_sequence.add_step(step)

        return step


teach_mode = TeachMode()
