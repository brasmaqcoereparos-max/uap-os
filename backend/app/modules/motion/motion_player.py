import time


class MotionPlayer:

    def __init__(self):

        self.running = False

    def play(

        self,

        sequence,

        callback,

    ):

        self.running = True

        for step in sequence.steps:

            if not self.running:

                break

            callback(step)

            time.sleep(step.delay)

    def stop(self):

        self.running = False


motion_player = MotionPlayer()
