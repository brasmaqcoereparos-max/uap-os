from app.modules.motion.motion_sequence import MotionSequence


class MotionManager:

    def __init__(self):

        self.sequences = {}

        self.current_sequence = None

    def create_sequence(

        self,

        name,

    ):

        sequence = MotionSequence(name)

        self.sequences[name] = sequence

        self.current_sequence = sequence

        return sequence

    def get_sequence(

        self,

        name,

    ):

        return self.sequences.get(name)

    def remove_sequence(

        self,

        name,

    ):

        self.sequences.pop(name, None)

    def list_sequences(self):

        return list(self.sequences.keys())


motion_manager = MotionManager()
