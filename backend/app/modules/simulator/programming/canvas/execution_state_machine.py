from enum import Enum


class EngineState(Enum):

    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED = "paused"
    FINISHED = "finished"
    ERROR = "error"


class ExecutionStateMachine:

    def __init__(self):

        self.state = EngineState.STOPPED

    def start(self):

        self.state = EngineState.RUNNING

    def pause(self):

        self.state = EngineState.PAUSED

    def resume(self):

        self.state = EngineState.RUNNING

    def stop(self):

        self.state = EngineState.STOPPED

    def finish(self):

        self.state = EngineState.FINISHED

    def error(self):

        self.state = EngineState.ERROR

    def current(self):

        return self.state.value


execution_state_machine = ExecutionStateMachine()
