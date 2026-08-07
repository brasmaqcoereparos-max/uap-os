import time


class MotionPlayer:

    def __init__(self):

        self.running = False

        self.on_step = None

        self.on_event = None

    def play(

        self,

        sequence,

    ):

        self.running = True

        for step in sequence.steps:

            if not self.running:

                break

            if self.on_step:

                self.on_step(step)

            for event in step.events:

                if self.on_event:

                    self.on_event(event)

            time.sleep(step.delay)

    def stop(self):

        self.running = False


motion_player = MotionPlayer()
