from enum import Enum


class TeachUIState(Enum):

    IDLE = "idle"
    JOG = "jog"
    RECORDING = "recording"
    PLAYING = "playing"
    PAUSED = "paused"
    STOPPED = "stopped"


class TeachUIStateManager:

    def __init__(self):

        self.state = TeachUIState.IDLE

    def set(self, state):

        self.state = state

    def get(self):

        return self.state


teach_ui_state = TeachUIStateManager()
